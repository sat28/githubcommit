from notebook.utils import url_path_join as ujoin
from notebook.base.handlers import IPythonHandler
import os, json, git, urllib, requests
from git import Repo, GitCommandError
from subprocess import check_output
import subprocess

class GitCommitHandler(IPythonHandler):

    def error_and_return(self, dirname, reason):

        # send error
        self.send_error(500, reason=reason)

        # return to directory
        os.chdir(dirname)

    def put(self):

        # git parameters from environment variables
        # expand variables since Docker's will pass VAR=$VAL as $VAL without expansion
        git_dir = "{}/{}".format(os.path.expandvars(os.environ.get('GIT_PARENT_DIR')), os.path.expandvars(os.environ.get('GIT_REPO_NAME')))
        git_url = os.path.expandvars(os.environ.get('GIT_REMOTE_URL'))
        git_user = os.path.expandvars(os.environ.get('GIT_USER'))
        git_repo_upstream = os.path.expandvars(os.environ.get('GIT_REMOTE_UPSTREAM'))
        git_branch = git_remote = os.path.expandvars(os.environ.get('GIT_BRANCH_NAME'))
        git_access_token = os.path.expandvars(os.environ.get('GITHUB_ACCESS_TOKEN'))

        # get the parent directory for git operations
        git_dir_parent = os.path.dirname(git_dir)

        # obtain filename and msg for commit
        data = json.loads(self.request.body.decode('utf-8'))
        filename = urllib.parse.unquote(data['filename'])
        msg = data['msg']
        commit_only_source = data['commit_only_source']


        # get current directory (to return later)
        cwd = os.getcwd()

        # select branch within repo
        try:
            os.chdir(git_dir)
            dir_repo = check_output(['git','rev-parse','--show-toplevel']).strip()
            repo = Repo(dir_repo.decode('utf8'))
        except GitCommandError as e:
            self.error_and_return(cwd, "Could not checkout repo: {}".format(dir_repo))
            return

        # create new branch
        try:
            print(repo.git.checkout('HEAD', b=git_branch))
        except GitCommandError:
            print("Switching to {}".format(repo.heads[git_branch].checkout()))

        # commit current notebook
        # client will sent pathname containing git directory; append to git directory's parent
        try:
            if commit_only_source :
                subprocess.run(['jupyter', 'nbconvert', '--to', 'script', str(os.environ.get('GIT_PARENT_DIR') + "/" + os.environ.get('GIT_REPO_NAME') + filename)])
                filename = str(os.environ.get('GIT_PARENT_DIR') + "/" + os.environ.get('GIT_REPO_NAME') + filename.replace('ipynb', 'py'))
            
            print(repo.git.add(str(os.environ.get('GIT_PARENT_DIR') + "/" + os.environ.get('GIT_REPO_NAME') + filename)))
            print(repo.git.commit( a=False, m="{}\n\nUpdated {}".format(msg, filename) ))

        except GitCommandError as e:
            print(e)
            self.error_and_return(cwd, "Could not commit changes to notebook: {}".format(git_dir_parent + filename))
            return

        # create or switch to remote
        try:
            remote = repo.create_remote(git_remote, git_url)
        except GitCommandError:
            print("Remote {} already exists...".format(git_remote))
            remote = repo.remote(git_remote)

        # push changes
        try:
            pushed = remote.push(git_branch)
            assert len(pushed)>0
            assert pushed[0].flags in [git.remote.PushInfo.UP_TO_DATE, git.remote.PushInfo.FAST_FORWARD, git.remote.PushInfo.NEW_HEAD, git.remote.PushInfo.NEW_TAG]
        except GitCommandError as e:
            print(e)
            self.error_and_return(cwd, "Could not push to remote {}".format(git_remote))
            return
        except AssertionError as e:
            self.error_and_return(cwd, "Could not push to remote {}: {}".format(git_remote, pushed[0].summary))
            return

        # open pull request
        try:
          github_url = "https://api.github.com/repos/{}/pulls".format(git_repo_upstream)
          github_pr = {
              "title":"{} Notebooks".format(git_user),
              "body":"IPython notebooks submitted by {}".format(git_user),
              "head":"{}:{}".format(git_user, git_remote),
              "base":"master"
          }
          github_headers = {"Authorization": "token {}".format(git_access_token)}
          r = requests.post(github_url, data=json.dumps(github_pr), headers=github_headers)
          if r.status_code != 201:
            print("Error submitting Pull Request to {}".format(git_repo_upstream))
        except:
            print("Error submitting Pull Request to {}".format(git_repo_upstream))

        # return to directory
        os.chdir(cwd)

        # close connection
        self.write({'status': 200, 'statusText': 'Success!  Changes to {} captured on branch {} at {}'.format(filename, git_branch, git_url)})


def setup_handlers(nbapp):
    route_pattern = ujoin(nbapp.settings['base_url'], '/git/commit')
    nbapp.add_handlers('.*', [(route_pattern, GitCommitHandler)])


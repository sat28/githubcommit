mkdir ~/githubcommit

#make a repo on github where you want to store notebooks and clone it
cd ~/githubcommit && git clone #name of repo && ssh-keygen -t rsa && ssh-keygen -y -f ~/.ssh/id_rsa > ~/.ssh/id_rsa.pub && ssh-add -K

export GIT_PARENT_DIR=~/githubcommit
export GIT_REPO_NAME=#your-repo-name
export GIT_BRANCH_NAME=#your-repo-branch
export GIT_USER=#your-github-user
export GIT_EMAIL=#your-github-email
export GITHUB_ACCESS_TOKEN=#find in setting personal access token
export GIT_USER_UPSTREAM=#your-github-user


############################################################################
#### DO NOT EDIT BELOW THIS LINE: derived variables
############################################################################
export GIT_REMOTE_URL=git@github.com:$GIT_USER/$GIT_REPO_NAME.git
export GIT_REMOTE_URL_HTTPS=https://github.com/$GIT_USER/$GIT_REPO_NAME.git
export GIT_REMOTE_UPSTREAM=$GIT_USER_UPSTREAM/$GIT_REPO_NAME

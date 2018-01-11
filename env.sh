####################### SSH KEY FOR GIT ###################################
ssh-keygen -t rsa && ssh-keygen -y -f ~/.ssh/id_rsa > ~/.ssh/id_rsa.pub && ssh-add -k
####################### To be added to git account settings ################


###################### GIT PARAMETERS #####################################
export GIT_PARENT_DIR=~
export GIT_REPO_NAME=gitjuphub
export GIT_BRANCH_NAME=master
export GIT_USER=sat28
export GIT_EMAIL=anand.shaleen@gmail.com
export GITHUB_ACCESS_TOKEN=b3a18d4fdca638cf347fa7b4833e22f808c12936
export GIT_USER_UPSTREAM=sat28


############################################################################
#### DO NOT EDIT BELOW THIS LINE: derived variables
############################################################################

export GIT_REMOTE_URL=git@github.com:$GIT_USER/$GIT_REPO_NAME.git
export GIT_REMOTE_URL_HTTPS=https://github.com/$GIT_USER/$GIT_REPO_NAME.git
export GIT_REMOTE_UPSTREAM=$GIT_USER_UPSTREAM/$GIT_REPO_NAME


####################### Git Repo where notebooks will be pushed ############
cd ~ && git clone $GIT_REMOTE_URL_HTTPS



####################### Change in jupyter config ###########################
if [ ! -f ~/.jupyter/jupyter_notebook_config.py ]; then
   jupyter notebook --generate-config
fi

echo 'c.NotebookApp.disable_check_xsrf = True' >> ~/.jupyter/jupyter_notebook_config.py
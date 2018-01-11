# githubcommit

githubcommit is a jupyter notebook extension enabling users push ipython notebooks to a git repo.
The git button gets displayed in the notebook toolbar. After saving any notebook
the user can push notebook to pre-specified git repository. There are few
environment variables that must be exported. Currently this extension supports
commits to a single github repo defined in environment variable but in the long
run need help to modify this extension allowing user to select his repo and branch.

## Installation

You can currently install this directly from git:

```
pip install git+https://github.com/sat28/githubcommit.git
jupyter serverextension enable --py githubcommit
jupyter nbextension install --py githubcommit
```

To enable this extension for all notebooks:

```
jupyter nbextension enable --py githubcommit
```

## Steps

* Install package using
* Create Git repo where notebooks will be pushed if not already exists
* Clone your repo in home directory
* Run the command - source env.sh
* Configure ssh key (present in ~/.ssh/id_rsa.pub or specified location) in github account
* Run jupyter notebook from within your repo directory


## Credits

Thanks to https://github.com/Lab41/sunny-side-up for laying the foundation of this extension.

Thanks to https://github.com/justvarshney for support.


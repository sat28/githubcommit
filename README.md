# githubcommit

githubcommit is a jupyter notebook extension enabling users push ipython notebooks to a git repo.
The git button gets displayed in the notebook toolbar. After saving any notebook
the user can push notebook to pre-specified git repository. There should be few
environment variables that must be exported. Currently this extension supports
commits to a single github repo defined in environment variable but in the long
run need help to modify this extension allowing user to select his repo and branch.

Please modify and run the env.sh beforehand.

Lastly add the ssh key to your github account for facilitating access. Go to setting of
github account and go to ssh keys and there add your key (vi ~/.ssh.id_rsa.pub)

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

## Credits

Thanks to https://github.com/Lab41/sunny-side-up for laying the foundation of this extension.

Thanks to https://github.com/justvarshney for support.


# OctoPrintPlugins

## Reference

- <https://docs.octoprint.org/en/master/development/environment.html>

## Setup

- `mkdir OctoPrintPlugins`
- `cd OctoPrintPlugins`
- grab source `git clone https://github.com/atiniir/OctoPrintPlugins.git`
- Open vscode
- Start powershell terminal session
- checking if running in virtual env
  - `python -v` == Python 3.11.3
  - created `test-venv.py` to check virtual env is active or not (it's not)
- pwsh vscode terminal
  - `python -m virtualenv venv`
  - `.\venv\Scripts\activate.ps1`
  - should see (venv) in the prompt
- now with venv confirmed working
  - `pip install --upgrade pip`
  - `pip install -U black flake8 flake8-bugbear`
  - `pip install "cookiecutter>=1.4,<1.7"`
  - `pip install -e './Octoprint[develop,plugins,docs]'`
- Can now run with F5 and do debug and breakpoints!
- Enable plugins for each plugin directory
  - `python setup.py develop`

### Not working

- attempting to use env for plugin dev
  - `octoprint dev plugin:new helloworld`
    - ERRORS with `re.error: global flags not at the start of the expression at position 1 (line 2, column 1)`

## Submodules

There are submodules setup for OctoPrint and several plugins

There is a submodule with plugin code at myplugins\OctoPrint-Queue which links to the repo <https://github.com/atiniir/OctoPrint-Queue>

### Create Submodule

```powershell
cd .\plugins
git submodule add https://github.com/atiniir/OctoPrint-Queue.git
git status
git add .
git commit -m "Add submodule"
```

### Remove Submodule

```powershell
# base of workspace
cd .\ 
# Remove the submodule entry from .git/config
git submodule deinit -f .\myplugins\OctoPrint-Queue
# Remove the submodule directory from the superproject's .git/modules directory
rm .git\modules\myplugins\OctoPrint-Queue -r -fo
# Remove the entry in .gitmodules and remove the submodule directory
rm -f .\myplugins\OctoPrint-Queue
```


## test-venv.py

```python
import sys

def is_venv():
    return (hasattr(sys, 'real_prefix') or
            (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix))

if is_venv():
    print('inside virtualenv or venv')
else:
    print('outside virtualenv or venv')
```

# Unknown Type Placeholder bug

This is a simple example repository to demonstrate the `WARNING: Unknown type: placeholder` bug that is thrown in
AutoAPI when using it within a ROS package (see https://github.com/readthedocs/sphinx-autoapi/issues/180).

## Steps to Reproduce

1.  Checkout the `bug` branch.
2.  Install Python 3.8 (https://docs.python.org/3/).
3.  Install the venv python package (i.e. `sudo apt install python3-venv`).
4.  Create a new virtual environment using the `--system-site-packages` flag (i.e. `python3 -m venv test_pkg --system-site-packages`).
5.  Install the python dependencies (i.e. `pip install -r requirements/doc_requirements.txt`).
6.  Build the documentation from within the `docs` folder (i.e. `make html`).
7.  Be greeted by the `WARNING: Unknown type: placeholder` bug.

## How to debug autoapi to find the bug

1.  Change the `"program": "~/venvs/placeholder_bug/bin/sphinx-build",` in the `.vscode/launch.json` file to point to your virtual environment's `sphinx-build` executable.
2.  Put a breakpoint in the `lib/python3.9/site-packages/autoapi/mappers/python/mapper.py` file at line `333` (i.e. `children = {child["name"]: child for child in module["children"]}`).
3.  Run the vscode debugger (i.e. `F5`).
4.  See that the code overwrites the dictionary entry for a given module, here `test_pkg`, when a module is encountered for the second time.

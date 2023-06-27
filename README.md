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

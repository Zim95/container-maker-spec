# container-maker-spec
[![License: AGPL v3](https://img.shields.io/badge/License-AGPL_v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)

Protobuf API spec for container-maker

# How to Install locally:
- Clone the repository:
    ```bash
    $ git clone https://github.com/Zim95/container-maker-spec
    ```
    This will create a directory called `container-maker-spec` and clone the files within that directory.

    If you want a custom directory name:
    ```bash
    $ git clone https://github.com/Zim95/container-maker-spec <target-directory>
    ```

- Navigate to the target directory (container-maker-spec by default) and hit:
    ```bash
    $ poetry install
    ```
    This will run `build.py` and generate the protobuf files and also install it automatically in your virtual environment.


# How to make it installable from git:
- When installing from `git`, the `build.py` file is not run.

- In this case we need to run it manually and generate the protobuf files.

- First, create the virtual environment. So that it installs all required dependencies.
    ```bash
    $ poetry shell
    ```
    This creates the virtual environment. Now install the required dependencies.
    ```bash
    $ poetry install --no-root
    ```

- Now hit build.py
    ```bash
    $ python build.py
    ```
    This will generate the files.

- Next, commit these changes to git.

- If someone downloads them from git, then these protobuf files will also be copied to site-packages.

- You can now, add this package to poetry using:
    ```bash
    $ poetry add git+https://github.com/Zim95/container-maker-spec.git@<tag>
    ```

# How to update tag:
- Update the version in `pyproject.toml`:

- Next, create the git tag:
    ```bash
    $ git tag <tagname> && git push -f origin <tagname>
    ```

- Overwrite the old tag:
    ```bash
    $ git tag -d <tagname> && git tag <tagname> && git push -f origin <tagname>
    ```

# `cookiecutter-gopy`

## Description

A [cookiecutter] to help generate a [`gopy`](https://github.com/go-python/gopy) project.

[cookiecutter]: https://cookiecutter.readthedocs.io/en/stable/index.html

## Usage


Step 1, install cookiecutter itself.

```bash
# Option A: using pipx ( https://github.com/pypa/pipx )
pipx install cookiecutter

# Option B: using uv ( https://docs.astral.sh/uv/concepts/tools/ )
uv tool install cookiecutter
```

Step 2, bootstrap your new gopy project using cookiecutter

```bash
# Using the main branch
cookiecutter https://github.com/b-long/cookiecutter-gopy.git

# Use a specific branch
cookiecutter https://github.com/b-long/cookiecutter-gopy.git --checkout develop
```

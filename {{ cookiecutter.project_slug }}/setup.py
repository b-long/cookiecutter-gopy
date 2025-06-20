import setuptools


from pathlib import Path

"""
NOTE: This project uses more than one version of a 'setup.py' file:
* 'setup.py', and
* 'setup_ci.py'

Based on:
    https://github.com/popatam/gopy_build_wheel_example/blob/main/setup_ci.py
"""

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()
PACKAGE_PATH = "g{{ cookiecutter.project_slug }}"
PACKAGE_NAME = "{{ cookiecutter.project_slug }}"

setuptools.setup(
    name=PACKAGE_NAME,
    packages=setuptools.find_packages(include=[PACKAGE_NAME]),
    py_modules=[f"{PACKAGE_NAME}.{PACKAGE_PATH}"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    package_data={PACKAGE_NAME: ["*.so"]},
    # Should match 'pyproject.toml' version number
    version="{{ cookiecutter.version }}",
    author_email="{{ cookiecutter.author_email }}",
    include_package_data=True,
)

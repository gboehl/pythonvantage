from setuptools import setup, find_packages
from os import path

# get version from dedicated version file
version = {}
with open("alpyvantage/__version__.py") as fp:
    exec(fp.read(), version)

# read the contents of the README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.rst"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/gboehl/alpyvantage",
    name='econpizza',
    version=version['__version__'],
    author="Gregor Boehl",
    author_email="admin@gregorboehl.com",
    description="A python API to Alpha Vantage",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    include_package_data=True,
    packages=['alpyvantage'],
    install_requires=[
        "pandas"
    ],
)

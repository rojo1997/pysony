from setuptools import setup
from setuptools import find_packages

setup(
    name = "pysony",
    version = "1.0",
    description = "Main Python package of the sony interview project",
    author = "Ernesto Martínez del Pino",
    author_email = "ernestomar1997@hotmail.com",
    packages = find_packages(),
    install_requires = [i.strip() for i in open("requirements.txt", mode = "r").readlines()],
    test_suite = "tests",
    python_requires = ">=3.9"
)
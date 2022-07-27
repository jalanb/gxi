"""Set up the gxi project"""

from setuptools import find_packages
from setuptools import setup


setup(
    packages=find_packages(),
    install_requires=[
        "deprecated>=1.2.10,<2.0",
        "lazy>=1.4,<2.0",
        "textual>=0.1.18",
        "stackprinter>=0.2.6",
    ],
    tests_require=[
        "coverage<5",
        "pytest",
        "pytest-cov",
        "tox",
    ],
)

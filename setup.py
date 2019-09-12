# -*- coding: utf-8 -*-
"""
    setup
    ~~~~~
    Tests helper functions
    :copyright: 2019 Chris Zimmerman
    :license: BSD-3-Clause
"""
import io
import re

from setuptools import find_packages
from setuptools import setup

with io.open("README.rst", "rt", encoding="utf8") as f:
    readme = f.read()

with io.open("fastapi_router/__init__.py", "rt", encoding="utf8") as f:
    version = re.search(r'__version__ = "(.*?)"', f.read()).group(1)

setup(
    name="fastapi_router",
    version=version,
    url="https://github.com/christopherzimmerman/fastapi_router",
    project_urls={
        "Code": "https://github.com/christopherzimmerman/fastapi_router",
        "Issue tracker": "https://github.com/christopherzimmerman/fastapi_router/issues",
    },
    license="BSD-3 Clause",
    author="Chris Zimmerman",
    author_email="chris@chriszimmerman.me",
    maintainer="Chris Zimmerman",
    maintainer_email="chris@chriszimmerman.me",
    description="Directory structure routing for fastapi",
    long_description=readme,
    classifiers=[
        "Development Status :: 1 - Planning",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=["trimport"],
    python_requires=">=3.5",
    extras_require={
        "dev": ["pytest", "coverage", "sphinx"],
        "docs": ["sphinx", "numpydoc"],
    },
)
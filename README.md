# Data Samples and Data Handling Routines for Pylogeny Packages

[![codecov](https://codecov.io/gh/pylogeny/data/branch/master/graph/badge.svg)](https://codecov.io/gh/pylogeny/data)
[![PyPI](https://img.shields.io/pypi/v/pylodata.svg)](https://pypi.org/project/pylodata)

This package allows for quick access to data in various forms which we need to develop methods for phylogenetic reconstruction in linguistics and beyond. 

## Installation

To install the package, type:
```
$ pip install pylodata
```
To use the package, you may also want to install LingPy:

```
$ pip install lingpy 
```

## Usage

```
>>> from pylodata import data_path, patterns, wordlist
>>> from lingpy import Wordlist
>>> patterns, characters = wordlist.get_multistate_patterns(Wordlist(data_path("wichmannmixezoquean.tsv")))
```


# pdfshrink

[![Travis](https://travis-ci.org/tdegeus/pdfshrink.svg?branch=master)](https://travis-ci.org/tdegeus/pdfshrink)
[![Build status](https://ci.appveyor.com/api/projects/status/nrs0mxqn5bnsyi03?svg=true)](https://ci.appveyor.com/project/tdegeus/pdfshrink)
[![Conda Version](https://img.shields.io/conda/vn/conda-forge/pdfshrink.svg)](https://anaconda.org/conda-forge/pdfshrink)


Simple command-line script that allows you to remove the size of PDF-files.

```none
pdfshrink <files>...
```

Note that the script is in fact a simple Python script that wraps GhostScript. 

# Contents

<!-- MarkdownTOC -->

- [Disclaimer](#disclaimer)
- [Getting pdfshrink](#getting-pdfshrink)
  - [Using conda](#using-conda)
  - [Using PyPi](#using-pypi)
  - [From source](#from-source)
- [Usage](#usage)

<!-- /MarkdownTOC -->

# Disclaimer

This library is free to use under the [MIT license](https://github.com/tdegeus/pdfshrink/blob/master/LICENSE). Any additions are very much appreciated, in terms of suggested functionality, code, documentation, testimonials, word-of-mouth advertisement, etc. Bug reports or feature requests can be filed on [GitHub](https://github.com/tdegeus/pdfshrink). As always, the code comes with no guarantee. None of the developers can be held responsible for possible mistakes.

Download: [.zip file](https://github.com/tdegeus/pdfshrink/zipball/master) | [.tar.gz file](https://github.com/tdegeus/pdfshrink/tarball/master).

(c - [MIT](https://github.com/tdegeus/pdfshrink/blob/master/LICENSE)) T.W.J. de Geus (Tom) | tom@geus.me | www.geus.me | [github.com/tdegeus/pdfshrink](https://github.com/tdegeus/pdfshrink)

# Getting pdfshrink

## Using conda

```bash
conda install -c conda-forge pdfshrink
```

This will also install all necessary dependencies.

## Using PyPi

```bash
pip install pdfshrink
```

This will also install the necessary Python modules, **but not GhostScript**.

## From source

```bash
# Download pdfshrink
git checkout https://github.com/tdegeus/pdfshrink.git
cd pdfshrink

# Install
python -m pip install .
```

This will also install the necessary Python modules, **but not GhostScript**.

# Usage

The usage is as follows (see `pdfshrink --help`):

```bash
pdfshrink
  Shrink a PDFs file size using GhostScript.

Usage:
  pdfshrink [options] <files>...

Options:
  -o, --output=<N>  Specify output file. (default: overwrite the input file(s))
  -s, --silent      Do not print any progress.
      --verbose     Verbose all commands.
  -h, --help        Show help.
      --version     Show version.

(c - MIT) T.W.J. de Geus | tom@geus.me | www.geus.me
```

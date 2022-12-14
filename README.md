# SPIIR Data Package

This repository contains gravitational wave data generation and processing algorithms
used by hte SPIIR low latency CBC search pipeline.

## Installation

Installation with these commands requires an existing installation of Python >= 3.8.

```
# you can change the last "venv" to any name you like
python -m venv venv
source venv/bin/activate
```

Next we need to change directories to where this repository is installed. For example:

```
# download spiir repository and change working directory
git clone https://github.com/tanghyd/spiir-data.git
cd spiir-search

# then we can install our local "spiir-data" package
# this will also install required dependencies
pip install .  # optionally add the -e flag for --editable mode
```

## Usage

Now we can import our package from the `spiir.data` namespace in Python as follows:

```
import spiir.data
```

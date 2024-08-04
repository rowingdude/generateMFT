# MFT Test Generator

A Python tool for generating test Master File Table (MFT) files with configurable record counts and error rates.

## Features

- Generate MFT files with customizable number of records
- Introduce random errors at a specified rate
- Modular design for easy extension and maintenance

## Requirements

- Python 3.6+

## Quick Start

1. Clone the repository:

`git clone https://github.com/rowingdude/mft-test-generator.git`
`cd mft-test-generator`


2. Run the mft_generator script:

`python mft_generator.py`

3. Follow the prompts to generate your MFT test file.

## Usage

For basic usage, run `mft_generator.py` and follow the interactive prompts.

For programmatic use, import the generator in your Python script:

``` 
from mft_file_generator import generate_mft_file

generate_mft_file("test.bin", 100, 0.1)  # 100 records, 10% error rate

```
# MFT Test Generator Usage Guide

The MFT Test Generator is a tool designed to create random Master File Table (MFT) files for testing purposes. It can generate a specified number of MFT records with an optional error rate to simulate corrupted or invalid records.

## Prerequisites

- Python 3.6 or higher

## File Structure

- `mft_structures.py`: Defines the basic structures for MFT headers and attributes.
- `mft_record_generator.py`: Contains the logic for generating individual MFT records.
- `mft_file_generator.py`: Handles the creation of complete MFT files.
- `main.py`: Provides an interactive interface for generating MFT files.

## Command-Line Options

The MFT Test Generator now supports the following command-line options:

- `-d, --debug`: Enable debug output. This will print detailed information about each record and attribute being generated.
- `-o FILENAME, --output FILENAME`: Specify the output filename. Default is "test_mft.bin".
- `-n NUM_RECORDS, --num-records NUM_RECORDS`: Specify the number of records to generate. Default is 1000.
- `-e ERROR_RATE, --error-rate ERROR_RATE`: Specify the error rate (0.0 to 1.0). Default is 0.05 (5%).


## Basic Usage

1. Ensure all the Python files are in the same directory.

2. Run the `main.py` script:

`python main.py`

3. Follow the prompts to specify:

- The output filename
- The number of records to generate
- The error rate (a float between 0.0 and 1.0)

4. The script will generate the MFT file and confirm its creation.

## Advanced Usage

You can also import the `generate_mft_file` function in your own Python scripts for more programmatic control:

`from mft_file_generator import generate_mft_file`

## Generate an MFT file with 1000 records and a 5% error rate
`generate_mft_file("custom_test.bin", 1000, 0.05)`

# Parameters

- filename: The name of the output MFT file.
- num_records: The number of MFT records to generate.
- error_rate: The probability (0.0 to 1.0) of introducing an error in each record.

## Error Types
The generator can introduce three types of errors:

## Corrupt magic number in the header
- Invalid record size
- Corrupt attribute header

These errors are randomly distributed based on the specified error rate.

## Customization
To modify the types of records or errors generated, you can edit the following files:

- mft_structures.py: Modify MFTAttribute to change attribute content generation.
- mft_record_generator.py: Adjust introduce_error method to change error types.

## Output

The generated file is a binary file mimicking the structure of an MFT. Each record is 1024 bytes long, consistent with standard MFT record sizes.

## Note
This tool is for testing purposes only and should not be used with or on real MFT files or live systems.
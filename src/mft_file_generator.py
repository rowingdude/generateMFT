import random
from mft_record_generator import MFTRecordGenerator

def generate_mft_file(filename, num_records, error_rate=0.1, debug=False):
    """Generate an MFT file with the specified number of records."""
    generator = MFTRecordGenerator(debug)
    with open(filename, 'wb') as f:
        for _ in range(num_records):
            introduce_error = random.random() < error_rate
            record = generator.generate_record(introduce_error)
            f.write(record)

if __name__ == "__main__":
    generate_mft_file("test_mft.bin", 100, 0.1)
    print("Generated test_mft.bin with 100 records and 10% error rate.")
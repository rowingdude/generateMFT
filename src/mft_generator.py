from mft_file_generator import generate_mft_file
import argparse

def main():
    parser = argparse.ArgumentParser(description="Generate a test MFT file.")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug output")
    parser.add_argument("-o", "--output", default="test_mft.bin", help="Output filename (default: test_mft.bin)")
    parser.add_argument("-n", "--num-records", type=int, default=1000, help="Number of records to generate (default: 1000)")
    parser.add_argument("-e", "--error-rate", type=float, default=0.05, help="Error rate (0.0 to 1.0, default: 0.05)")
    args = parser.parse_args()

    generate_mft_file(args.output, args.num_records, args.error_rate, args.debug)
    print(f"Generated {args.output} with {args.num_records} records and {args.error_rate:.1%} error rate.")

if __name__ == "__main__":
    main()
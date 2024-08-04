from mft_file_generator import generate_mft_file

def main():
    filename = input("Enter the output filename: ")
    num_records = int(input("Enter the number of records to generate: "))
    error_rate = float(input("Enter the error rate (0.0 to 1.0): "))

    generate_mft_file(filename, num_records, error_rate)
    print(f"Generated {filename} with {num_records} records and {error_rate:.1%} error rate.")

if __name__ == "__main__":
    main()
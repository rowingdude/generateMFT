import random
import struct
from mft_structures import MFTHeader, MFTAttribute

class MFTRecordGenerator:
    def __init__(self, debug=False):
        self.record_size = 1024
        self.attribute_types = [0x10, 0x20, 0x30, 0x40, 0x50, 0x60, 0x70, 0x80, 0x90, 0xA0, 0xB0, 0xC0, 0xD0, 0xE0, 0xF0, 0x100]
        self.debug = debug

    def generate_record(self, introduce_error=False):
        """Generate a complete MFT record."""
        try:
            header = MFTHeader()
            record = bytearray(header.pack(self.debug))
            if self.debug:
                print(f"Header size: {len(record)}")

            # Add attributes
            for _ in range(random.randint(1, 5)):
                attr_type = random.choice(self.attribute_types)
                try:
                    attribute = MFTAttribute(attr_type).pack(self.debug)
                    if self.debug:
                        print(f"Attribute type: {attr_type:x}, size: {len(attribute)}")
                    if len(record) + len(attribute) <= self.record_size - 8:
                        record.extend(attribute)
                except Exception as e:
                    if self.debug:
                        print(f"Error generating attribute type {attr_type:x}: {e}")

            # Add end marker
            record.extend(struct.pack('<I', 0xFFFFFFFF))

            # Pad to full record size
            record.extend(b'\x00' * (self.record_size - len(record)))

            if introduce_error:
                self.introduce_error(record)

            return record
        except Exception as e:
            if self.debug:
                print(f"Error in generate_record: {e}")
            raise

    def introduce_error(self, record):
        """Introduce a random error into the record."""
        error_type = random.choice(['corrupt_magic', 'invalid_size', 'corrupt_attribute'])
        if error_type == 'corrupt_magic':
            record[0:4] = b'\x00\x00\x00\x00'
        elif error_type == 'invalid_size':
            struct.pack_into('<I', record, 24, 2048)  # Set an invalid record size
        elif error_type == 'corrupt_attribute':
            # Corrupt a random attribute header
            attr_start = random.randint(64, len(record) - 24)
            record[attr_start:attr_start+4] = b'\xFF\xFF\x00\x00'
import struct
from datetime import datetime, timedelta
import random

def generate_random_time():
    """Generate a random Windows timestamp."""
    now = datetime.now()
    delta = timedelta(days=random.randint(0, 365 * 10))  # Up to 10 years in the past
    random_time = now - delta
    windows_ticks = int((random_time - datetime(1601, 1, 1)).total_seconds() * 10000000)
    return windows_ticks

class MFTHeader:
    def __init__(self):
        self.magic = 0x454C4946  # FILE
        self.update_sequence_offset = random.randint(42, 48)
        self.update_sequence_count = random.randint(1, 4)
        self.logfile_sequence_number = random.randint(0, 1000000)
        self.sequence_number = random.randint(1, 1000)
        self.hard_link_count = random.randint(1, 5)
        self.attribute_offset = random.randint(56, 96)
        self.flags = random.choice([0x0001, 0x0002, 0x0004, 0x0008])
        self.used_size = random.randint(512, 1024)
        self.allocated_size = 1024
        self.file_reference = random.randint(0, 1000000)
        self.next_attribute_id = random.randint(1, 100)
        self.record_number = random.randint(0, 1000000)

    def pack(self):
        return struct.pack('<IHHQHHHHIIQHHI', 
                           self.magic, self.update_sequence_offset, self.update_sequence_count,
                           self.logfile_sequence_number, self.sequence_number, self.hard_link_count,
                           self.attribute_offset, self.flags, self.used_size, self.allocated_size,
                           self.file_reference, self.next_attribute_id, self.record_number)

class MFTAttribute:
    def __init__(self, attr_type):
        self.type = attr_type
        self.length = 0
        self.non_resident_flag = 0
        self.name_length = 0
        self.name_offset = 0
        self.flags = 0
        self.attribute_id = random.randint(0, 0xFFFF)
        self.content = self.generate_content()

    def generate_content(self):
        if self.type == 0x10:  # Standard Information
            return struct.pack('<QQQQQIIIIIQQQ',
                               generate_random_time(),
                               generate_random_time(),
                               generate_random_time(),
                               generate_random_time(),
                               random.randint(0, 0xFFFFFFFF),
                               random.randint(0, 0xFFFFFFFF),
                               random.randint(0, 0xFFFFFFFF),
                               random.randint(0, 0xFFFFFFFF),
                               random.randint(0, 0xFFFFFFFF),
                               random.randint(0, 0xFFFFFFFF),
                               random.randint(0, 0xFFFFFFFFFFFFFFFF),
                               random.randint(0, 0xFFFFFFFFFFFFFFFF))
        elif self.type == 0x30:  # File Name
            name = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=random.randint(1, 20)))
            return struct.pack('<QQQQQQQQQBB',
                               random.randint(0, 0xFFFFFFFFFFFFFFFF),
                               generate_random_time(),
                               generate_random_time(),
                               generate_random_time(),
                               generate_random_time(),
                               random.randint(0, 0xFFFFFFFFFFFFFFFF),
                               random.randint(0, 0xFFFFFFFFFFFFFFFF),
                               random.randint(0, 0xFFFFFFFFFFFFFFFF),
                               len(name),
                               random.randint(0, 3)) + name.encode('utf-16le')
        else:
            return os.urandom(random.randint(16, 128))

    def pack(self):
        self.length = len(self.content) + 16
        header = struct.pack('<IIBBBHHH',
                             self.type,
                             self.length,
                             self.non_resident_flag,
                             self.name_length,
                             self.name_offset,
                             self.flags,
                             self.attribute_id)
        return header + self.content
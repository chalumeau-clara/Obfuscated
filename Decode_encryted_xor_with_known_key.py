import os
import struct
import sys

def byte_xor(content, key, len_byte_key):
    translated = ""
    len_content = len(content)
    index = 0
    while (index < len_content):
        data = content[index:index+len_byte_key]
        p = struct.unpack("I", data)[0]
        translated += struct.pack("I", p ^ key)
        index += len_byte_key
    return tranlated
        
in_file = open("file_name", "rb")
out_file = open("out_file_name", "wb")
xor_key = 0x00
len_byte_key = 1
rsrc_content = in_file.read()
decryted_content = byte_xor(rsrc_content, key, len_byte_key)
out_file.write(decryted_content)

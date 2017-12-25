#!/usr/bin/python
# coding: utf-8


class Op(object):
    WRITE_BLOCK = bytes.fromhex("50")
    READ_BLOCK = bytes.fromhex("51")
    READ_METADATA = bytes.fromhex("52")
    REPLACE_BLOCK = bytes.fromhex("53")
    COPY_BLOCK = bytes.fromhex("54")
    BLOCK_CHECKSUM = bytes.fromhex("55")
    TRANSFER_BLOCK = bytes.fromhex("56")

    FIRST_CODE = WRITE_BLOCK

    def __init__(self, code):
        self.code = code

    def read(self, data_input):
        return data_input.read()

    def write(self, data_output):
        data_output.write(self.code)





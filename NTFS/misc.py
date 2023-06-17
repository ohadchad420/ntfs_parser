import NTFS.globals as g

def from_bytes(bytes, byteorder="little", signed=True):
    if type(bytes) == int: # handle case when only 1 byte was sent
        return int.from_bytes([bytes], byteorder=byteorder, signed=signed)
    return int.from_bytes(bytes, byteorder=byteorder, signed=signed)

def lcn_to_byte_offset(lcn):
    return lcn * g.SECTORS_PER_CLUSTER * g.BYTES_PER_SECTOR
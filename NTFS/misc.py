from gc import freeze
import NTFS.globals as g

def from_bytes(bytes, byteorder="little", signed=True):
    if type(bytes) == int: # handle case when only 1 byte was sent
        return int.from_bytes([bytes], byteorder=byteorder, signed=signed)
    return int.from_bytes(bytes, byteorder=byteorder, signed=signed)

def lcn_to_byte_offset(lcn):
    return lcn * g.SECTORS_PER_CLUSTER * g.BYTES_PER_SECTOR
    
class Freeze():

    freeze = False

    def __init__(self):
        self.freeze = True
    
    def __setattr__(self, __name, __value):
        if self.freeze:
            raise AttributeError("This struct's attributes can't be modified")
        object.__setattr__(self, __name, __value)
           
    
    def __delattr__(self, __name):
        if self.freeze:
            raise AttributeError("This struct's attributes can't be modified")
        object.__delattr__(self, __name)
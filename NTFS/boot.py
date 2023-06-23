import NTFS.globals as g
from NTFS.misc import *

_boot_instance = None

class Boot(Freeze):

    def __init__(self, bootfile_raw=b""):
        global _boot_instance

        if _boot_instance != None:
            return None

        if len(bootfile_raw) != 512:
            raise ValueError("BOOT Sector (0) recieved is not 512 bytes long")
        
        if bootfile_raw[0x3:0x7] != b"NTFS":
            raise Exception(f"File system is not NTFS!")
        
        self.bytes_per_sector = from_bytes(bootfile_raw[0xB:0xD])
        g.BYTES_PER_SECTOR = self.bytes_per_sector
        self.sectors_per_cluster = from_bytes(bootfile_raw[0xD])
        g.SECTORS_PER_CLUSTER = self.sectors_per_cluster

        self.sectors_in_disk = from_bytes(bootfile_raw[0x28:0x30])

        self.mft_cluster_offset = from_bytes(bootfile_raw[0x30:0x38])

        # actually is from 0x40:0x44, however saved in disk as if it is only one byte long
        # so negative values wont have 0xFF in their more significant bytes
        self.mft_clusters_per_entry = from_bytes(bootfile_raw[0x40]) 

        _boot_instance = self

        super().__init__()
    
    def get(bootfile_raw=b""):
        global _boot_instance

        if _boot_instance == None:
            Boot(bootfile_raw)
        return _boot_instance
    
    @property
    def mft_bytes_per_entry(self):
        return 2 ** (-1 * self.mft_clusters_per_entry)

    @property
    def mft_byte_offset(self):
        return lcn_to_byte_offset(self.mft_cluster_offset)
    
    @property
    def bytes_per_cluster(self):
        return g.SECTORS_PER_CLUSTER * g.BYTES_PER_SECTOR

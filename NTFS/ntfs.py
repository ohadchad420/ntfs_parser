import NTFS.globals as g
from NTFS.boot import Boot

class NTFSManager():

    def __init__(self, disk_drive):
        self.drive_file = open(disk_drive, 'rb')
        self.drive_file.seek(0)
        boot_sector_raw = self.drive_file.read(g.BOOT_SECTOR_SIZE)

        self._boot = Boot(boot_sector_raw)

    def exit(self):
        if self.drive_file is not None:
            self.drive_file.close()
        self.drive_file = None
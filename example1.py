from NTFS.all import *

HARD_DRIVE = "\\\\?\\C:"

def main():
    print(HARD_DRIVE)
    ntfs_instance = NTFSManager(HARD_DRIVE)
    print(ntfs_instance._boot.mft_byte_offset)


if __name__ == "__main__":
    main()
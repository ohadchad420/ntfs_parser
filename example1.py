from NTFS.all import *

HARD_DRIVE = "\\\\?\\C:"

def main():
    print(HARD_DRIVE)
    ntfs_instance = NTFSManager(HARD_DRIVE)


if __name__ == "__main__":
    main()
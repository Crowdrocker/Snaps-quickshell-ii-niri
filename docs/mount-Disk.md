sudo mkdir -p /run/media/wehttamsnaps/LINUXDRIVE-1
sudo mkdir -p /run/media/wehttamsnaps/PC-EXTRA-2
sudo mkdir -p /run/media/wehttamsnaps/GAMEDRIVE
sudo mkdir -p /run/media/wehttamsnaps/Wettam-Snaps-Main

sudo mount /dev/sdb1 /run/media/wehttamsnaps/LINUXDRIVE-1
sudo mount -t ntfs-3g /dev/sdd1 /run/media/wehttamsnaps/PC-EXTRA-2
sudo mount -t ntfs-3g /dev/sdi1 /run/media/wehttamsnaps/GAMEDRIVE
sudo mount -t ntfs-3g /dev/sdj1 /run/media/wehttamsnaps/Wettam-Snaps-Main


sudo unmount /dev/sdb1 /run/media/wehttamsnaps/LINUXDRIVE-1
sudo udiskie-umount /dev/sdd1 /run/media/wehttamsnaps/PC-EXTRA-2
sudo udiskie-umount /dev/sde1 /run/media/wehttamsnaps/GAMEDRIVE
sudo udiskie-umount /dev/sdj1 /run/media/wehttamsnaps/Wettam-Snaps-Main

echo "========================================"
echo "Arch Linux Disk Mounting Cheat Sheet"
echo "========================================"

echo -e "\n📋 QUICK MOUNT COMMANDS:"
echo "# Mount drive: udisksctl mount -b /dev/sdXY"
echo "# Unmount: udisksctl unmount -b /dev/sdXY"
echo "# List drives: lsblk -f"

echo -e "\n🎯 YOUR DRIVES CHEAT SHEET:"
echo "PC-EXTRA-2:      udisksctl mount -b /dev/sdd1"
echo "Wettam Snaps Main: udisksctl mount -b /dev/sde1"
echo "GAMEDRIVE:       udisksctl mount -b /dev/sdj1"
echo "LINUXDRIVE-1:    udisksctl mount -b /dev/sdb1"

echo -e "\n🔍 CHECK DRIVE STATUS:"
echo "# See all drives: lsblk -f"
echo "# See mounted drives: df -h | grep -E '(/dev/sd|/mnt/)'"
echo "# Check drive health: sudo smartctl -a /dev/sdX"

echo -e "\n📁 AUTO-MOUNT AT BOOT (fstab):"
echo "# Edit fstab: sudo nano /etc/fstab"
echo "# Example entry:"
echo "/dev/sdd1 /mnt/PC-EXTRA-2 ntfs-3g defaults,uid=1000,gid=1000,umask=002 0 0"
echo ""
echo "# Apply changes:"
echo "sudo systemctl daemon-reload"
echo "sudo mount -a"

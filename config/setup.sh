sudo cp cmdline.txt /boot/cmdline.txt
sudo cp raspi-blacklist.conf /etc/modprobe.d/raspi-blacklist.conf
sudo cp modules /etc/modules

sudo chown root:root /boot/cmdline.txt
sudo chown root:root /etc/modprobe.d/raspi-blacklist.conf
sudo chown root:root /etc/modules

sudo chmod 755 /boot/cmdline.txt
sudo chmod 644 /etc/modprobe.d/raspi-blacklist.conf
sudo chmod 644 /etc/modules

sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install wicd-curses

sudo REPO_URI=https://github.com/notro/rpi-firmware rpi-update
sudo reboot

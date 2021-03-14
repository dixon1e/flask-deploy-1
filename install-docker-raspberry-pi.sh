# as sudo -i
if [ "$EUID" -ne 0 ]
    then echo "Must be root"
    exit
fi

# Get the latest, not from repository
curl -sSL https://get.docker.com | sudo -E sh
# Run without sudo, N.B. must exit this shell
sudo usermod -aG docker pi
# Dependencies for docker-compose
sudo apt-get install -y libffi-dev libssl-dev
sudo apt-get install -y python3 python3-pip
sudo apt-get remove  -y python-configparser
# Install docker-compose
sudo pip3 -v install docker-compose
# Restart to be sure all is taken in
sudo reboot

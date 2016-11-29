set -e
set -x

echo "Provisioning starts!"

#sudo -s
sudo apt-get update
sudo apt-get install python3-pip python3-dev nginx imagemagick libmagickwand-dev lynx
sudo pip3 install virtualenv
sudo pip install  --upgrade pip
pip3 install requests
pip install Wand
sudo pip3 install -r requirements.txt

#Config Gunicorn:
sudo cp ./imageapi.service /etc/systemd/system/ 
sudo systemctl start imageapi.service
sudo systemctl enable imageapi.service

echo "Provisioning complete!"

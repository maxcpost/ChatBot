#!/bin/bash

# Update and upgrade the system
sudo apt update && sudo apt upgrade -y

# Install Python and necessary packages
sudo apt install python3 python3-pip python3-venv git nginx supervisor -y

# Clone the repository
git clone https://github.com/yourusername/business-chatbot.git
cd business-chatbot

# Set up the virtual environment and install dependencies
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Copy environment variables
cp .env.example .env

# Configure Nginx
sudo cp config/nginx/moly.agoratree.xyz /etc/nginx/sites-available/
sudo ln -s /etc/nginx/sites-available/moly.agoratree.xyz /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx

# Configure Supervisor
sudo cp config/supervisor/moly.conf /etc/supervisor/conf.d/
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl start moly

# Obtain and install SSL certificate
sudo apt install certbot python3-certbot-nginx -y
sudo certbot --nginx -d moly.agoratree.xyz

echo "Deployment complete."
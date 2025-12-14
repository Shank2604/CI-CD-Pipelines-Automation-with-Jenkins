#!/bin/bash

APP_DIR="/opt/devops-app"

echo "Starting deployment..."

if [ ! -d "$APP_DIR" ]; then
  sudo mkdir -p $APP_DIR
fi

sudo cp -r * $APP_DIR
cd $APP_DIR

pip3 install -r requirements.txt

sudo pkill -f app.py || true
nohup python3 app/app.py > output.log 2>&1 &

echo "Deployment completed!"

#!/bin/sh

sed -i 's/\r//' script.sh
chmod +x install.sh
chmod +x ../main.py
chmod 775 ../exploit/
chmod 775 ../payload/
chmod +x ../run.sh
chmod +x ../script.sh
chmod +x ../__init__.py
clear
bash script.sh

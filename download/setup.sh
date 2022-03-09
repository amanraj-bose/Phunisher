#!/bin/sh

sed -i 's/\r//' script.sh
chmod +x script.sh
dos2unix ../main.py
chmod +x ../main.py
chmod 775 ../exploit/
chmod 775 ../payload/
chmod +x ../run.sh
chmod +x ../script.sh
dos2unix ../__init__.py
dos2unix install.py
dos2unix gui_installation.py
chmod +x ../__init__.py
sed -i 's/\r//' ../run.sh
sed -i 's/\r//' script.sh
clear
bash script.sh

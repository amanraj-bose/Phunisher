#!/bin/sh

if [ "$(whoami)" = "root" ]; then
    clear
    ./__init__.py
else
    clear
    printf "\n\e[1;34mPlease run on root, command for root access \e[1;32msudo su \e[1;34m\nand again run \e[1;33m./run.sh\e[1;34m for running Phunisher Framework\e[1;31m .....\e[1;37m"

fi

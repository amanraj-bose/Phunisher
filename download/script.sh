#!/bin/bash

clear
if [ "$(whoami)" == "root" ]; then
  printf '\e[1;34m'
  figlet Checking . . . .
  spinner() {
    local i checking num
    checking='/-\|'
    num=${#checking}
    printf ' '
    while sleep 0.1; do
      printf "%s\b" "${checking:i++%num:1}"
    done
  }
  printf '\e[1;34mChecking Your System \e[1;32m'
  spinner &
  sleep 2
  printf '\n\n'
  printf "\e[1;31mYou Are on Root Device \e[1;34m"
  sleep 3
  kill "$!"
  printf '\n'
  echo "$(tput setaf 2)"[*]Checking Necessary Repo ......"$(tput sgr0)"
  echo "$(tput setaf 2)""$(tput sgr0)"
  sudo apt-get install figlet -y
  sudo apt-get install xterm -y
  clear
  printf '\e[1;34m'
  echo "      
                   _____
                    ||
                    ||  
                |===========|
                    |P|
                    |U|
                    |N|
                    |I|
                    |S|
                    |H|
                    |E|
                    |R|
                    \_/
  "
  printf "\t\t\e[1;37m[\e[1;34mVersion : \e[1;32m1.0\e[1;37m]\n"
  if [ $(getconf LONG_BIT) = "64" ]; then
    printf "\n\t\t\e[1;32mOS Detected : 64 Bit\n"
  else
    printf "\n\t\t\e[1;32mOS Detected : 32 Bit\n"
  fi

  DISTRO=$(cat /etc/*-release | tr [:upper:] [:lower:] | grep -Poi '(debian|ubuntu|red hat|centos|nameyourdistro)' | uniq)
  if [ -z $DISTRO ]; then
    DISTRO='unknown'
  fi
  printf "\t\t\e[1;33mDetected Linux distribution: $DISTRO\e[1;37m"

  printf '\n\n\n'
  wget -q --tries=10 --timeout=20 --spider http://google.com
  if [ $? -eq 0 ]; then
    printf '\e[1;31m[\e[1;33mInternet Status\e[1;31m] \e[1;32m Internet Connection Availabel\n\n'
  else
    printf '\e[1;31m[\e[1;33mInternet Status\e[1;31m] \e[1;31m Internet Connection unavailabel\n\n'
  fi

  python="python3"
  which $python >/dev/null 2>&1
  if [ $? == 0 ]; then
    printf '\e[1;37m'
    echo "$(tput setaf 2)"[✓] Python3 is Already Installed"$(tput sgr0)"
    sleep 0.1s

  else
    printf '\e[1;37m'
    echo "$(tput setaf 1)"[✘] Python3 is not Installed"$(tput sgr0)"
    sleep 1s
    echo "$(tput setaf 3)"[!] Python3 is Installing......"$(tput sgr0)"
    xterm -T "☢ INSTALL PYTHON3 ☢" -geometry 100x30 -e "sudo apt-get install python3 -y"
    xterm -T "☢ INSTALL PYTHON3 ☢" -geometry 100x30 -e "apt-get install python3-pip -y"
    echo "$(tput setaf 2)"[✓] Python3 is Already Installed"$(tput sgr0)"
    sleep 0.1s

  fi
  cpp="g++"
  which $cpp >/dev/null 2>&1
  if [ $? == 0 ]; then
    printf '\e[1;37m'
    echo "$(tput setaf 2)"[✓] C++ is Already Installed"$(tput sgr0)"
    sleep 0.1s

  else
    printf '\e[1;37m'
    echo "$(tput setaf 1)"[✘] C++ is not Installed"$(tput sgr0)"
    sleep 1s
    echo "$(tput setaf 3)"[!] C++ is Installing......"$(tput sgr0)"
    xterm -T "☢ INSTALL C++ ☢" -geometry 100x30 -e "sudo apt-get install g++ -y"
    xterm -T "☢ INSTALL C++ ☢" -geometry 100x30 -e "sudo apt-get install build-essential -y"
    echo "$(tput setaf 2)"[✓] C++ is Installed"$(tput sgr0)"
    sleep 0.1s
  fi

  ruby="ruby"
  which $ruby >/dev/null 2>&1
  if [ $? == 0 ]; then
    printf '\e[1;37m'
    echo "$(tput setaf 2)"[✓] Ruby is Already Installed"$(tput sgr0)"
    sleep 0.1s

  else
    printf '\e[1;37m'
    echo "$(tput setaf 1)"[✘] Ruby is not Installed"$(tput sgr0)"
    sleep 1s
    echo "$(tput setaf 3)"[!] Ruby is Installing......"$(tput sgr0)"
    xterm -T "☢ INSTALL Ruby ☢" -geometry 100x30 -e "sudo apt-get install ruby -y"
    echo "$(tput setaf 2)"[✓] Ruby is Installed"$(tput sgr0)"
    sleep 0.1s
  fi
  printf '\e[1;33m[ Checking ] \e[1;31mPynput\n'
  xterm -T "Installing Python Modules" -geometry 100x30 -e "pip3 install pynput"
  sleep 0.1s
  printf '\e[1;32m[ Ok ] \e[1;32mPynput Installed\n'
  printf '\e[1;33m[ Checking ] \e[1;31mPyinstaller \n'
  xterm -T "Installing Python Modules" -geometry 100x30 -e "pip3 install pyinstaller"
  sleep 0.1s
  printf '\e[1;32m[ Ok ] \e[1;32mPyinstaller Installed\n'
  printf '\e[1;33m[ Checking ] \e[1;31mBeautifulSoup4 \n'
  xterm -T "Installing Python Module" -geometry 100x30 -e "pip3 install beautifulsoup4"
  sleep 0.1s
  printf '\e[1;32m[ Ok ] \e[1;32mBeautifulSoup4 Installed\n'
  printf '\e[1;33m[ Checking ] \e[1;31mPyWhatkit \n'
  xterm -T "Installing Python Module" -geometry 100x30 -e "pip3 install pywhatkit"
  sleep 0.1s
  printf '\e[1;32m[ Ok ] \e[1;32mPyWhatkit Installed\n'
  printf '\e[1;33m[ Checking ] \e[1;31mRequests \n'
  xterm -T "Installing Python Module" -geometry 100x30 -e "pip3 install requests"
  sleep 0.1s
  printf '\e[1;32m[ Ok ] \e[1;32mRequests Installed\n'
  printf '\e[1;33m[ Checking ] \e[1;31mHalo \n'
  xterm -T "Installing Python Module" -geometry 100x30 -e "pip3 install halo"
  sleep 0.1s
  printf '\e[1;32m[ Ok ] \e[1;32mHalo Installed\n'
  printf '\e[1;33m[ Checking ] \e[1;31mNumpy \n'
  xterm -T "Installing Python Module" -geometry 100x30 -e "pip3 install numpy"
  sleep 0.1s
  printf '\e[1;32m[ Ok ] \e[1;32mNumpy Installed\n'
  printf '\e[1;33m[ Checking ] \e[1;31mLolcat \n'
  xterm -T "Installing Ruby Module" -geometry 100x30 -e "gem install lolcat -y"
  sleep 0.1s
  printf '\e[1;32m[ Ok ] \e[1;32mLolcat Installed\n'
  # pip install PySocks
  printf '\e[1;33m[ Checking ] \e[1;31mPySocks \n'
  xterm -T "Installing Python Module" -geometry 100x30 -e "pip3 install PySocks"
  sleep 0.1s
  printf '\e[1;32m[ Ok ] \e[1;32mPySocks Installed\n'
  # pip install requests-futures
  printf '\e[1;33m[ Checking ] \e[1;31mRequests-Futures \n'
  xterm -T "Installing Python Module" -geometry 100x30 -e "pip3 install requests-futures"
  sleep 0.1s
  printf '\e[1;32m[ Ok ] \e[1;32mRequests-Futures Installed\n'
  # pip install certifi
  printf '\e[1;33m[ Checking ] \e[1;31mCertifi \n'
  xterm -T "Installing Python Module" -geometry 100x30 -e "pip3 install certifi"
  sleep 0.1s
  printf '\e[1;32m[ Ok ] \e[1;32mCertifi Installed\n'
  # pip install stem
  printf '\e[1;33m[ Checking ] \e[1;31mStem \n'
  xterm -T "Installing Python Module" -geometry 100x30 -e "pip3 install stem"
  sleep 0.1s
  printf '\e[1;32m[ Ok ] \e[1;32mStem Installed\n'
  # pip install torrequest
  printf '\e[1;33m[ Checking ] \e[1;31mTorrequest \n'
  xterm -T "Installing Python Module" -geometry 100x30 -e "pip3 install torrequest"
  sleep 0.1s
  printf '\e[1;32m[ Ok ] \e[1;32mTorrequest Installed\n'
  # pip install GitPython
  printf '\e[1;33m[ Checking ] \e[1;31mGitPython \n'
  xterm -T "Installing Python Module" -geometry 100x30 -e "pip3 install GitPython"
  sleep 0.1s
  printf '\e[1;32m[ Ok ] \e[1;32mGitPython Installed\n'
  # pip install keyboard
  printf '\e[1;33m[ Checking ] \e[1;31mKeyboard \n'
  xterm -T "Installing Python Module" -geometry 100x30 -e "pip3 install keyboard"
  sleep 0.1s
  printf '\e[1;32m[ Ok ] \e[1;32mKeyboard Installed\n'
  # pip install rarfile
  printf '\e[1;33m[ Checking ] \e[1;31mRarfile \n'
  xterm -T "Installing Python Module" -geometry 100x30 -e "pip3 install rarfile"
  sleep 0.1s
  printf '\e[1;32m[ Ok ] \e[1;32mRarfile Installed\n'
  # pip install pandas
  printf '\e[1;33m[ Checking ] \e[1;31mPandas \n'
  xterm -T "Installing Python Module" -geometry 100x30 -e "pip3 install pandas"
  sleep 0.1s
  printf '\e[1;32m[ Ok ] \e[1;32mPandas Installed\n'
  # 
  printf '\e[1;33m[ Checking ] \e[1;31mPandas-profiling \n'
  xterm -T "Installing Python Module" -geometry 100x30 -e "pip3 install pandas-profiling"
  sleep 0.1s
  printf '\e[1;32m[ Ok ] \e[1;32mPandas-profiling Installed\n'
  cd ../
  clear
  dos2unix __init__.py
  chmod +x __init__.py
  ./__init__.py
  
else

  printf '\e[1;34m'
  figlet Checking . . . .
  spinner() {
    local i checking n
    checking='/-\|'
    n=${#checking}
    printf ' '
    while sleep 0.1; do
      printf "%s\b" "${checking:i++%n:1}"
    done
  }
  clear
  printf '\e[1;34m'
  figlet Checking . . . .
  printf '\e[1;34mChecking Your System \e[1;32m'
  spinner &
  sleep 2
  printf '\n\n'
  printf "\e[1;31mYou Are not on Root Device\e[1;37m"
  kill "$!"
  printf '\n'
  exit
fi

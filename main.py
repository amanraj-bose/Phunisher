#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from modules.src.setting import setting
from sys import exit, stdout
from builtins import input, print, OSError, KeyboardInterrupt, Exception
from os import system
from threading import Thread, ThreadError, BrokenBarrierError
import urllib
from platform import platform
from modules.colour import color as cl
from modules.colour import bright as br
from modules.banner import banners, check, welcome
from random import choice
from halo import Halo
from time import sleep
from exploits.website.urlscrapping import scan_url
from webbrowser import open_new_tab
from exploits.website.web_cloning import url
from modules.donut import donut
from exploits.information_Gathering.port_scanning import port_scan
from urllib.request import urlopen
from pkg_resources import get_distribution, DistributionNotFound
from subprocess import call
from exploits.information_Gathering.image_data_extracter import data_extracter_from_images
from exploits.website.website_data_gathering import html
from pandas_profiling import ProfileReport
import pandas as pd
from json import load


class set:

    def choose(self):
        self.sprint(welcome)
        while True:
            self.input_system = str(
                input(f"\n\n{br.red_1}Phunisher@Framework{cl.yellow}:~ \033[0m{cl.green}"))
            if self.input_system == "setting" or self.input_system == "S":
                system("clear")
                setting()
            elif self.input_system == "start" or self.input_system == "run":
                system("clear")
                self.__main__()
            elif self.input_system == "start -c" or self.input_system == "run -c":
                system("clear")
                self.main()
            elif self.input_system == "start --skip" or self.input_system == "run --skip":
                system("clear")
                sleep(1)
                self.main_window()
            elif self.input_system == "start --cs" or self.input_system == "run --cs":
                system("clear")
                self.checker()
            elif self.input_system == "phf --help" or self.input_system == "phf -h" or self.input_system == "run --help" or self.input_system == "run -h" or self.input_system == "help" or self.input_system == "?":
                print(f"""{cl.white}
                Usage : [options] [sub-options]

                --help or -help                          For help
                start [-c] [--skip] [--cs]            For start punisher framework for such options -c for without checking
                                                         --skip for starting not any dynamic starter or start for starting the punisher framework
                                                         and starting only on check menu to user this command --cs
                """)
            elif self.input_system == "clear" or self.input_system == "cls":
                system("clear")
            elif self.input_system == "exit" or self.input_system == "quit":
                exit(0)
            elif self.input_system == "sudo apt-get update" or self.input_system == "sudo apt update" or self.input_system == "apt-get update" or self.input_system == "apt update":
                system("sudo apt-get update")
            elif self.input_system == "ls" or self.input_system == "dir":
                system("ls")
            else:
                print("")

    def internet_checking(self) -> None:
        try:
            urlopen("https://www.google.com/",  timeout=5)
            return True
        except urllib.error.URLError:
            return False

    def sprint(self, value):
        for word in value + '\n':
            stdout.write(word)
            stdout.flush()
            sleep(0.05)

    def slow(self, value):
        for word in value + '\n':
            stdout.write(word)
            stdout.flush()
            sleep(0.01)

    def installer(self) -> None:
        while True:
            self.installer = str(input(f"\n{cl.blue}Installer > {cl.white}"))
            if self.installer == "Y" or self.installer == "y" or self.installer == "yes" or self.installer == "Yes" or self.installer == "YES" or self.installer == "1":
                for installed in ['requests', 'halo', 'numpy', 'beautifulsoup4', 'pynput', 'PySocks', 'requests-futures', 'certifi', 'stem', 'torrequest', 'GitPython', 'keyboard', 'rarfile', 'pandas', 'pandas-profiling', 'pyinstaller']:
                    call(['pip3', 'install', installed])
                exit(0)
            elif self.installer == "N" or self.installer == "n" or self.installer == "no" or self.installer == "No" or self.installer == "NO" or self.installer == "0":
                system("clear")
                exit(0)
            elif self.installer == "quit" or self.installer == "exit":
                exit(0)
            elif self.installer == "help" or self.installer == "?" or self.installer == "phf --help" or self.installer == "phf -h":
                print(f"""\n{cl.white}If you are choose{cl.green} Y, yes, y, YES, Yes, 1{cl.white} .it will be installing all modules but you choose {cl.red}N, n, no, No, NO, 0 {cl.white}.it will not install any module any some error occured on your tool""")
            else:
                print("")

    def internet_result(self) -> None:
        if self.internet_checking():
            self.sprint("\n" + "\033[91m" + "[" + "\033[93m" +
                        "*" + "\033[91m" + "]" + "\033[93m" + " Checking Internet Connection....")
            sleep(0.2)
            self.slow("\n" + cl.cyan + "[" + cl.green + "+" + cl.cyan +
                      "]" + cl.blue + " Internet Connection is available")
        else:
            self.slow("\n" + "\033[91m" + "[" + "\033[93m" +
                      "*" + "\033[91m" + "]" + "\033[93m" + " Checking Internet Connection....")
            sleep(0.2)
            self.slow("\n" + cl.cyan + "[" + cl.yellow + "-" + cl.cyan +
                      "]" + cl.red + " Internet Connection is UnAvailable")

    def module_checking(self) -> None:
        for modules in ['requests', 'halo', 'numpy', 'beautifulsoup4', 'pynput', 'PySocks', 'requests-futures', 'certifi', 'stem', 'torrequest', 'GitPython', 'keyboard', 'rarfile', 'pandas', 'pandas-profiling', 'pyinstaller']:
            try:
                dist = get_distribution(modules)
                self.sprint(
                    f"{cl.blue}[{cl.green}+{cl.blue}] {cl.cyan}Module is Found {cl.green} --> {dist.key}{cl.magenta}({dist.version})")
            except DistributionNotFound and KeyboardInterrupt and Exception:
                self.sprint(
                    f"{cl.red}[{cl.yellow}-{cl.red}] {cl.red}Module is not Found --> {cl.blue}{modules} ")
                self.installer()

    def checking(self) -> None:
        system("clear")
        self.slow(check)
        self.sprint(f"""{cl.blue}
            \t\t\t\t  |_    Name : Phunisher        _|
            \t\t\t\t  |_    Written in : Python     _|
            \t\t\t\t  |_    Created By {cl.red}Aman Raj {cl.blue}    _|
            \t\t\t\t  |_    \033[47mMade    in   India \033[0m  {cl.blue}   _|""")
        print("\n\n")
        self.internet_result()
        self.sprint("\033[92m" + "[" + "\033[94m" +
                        "*" + "\033[92m" + "]" + f"{cl.blue} System Found ----> {cl.green}{platform()}")
        self.module_checking()
        print('\n\n')
        sleep(5)

    def starting(self) -> None:
        system("clear")
        donut()
        self.spinner = Halo(
            text=f'{br.white_1}  Starting Phunisher Framework', spinner='dot')
        self.spinner.start()
        sleep(5)
        self.spinner.stop()

    def main_window(self) -> None:
        system("clear")
        stdout.write(choice(banners))
        print("\n")

        print(f"""
        {br.white_1}

    {cl.red}[{cl.yellow}1{cl.red}]{cl.blue} Website attack{cl.red} {br.red_1}[Required Internet] {cl.red}
    [{cl.yellow}2{cl.red}]{cl.blue} Destroyer {cl.red}
    [{cl.yellow}3{cl.red}]{cl.blue} Third Party Modules {cl.red}
    [{cl.yellow}4{cl.red}]{cl.blue} Port Scanner {cl.red}
    [{cl.yellow}5{cl.red}]{cl.blue} Help, Credits, About {cl.white}

    99) Exit from Phunisher
        """)
        while True:
            self.user = str(
                input(f"{cl.blue}PHF{cl.red}_{cl.blue}> {br.white_1}"))
            if self.user == "1" or self.user == "01":
                self.website()
            elif self.user == "2" or self.user == "02":
                self.destroyer()
            elif self.user == "99":
                system("clear")
                exit(0)
            elif self.user == "3" or self.user == "03":
                self.gathering()
            elif self.user == "4" or self.user == "04":
                self.scanner()
            elif self.user == "5" or self.user == "05":
                self.help()
            elif self.user == "cls":
                system("clear")
            elif self.user == "quit":
                exit(0)
            elif self.user == "banner":
                self.main_window()
            elif self.user == "help":
                print(f"""
                {cl.green}

                This Tool is made up for Pen-Tester.it is just like a social engineering toolkit. his Version is {cl.red}1.0.0{cl.green}\n
                """)
            else:
                self.main_window()

    def website(self) -> None:
        system("clear")
        stdout.write(choice(banners))
        print("\n")
        print(f"""
        {br.white_1}

    {cl.red}
    [{cl.yellow}1{cl.red}]{cl.blue} Website Cloning {cl.red}
    [{cl.yellow}2{cl.red}]{cl.blue} Url Scraping {cl.red}
    [{cl.yellow}3{cl.red}]{cl.blue} Website Data Gather {cl.green}(Filter the special tag data){cl.white}

    99) Back to Main Window
        """)
        while True:
            self.website_input = str(input(
                f"{cl.blue}PHF{cl.white}({cl.red}Website{cl.white}){cl.blue}_> {br.white_1}"))

            if self.website_input == "1" or self.website_input == "01":
                    print(f"""\n{br.white_1}Please Enter the website name because they clone us and filename with .html but onething important Internet
Connection required\n""")
                    url(str(input(f"{br.white_1}\n{cl.blue}PHF {cl.white}({cl.red}website/Website Cloning {cl.blue}[{cl.green}Enter the url{cl.blue}]{cl.white}){cl.blue}_> {br.white_1}")),
                    str(input(
                        f"\n{cl.blue}PHF {cl.white}({cl.red}website/Website Cloning {cl.blue}[{cl.green}Enter the Filename with {cl.yellow}<.htm/.html>{cl.blue}]{cl.white}){cl.blue}_> {br.white_1}")),
                    str(input(f"""\n{cl.blue}PHF {cl.white}({cl.red}website/Website Cloning {cl.blue}[{cl.green}Enter the Y/n because if you choose 'Y',
automatic open website on your default browser. and save it on Desktop folder.if you 'n'. it will giving file on Desktop folder {cl.blue}]{cl.white}){cl.blue}_> {br.white_1}""")),
                    str(input(f"{br.white_1}\n{cl.blue}PHF {cl.white}({cl.red}website/Website Cloning {cl.blue}[{cl.green}Enter the username{cl.blue}]{cl.white}){cl.blue}_> {br.white_1}")))
                    print("\n")
            elif self.website_input == "99":
                self.main_window()
            elif self.website_input == "2" or self.website_input == "02":
                print(f"""{br.white_1}
if You are not giving url then
it will giving error or must be required internet connection""")

                scan_url()
            elif self.website_input == "cls":
                system("clear")
            elif self.website_input == "quit":
                exit(0)
            elif self.website_input == "banner":
                self.website()
            elif self.website_input == "help":
                print(f"""
                {cl.green}

                This Tool is made up for Pen-Tester.it is just like a social engineering toolkit. his Version is {cl.red}1.0.0{cl.green}\n
                """)
            elif self.website_input == "03" or self.website_input == "3":
                html(str(input(f"{br.white_1}\n{cl.blue}PHF {cl.white}({cl.red}website/Website Data Gather{cl.blue}[{cl.green}Enter the URl{cl.blue}]{cl.white}){cl.blue}_> {br.white_1}")), str(input(f"{br.white_1}\n{cl.blue}PHF {cl.white}({cl.red}website/Website Data Gather{cl.blue}[{cl.green}Enter the Tag Name{cl.blue}]{cl.white}){cl.blue}_> {br.white_1}")), str(input(
                    f"{br.white_1}\n{cl.blue}PHF {cl.white}({cl.red}website/Website Data Gather{cl.blue}[{cl.green}Enter the Options, if You are choose 1 that make file of your scrap your given tag then make parse_data.html{cl.blue}]{cl.white}){cl.blue}_> {br.white_1}")), str(input(f"{br.white_1}\n{cl.blue}PHF {cl.white}({cl.red}website/Website Data Gather{cl.blue}[{cl.green}Enter the UserName{cl.blue}]{cl.white}){cl.blue}_> {br.white_1}")))
            else:
                self.website()

    def bruteforce(self) -> None:
        pass

    def windows_System(self) -> None:
        system("clear")
        stdout.write(choice(banners))
        print("\n")
        print(f"""{br.white_1}

        1) Exe Already Maded {cl.red}(recommded){cl.white}
        2) Exe made Quickly {cl.red}(Required Internet Connection){cl.white}

        99) Back Destroyer/Windows
        """)
        while True:
            self.windows = str(input(
                f"{cl.blue}PHF{cl.white}({cl.red}Destroyer/Corrupted EXE/Windows{cl.white}){cl.blue}_> {br.white_1}"))
            if self.windows == "1" or self.windows == "01":
                self.user_input_windows = str(input(
                    f"{br.white_1}\n{cl.blue}PHF {cl.white}({cl.red}Destroyer/Corrupted EXE/Windows {cl.blue}[{cl.green}Enter the username{cl.blue}]{cl.white}){cl.blue}_> {br.white_1}"))
                print(
                    f"{cl.blue}[{cl.red}*{cl.red}] {cl.green}Sometime for Copying exploit\n")
                sleep(.2)
                system(
                    f"sudo cp -r exploits/window_corrupter /home/{self.user_input_windows}/Desktop")
                print(
                    f"{cl.red}[{cl.yellow}Note{cl.red}]{cl.blue} Check Your Desktop Folder\n")
            elif self.windows == "2" or self.windows == "02":
                system(
                    "xterm -T 'EXE for windows DESTROYER' -geometry 100x30 -e 'sudo pyinstaller --onefile exploits/window_corrupter.py'")
                self.user_input_windows_exe = str(input(
                    f"{br.white_1}\n{cl.blue}PHF {cl.white}({cl.red}Destroyer/Corrupted EXE/Windows {cl.blue}[{cl.green}Enter the username{cl.blue}]{cl.white}){cl.blue}_> {br.white_1}"))
                system(
                    f"sudo cp -r exploits/dist/window_corrupter /home/{self.user_input_windows_exe}/Desktop")
                system("sudo rm -r exploits/dist")
                system("sudo rm -r exploits/build")
                system("sudo rm -r exploits/window_corrupter.spec")
            elif self.windows == "99":
                self.destroyer_menu()
            elif self.windows == "cls":
                system("clear")
            elif self.windows == "quit":
                exit(0)
            elif self.windows == "banner":
                self.windows_System()
            elif self.windows == "help":
                print(f"""
                {cl.green}

                This Tool is made up for Pen-Tester.it is just like a social engineering toolkit. his Version is {cl.red}1.0.0{cl.green}\n
                """)
            else:
                self.windows_System()

    def destroyer_menu(self) -> None:
        system("clear")
        stdout.write(choice(banners))
        print("\n")

        print(f"""{br.white_1}
        {cl.red}[{cl.yellow}1{cl.red}] {cl.yellow}Windows
        {cl.red}[{cl.yellow}2{cl.red}] {cl.yellow}Linux
        {cl.red}[{cl.yellow}3{cl.red}] {cl.yellow}Android{cl.white}

        99) back to destroyer Window

        """)
        while True:
            self.main_destroyer_input = str(input(
                f"{cl.blue}PHF{cl.white}({cl.red}Destroyer/Corrupted EXE{cl.white}){cl.blue}_> {br.white_1}"))
            if self.main_destroyer_input == "1" or self.main_destroyer_input == "01":
                self.windows_System()
            elif self.main_destroyer_input == "99":
                self.destroyer()
            elif self.main_destroyer_input == "cls":
                system("clear")
            elif self.main_destroyer_input == "quit":
                exit(0)
            elif self.main_destroyer_input == "banner":
                self.destroyer_menu()
            elif self.main_destroyer_input == "help":
                print(f"""
                {cl.green}

                This Tool is made up for Pen-Tester.it is just like a social engineering toolkit. his Version is {cl.red}1.0.0{cl.green}\n
                """)
            else:
                self.destroyer_menu()

    def destroyer_menu_2(self) -> None:
        system("clear")
        stdout.write(choice(banners))
        print("\n")
        print(f"""
        {br.red_1}[{br.yellow_1}1{br.red_1}] {br.yellow_1}Windows
        {cl.red}[{cl.yellow}2{cl.red}] {cl.yellow}Linux
        {cl.red}[{cl.yellow}3{cl.red}] {cl.yellow}Android{cl.white}

        99) back to destroyer Window

        """)
        self.destroyer_menu_2_input = str(input(
            f"{cl.blue}PHF{cl.white}({cl.red}Destroyer/CPU Overload{cl.white}){cl.blue}_> {br.white_1}"))
        if self.destroyer_menu_2_input == "1" or self.destroyer_menu_2_input == "01":
            print(f"""{br.white_1}
            (1) Automatic
            (2) Manually {br.red_1}(Time and Internet Consuming){br.white_1}

            99) Back to Destroyer Menu
            """)
            self.windows_cpu_overload_input = str(input(
                f"{cl.blue}PHF{cl.white}({cl.red}Destroyer/Cpu Overload/Windows{cl.white}){cl.blue}_> {br.white_1}"))
            if self.windows_cpu_overload_input == "1" or self.windows_cpu_overload_input == "01":
                self.user_input_windows_cpu = str(input(
                    f"{br.white_1}\n{cl.blue}PHF {cl.white}({cl.red}Destroyer/Cpu Overload/Windows {cl.blue}[{cl.green}Enter the username{cl.blue}]{cl.white}){cl.blue}_> {br.white_1}"))
                print("Sometime for Copying the exploit")
                system(
                    f'cp -r exploits/cpu_overload /home/{self.user_input_windows_cpu}/Desktop')
                print(
                    f"{br.red_1}Exploits already copide on you {br.green_1}Desktop{br.white_1}")
            elif self.destroyer_menu_2_input == "2" or self.destroyer_menu_2_input == "02":
                system(
                    "xterm -T 'Cpu overload converted into Exe' -geometry 100x30 -e 'sudo pyinstaller --onefile exploits/cpu_overload.py'")
                self.user_input_windows_exe_cpu = str(input(
                    f"{br.white_1}\n{cl.blue}PHF {cl.white}({cl.red}Destroyer/Cpu Overload/Windows {cl.blue}[{cl.green}Enter the username{cl.blue}]{cl.white}){cl.blue}_> {br.white_1}"))
                system(
                    f"sudo cp -r exploits/dist/cpu_overload.py /home/{self.user_input_windows_exe_cpu}/Desktop")
                system("sudo rm -r exploits/dist")
                system("sudo rm -r exploits/build")
                system("sudo rm -r exploits/cpu_overload.spec")
            elif self.destroyer_menu_2_input == "99":
                self.destroyer()
            elif self.destroyer_menu_2_input == "cls":
                system("clear")
            elif self.destroyer_menu_2_input == "quit":
                exit(0)
            elif self.destroyer_menu_2_input == "banner":
                self.destroyer_menu_2()
            elif self.destroyer_menu_2_input == "help":
                print(f"""
                {cl.green}

                This Tool is made up for Pen-Tester.it is just like a social engineering toolkit. his Version is {cl.red}1.0.0{cl.green}\n
                """)
        else:
            self.destroyer_menu_2()

    def destroyer(self) -> None:
        system("clear")
        stdout.write(choice(banners))
        print("\n")
        print(f"""{br.white_1}
    1) Corrupted EXE
    2) CPU Overload

    99) Back to Main Window

        """)
        while True:
            self.destroyer_input = str(input(
                f"{cl.blue}PHF{cl.white}({cl.red}Destroyer{cl.white}){cl.blue}_> {br.white_1}"))
            if self.destroyer_input == "1" or self.destroyer_input == "01":
                self.destroyer_menu()
            elif self.destroyer_input == "2" or self.destroyer_input == "02":
                self.destroyer_menu_2()
            elif self.destroyer_input == "99":
                self.main_window()
            elif self.destroyer_input == "cls":
                system("clear")
            elif self.destroyer_input == "quit":
                exit(0)
            elif self.destroyer_input == "banner":
                self.destroyer()
            elif self.destroyer_input == "help":
                print(f"""
                {cl.green}

                This Tool is made up for Pen-Tester.it is just like a social engineering toolkit. his Version is {cl.red}1.0.0{cl.green}\n
                """)
            else:

                self.destroyer()

    def gathering(self) -> None:
        system("clear")
        stdout.write(choice(banners))
        print("\n")
        print(f"""
        {br.red_1}[{br.yellow_1}1{br.red_1}] Image Data Gathering{br.white_1}
        {br.red_1}[{br.yellow_1}2{br.red_1}] Data analysising{br.white_1}
        {br.red_1}[{br.yellow_1}3{br.red_1}] Json Data to CSV Data{br.white_1}

        99) Back to Main Window
        """)
        while True:
            self.gathering_input = str(input(
                f"{cl.blue}PHF{cl.white}({cl.red}Gathering Data{cl.white}){cl.blue}_> {br.white_1}"))
            if self.gathering_input == "1" or self.gathering_input == "01":
                data_extracter_from_images(str(input(f"{cl.blue}PHF{cl.white}({cl.red}Gathering / Image Data Gathering{cl.blue}[{cl.green}If you are enter the value [1] so your give an image_data.txt but if you choose [2] so all data print on your terminal{cl.blue}]{cl.white}){cl.blue}_> {br.white_1}")), str(
                    input(f"{cl.blue}PHF{cl.white}({cl.red}Gathering/ Image Data Gathering{cl.blue}[{cl.green}Enter the image Folder path{cl.blue}]{cl.white}){cl.blue}_> {br.white_1}")))
                system("mv data.txt /home")
                print("\ndata.txt ----> Go on Your Home Folder\n")
            elif self.gathering_input == "3" or self.gathering_input == "03":
                self.json_file_name = str(input(
                    f"{cl.blue}PHF{cl.white}({cl.red}Gathering/Json File to CSV Data{cl.blue}[{cl.green}Enter the Json file name or Path{cl.blue}]{cl.white}){cl.blue}_> {br.white_1}"))
                with open(self.json_file_name, "r") as f:
                    json_variable = pd.DataFrame(dict(load(f)))
                self.file_choser = str(input(
                    f"{cl.blue}PHF{cl.white}({cl.red}Gathering/Json File to CSV Data{cl.blue}[{cl.green}If you choose YES then the make specific file in CSV. if not you choose NO then print on your terminal or if you choose HTML then made up of html file{cl.blue}]{cl.white}){cl.blue}_> {br.white_1}"))
                if self.file_choser == "html" or self.file_choser == "HTML" or self.file_choser == "Html":
                    json_variable.to_html("data.html")
                    system("mv data.html /home")
                    print(f"data.csv  ----->   Go on Your Home Folder\n")
                elif self.file_choser == "No" or self.file_choser == "NO" or self.file_choser == "no":
                    print(json_variable)
                else:
                    json_variable.to_csv("data.csv")
                self.index_allow = str(input(
                    f"{cl.blue}PHF{cl.white}({cl.red}Gathering/Json File to CSV Data{cl.blue}[{cl.green}If you choose true then the not change in your index of csv but you are choose false then they off the indexing option{cl.blue}]{cl.white}){cl.blue}_> {br.white_1}"))
                if self.index_allow == "false" or self.index_allow == "False" or self.index_allow == "FALSE":
                    json_variable.to_csv("data.csv", index=False)
                    system("mv data.csv /home")
                    print(f"\ndata.csv  ----->   Go on Your Home Folder\n")
                else:
                    json_variable.to_csv("data.csv", index=True)
                    system("mv data.csv /home")
                    print(f"\ndata.csv  ----->   Go on Your Home Folder\n")
            elif self.gathering_input == "99":
                self.main_window()
            elif self.gathering_input == "cls":
                system("clear")
            elif self.gathering_input == "quit":
                exit(0)
            elif self.gathering_input == "banner":
                self.gathering()
            elif self.gathering_input == "help":
                print(f"""
                    {cl.green}

                    This Tool is made up for Pen-Tester.it is just like a social    engineering toolkit. his Version is {cl.red}1.0.0{cl.green}\n
                    """)
            elif self.gathering_input == "02" or self.gathering_input == "2":
                def analysis(path, filename, login_name) -> str:
                    data_frame = pd.read_csv(path)
                    profile = ProfileReport(data_frame)
                    profile.to_file(output_file=f"{filename}.html")
                    system(f"mv {filename}.html /home/{login_name}/Desktop")
                analysis(str(input(f"{cl.blue}PHF{cl.white}({cl.red}Gathering/Data analysising{cl.blue}[{cl.green}Enter the path of the csv file{cl.blue}]{cl.white}){cl.blue}_> {br.white_1}")), str(input(
                    f"{cl.blue}PHF{cl.white}({cl.red}Gathering/Data analysising{cl.blue}[{cl.green}Enter the Filename{cl.blue}]{cl.white}){cl.blue}_> {br.white_1}")), str(input(f"{cl.blue}PHF{cl.white}({cl.red}Gathering/Data analysising{cl.blue}[{cl.green}Enter the UserName{cl.blue}]{cl.white}){cl.blue}_> {br.white_1}")))
                print(f"\n{br.cyan_1}Go On your {br.green_1}Desktop {br.cyan_1}Folder\n")
            else:
                self.gathering()

    def scanner(self) -> None:
        system("clear")
        stdout.write(choice(banners))
        print("\n")
        print(f"""{br.white_1}
    {cl.red}[{cl.yellow}1{cl.red}] {cl.yellow}Port Scanner {br.cyan_1}  [{br.red_1}Buggy and Slower{br.cyan_1}]
    {cl.red}[{cl.yellow}2{cl.red}] {cl.yellow}Port Scanner Faster   {cl.white}{br.cyan_1}[{br.green_1}Faster & recommded{br.cyan_1}]{br.white_1}

    99) Back to Main Window
        """)
        while True:
            self.scanner_input = str(input(
                f"{cl.blue}PHF{cl.white}({cl.red}Port Scanner{cl.white}){cl.blue}_> {br.white_1}"))

            if self.scanner_input == "99":
                self.main_window()
            elif self.scanner_input == "cls":
                system("clear")
            elif self.scanner_input == "quit":
                exit(0)
            elif self.scanner_input == "banner":
                self.destroyer()
            elif self.scanner_input == "help":
                print(f"""
                    {cl.green}

                    This Tool is made up for Pen-Tester.it is just like a social    engineering toolkit. his Version is {cl.red}1.0.0{cl.green}\n
                    """)
            elif self.scanner_input == "1" or self.scanner_input == "01":
                port_scan(str(input(f"{cl.blue}PHF{cl.white}({cl.red}Port Scanner/Port Scanner{cl.blue}[{cl.green}Enter the Ip/Valid Website{cl.blue}]{cl.white}){cl.blue}_> {br.white_1}")), str(
                    input(f"{cl.blue}PHF{cl.white}({cl.red}Port Scanner/Port Scanner{cl.blue}[{cl.green}Enter the Port{cl.blue}]{cl.white}){cl.blue}_> {br.white_1}")))
            elif self.scanner_input == "2" or self.scanner_input == "02":
                try:
                    from exploits.information_Gathering.port_scanner_faster import scanner, start_port, end_port
                    print("\n")
                    for ports in range(start_port, end_port+1):
                        thread = Thread(target=scanner, args=(ports,))
                        thread.start()
                    print("\n")
                except ThreadError and BrokenBarrierError and KeyboardInterrupt and OSError:
                    print("")
            else:
                self.scanner()

    def help(self) -> None:
        system("clear")
        stdout.write(choice(banners))
        print("\n")
        print(f"""
    {br.green_1}
        1) Help
        2) About
        3) Credit

        {cl.white}99) Back to Main Window
        """)
        while True:

            self.help_input = str(
                input(f"{cl.blue}PHF{cl.white}({cl.red}Help{cl.white}){cl.blue}_> {br.white_1}"))

            if self.help_input == "1" or self.help_input == "01":
                print(f"""{cl.green}

                This Tool is made up for Pen-Tester.it is just like a social engineering toolkit. his Version is {cl.red}1.0.0{cl.green}\n""")
            elif self.help_input == "2" or self.help_input == "02":
                system("cd ../website")
                open_new_tab("index.html")
            elif self.help_input == "3" or self.help_input == "03":
                open_new_tab("https://github.com/amanraj9077/readme.md")
            elif self.help_input == "99":
                self.main_window()
            elif self.help_input == "cls":
                system("clear")
            elif self.help_input == "quit":
                exit(0)
            elif self.help_input == "banner":
                self.help()
            elif self.help_input == "help":
                print(f"""
                {cl.green}

                This Tool is made up for Pen-Tester.it is just like a social engineering toolkit. his Version is {cl.red}1.0.0{cl.green}\n
                """)
            else:
                system("clear")
                self.help()

    def checker(self):
        try:
            self.checking()
            self.main_window()
        except KeyboardInterrupt and Exception and KeyboardInterrupt as e:
            print("")

    def main(self) -> None:
        try:
            self.starting()
            self.main_window()
        except KeyboardInterrupt and Exception and KeyboardInterrupt as e:
            print("")

    def __main__(self) -> None:
        try:
            self.checking()
            self.starting()
            self.main_window()
        except KeyboardInterrupt and Exception and KeyboardInterrupt as e:
            print("")

    def __Main_Over__(self):
        try:
            self.choose()
        except KeyboardInterrupt and Exception and KeyboardInterrupt as e:
            print("")

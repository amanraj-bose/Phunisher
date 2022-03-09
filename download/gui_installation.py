#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import urllib
from os import system
from subprocess import call
from tkinter import *
from tkinter import messagebox
import pyttsx3
from urllib.request import urlopen
from pkg_resources import DistributionNotFound, get_distribution
from colour import color as cl

system("dos2unix install.py")

class download(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.title("Phunisher Installation")

    def Internet(self):
        try:
            urlopen("https://google.com/", timeout=5)
            return True
        except urllib.error.URLError:
            return False

    def clear(self):
        for items in self.Framizeation.winfo_children():
            items.destroy()

    def copyrights(self):
        self.Framizeation = Frame(self)
        self.Framizeation.pack()
        Label(self.Framizeation, text="""Copyright 2022 aman_raj,amanraj-9077 and others

    Licensed under the Apache License, Version 2.0 
    (the "License"); you may not use this file except 
    in compliance with the License.You may obtain a copy 
of the License at : 
     http://www.apache.org/licenses/LICENSE-2.0""", bd=0, foreground="#000", background="yellow", font=('Terminal', 18), justify=CENTER).pack(side=TOP)
        self.next_button = Button(self.Framizeation, text="Finish", fg="#000",
                                  bg="#adff2f", command=lambda: [quit()], relief=SUNKEN, bd=3)
        self.next_button.pack(side=TOP, anchor="e", pady=5, padx=2)
        self.back_button = Button(
            self.Framizeation, text="Exit", fg="#000", bg="#cd5c5c", command=quit, relief=SUNKEN)
        self.back_button.pack(side=TOP, anchor="w", padx=2, pady=0)

        self.speak_button = Button(
            self.Framizeation, fg="#000", bg="magenta", command=self.speak_right, text="e")
        self.speak_button.pack(side=TOP, anchor="n")

    def status(self):
        self.root_status = StringVar()
        if self.Internet():
            self.root_status.set("Internet Connection Available")
        else:
            self.root_status.set("Internet Connection Unavilabel")
            messagebox.showwarning("Error", "Connection not availabel")
        self.status_label = Label(
            self, textvariable=self.root_status, foreground="#000", anchor="w", bg="grey")
        self.status_label.pack(side=BOTTOM, fill=X)

    def clear_main(self):
        for widget in self.Frameize.winfo_children():
            widget.destroy()
        for frameize2 in self.Frameize_2.winfo_children():
            frameize2.destroy()
        for frameize3 in self.Frameize_3.winfo_children():
            frameize3.destroy()
        for up_down in self.Frame_UP_DOWN.winfo_children():
            up_down.destroy()

    def all(self):
        self.Frameize = Frame(self)
        self.Frameize.pack(side=TOP, padx=5, pady=2, anchor="n", fill=X)
        self.module_Label = Label(self.Frameize, text="\t\tModules\t\t",
                                  fg="#000", bg="green", relief=RAISED, font=('ds-digital', 20), bd=0)
        self.module_Label.pack(side=LEFT, anchor="w")
        self.Install_button = Button(self.Frameize, bg="red", fg="black",
                                     text="  Install  ", command=self.module, font=("ds-digital", 20), bd=5)
        self.Install_button.pack(side=LEFT, anchor="e", padx=30)

        self.Frameize_2 = Frame(self)
        self.Frameize_2.pack(side=TOP, padx=5, pady=2, anchor="n", fill=X)
        self.package_Label = Label(self.Frameize_2, text="\tLinux Packages\t\t",
                                   fg="#000", bg="yellow", relief=RAISED, font=('ds-digital', 20), bd=0)
        self.package_Label.pack(side=LEFT, anchor="w")
        self.Install_packages_button = Button(
            self.Frameize_2, bg="red", fg="black", text="  Install  ", command=self.package, font=("ds-digital", 20), bd=5)
        self.Install_packages_button.pack(side=LEFT, anchor="e", padx=30)

        self.Frameize_3 = Frame(self)
        self.Frameize_3.pack(side=TOP, padx=5, pady=2, anchor="n", fill=X)
        self.Both_Label = Label(self.Frameize_3, text="\t\tBoth\t\t", fg="#000",
                                bg="cyan", relief=RAISED, font=('ds-digital', 20), bd=0)
        self.Both_Label.pack(side=LEFT, anchor="w")
        self.Install_Both_button = Button(
            self.Frameize_3, bg="red", fg="black", text="  Install  ", command=lambda: [self.module(), self.package()], font=("ds-digital", 20), bd=5)
        self.Install_Both_button.pack(side=LEFT, anchor="e", padx=30)

        self.Frame_UP_DOWN = Frame(self)
        self.Frame_UP_DOWN.pack(side=BOTTOM, fill=X)
        self.Next_Button = Button(
            self.Frame_UP_DOWN, bg="#adff2f", fg="black", command=lambda: [self.clear_main(), self.copyrights()], text="Next", bd=3)
        self.Next_Button.pack(side=RIGHT)
        self.Exit_Button = Button(
            self.Frame_UP_DOWN, bg="#cd5c5c", fg="black", command=quit, text="Exit", bd=3)
        self.Exit_Button.pack(side=LEFT, anchor=W)

    def module(self):
        system("clear")
        for modules in ['requests', 'halo', 'numpy', 'beautifulsoup4', 'pynput', 'PySocks', 'requests-futures', 'certifi', 'stem', 'torrequest', 'GitPython', 'keyboard', 'rarfile']:
            try:
                dist = get_distribution(modules)
                print("Time ==> ",time.strftime("%H:%M:%S:%p").replace("''", ""))
                print(
                    f"{cl.blue}[{cl.green}+{cl.blue}] {cl.cyan}Module is Found {cl.green} --> {dist.key}{cl.magenta}({dist.version})")

            except DistributionNotFound and KeyboardInterrupt and Exception:
                for installed in ['requests', 'halo', 'numpy', 'beautifulsoup4', 'pynput', 'PySocks', 'requests-futures', 'certifi', 'stem', 'torrequest', 'GitPython', 'keyboard', 'rarfile']:
                    call(['pip3', 'install', installed])
                system("clear")
                times = time.strftime("%H:%M:%S:%p").replace("''", "")
                print(f"{cl.magenta}[{cl.white}*{cl.magenta}] {cl.yellow}Installed all modules at {times}")
    def package(self):
        for installed in ['python3', 'python3-pip', 'g++', 'build-essential', 'ruby']:
            call(['sudo', 'apt', 'install', installed, '-y'])
        system("clear")
        times = time.strftime("%H:%M:%S:%p").replace("''", "")
        print(f"{cl.magenta}[{cl.white}*{cl.magenta}] {cl.yellow}Installed all Packages at {times}")

    def speak(self, text):
        pyttsx3.speak(text)

    def speak_right(self):
        self.speak("""
        Copyright 2022 aman_raj,amanraj-9077 and others
    Licensed under the Apache License, Version 2.0 
    (the "License"); you may not use this file except 
    in compliance with the License.You may obtain a copy 
of the License at : 
     http://www.apache.org/licenses/LICENSE-2.0
        """)

    def about(self):
        pass

    def download(self):
        self.status()
        self.all()


if __name__ == '__main__':
    try:
        r = download()
        r.download()
        r.mainloop()
    except AttributeError:
        print("")

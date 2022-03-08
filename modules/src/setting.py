import os
from git import Git
from git import GitError
from modules.colour import color as cl
from sys import exit



def update(path) -> str:
    try:
        Git(f"{path}").clone(
            "https://github.com/amanraj-9077/Phunisher_Framework.git")
        print("Update Succesfully")
    except GitError and KeyboardInterrupt and Exception and TimeoutError as e:
        print(f"{cl.red}Some Error occured{cl.white}")


def setting() -> None:
    print("\033[1;44m")
    print(f"""{cl.white}
    (1) configuration
    (2) update
    (3) reinstall

    (99) exit
    \n\n\n""")
    while True:
        user_input = str(input(f"\033[1;34m{cl.white}BIOS > "))
        if user_input == "1" or user_input == "01":
            configure(str(input(
                f"{cl.white}BIOS [Enter your Id] > ")), str(input( f"{cl.white}BIOS [Enter your Email] > ")))
        elif user_input == "2" or user_input == "02":
            update(
            str(input(f"{cl.white}BIOS [Enter Your Phunisher Framework Path] > ")))
        elif user_input == "3" or user_input == "03":
            reinstall()
        elif user_input == "99":
            exit(0)
        else:
            print("")


def configure(ids, email) -> str:
    with open('id.txt', 'w') as f:
        f.write(ids)
    with open('email.txt', 'w') as g:
        g.write(email)


def reinstall() -> None:
    os.system("cd ../../")
    os.system("rm -r Phunisher_Framework")
    os.system("git clone https://github.com/amanraj-9077/Phunisher_Framework.git")

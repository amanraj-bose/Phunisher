#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from speak import say
from time import sleep
from colour import color as cl
from colour import bright as br
from sys import exit, stdout
from os import system
from urllib.request import urlopen
import urllib
from banner import banner4
from pkg_resources import get_distribution, DistributionNotFound
from subprocess import call

system("dos2unix gui_installation.py")

class Installer:
    def __init__(self) -> None:
        super().__init__()

    def flag(self) -> None:
        system("clear")
        self.sprint(f"""{br.white_1}
          ____________
        ! ____________!
        ! ____{br.blue_1} @ _____{br.white_1}!      
        ! ____________!
        !
        !
        !
        !


        {br.blue_1}0) <---                          [e] speak               {br.red_1}(9)Finish
        """)
        while True:
            self.finish = str(input(f"\n\n{br.cyan_1}Installer{br.red_1}@{br.magenta_1}Phunisher{br.yellow_1}${br.white_1}: {br.white_1}"))
            if self.finish == "exit":
                exit(0)
            elif self.finish == "e":
                say("Made in India")
            elif self.finish == "9":
                # system("sudo pyinstaller --onefile phf.py")
                self.sprint("""\n\033[1;34mPlease run on root, command for root access \033[1;32msudo su \033[1;34m\nand again run\033[1;31m cd ../ \033[1;33m./run.sh\033[1;34m for running Phunisher Framework\033[1;31m .....\033[1;37m""")
                exit(0)
                # Finish function
            elif self.finish == "0":
                self.creator_version()
            else:
                self.flag()


    def creator_version(self) -> None:
        system("clear")
        print(f"""
                {banner4}
{br.blue_1}
                Created By {br.red_1}Aman Raj {br.blue_1}
                Version ------> 0.1

        {br.green_1}Description =>\033[0m {cl.white} It is Madeup for Pentesters and Hackers.
        It is a Fully automatic Tool and it is very user freindly. we shall make many Variant.if are you giving 
        best feedback.if any glitches found on this tool please give me feedback on our website {br.red_1}https://phunisher.io \033[0m{cl.white}
        \n{br.red_1}Warning :\033[0m{cl.yellow}This Tool use on your risk\033[0m 

        {br.blue_1}0) <---                          [e] speak               {br.red_1}--->(1
        """)
        while True:
            self.install_step3 = str(input(f"\n\n{br.cyan_1}Installer{br.red_1}@{br.magenta_1}Phunisher{br.yellow_1}${br.white_1}: {br.white_1}"))
            if self.install_step3 == "exit":
                exit(0)
            elif self.install_step3 == "e":
                say("""
                                Created By Aman Raj
                Version 0.1

        Description It is Madeup for Pentesters and Hackers.
        It is a Fully automatic Tool and it is very user freindly. we shall make many Variant.if are you giving 
        best feedback.if any glitches found on this tool please give me feedback on our website https://phunisher.io
        Warning This Tool use on your risk
                """)
            elif self.install_step3 == "1" or self.install_step3 == "01":
                self.flag()
            elif self.install_step3 == "0":
                self.License_Copyright()
            else:
                self.creator_version()

    def License_Copyright(self) -> None:
        system("clear")
        print(f'''{br.red_1}
                                Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/\033[0m{cl.white}
                        
TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

1.  Definitions.

    "License" shall mean the terms and conditions for use, reproduction,
    and distribution as defined by Sections 1 through 9 of this document.

    "Licensor" shall mean the copyright owner or entity authorized by
    the copyright owner that is granting the License.

    "Legal Entity" shall mean the union of the acting entity and all
    other entities that control, are controlled by, or are under common
    control with that entity. For the purposes of this definition,
    "control" means (i) the power, direct or indirect, to cause the
    direction or management of such entity, whether by contract or
    otherwise, or (ii) ownership of fifty percent (50%) or more of the
    outstanding shares, or (iii) beneficial ownership of such entity.

    "You" (or "Your") shall mean an individual or Legal Entity
    exercising permissions granted by this License.

    "Source" form shall mean the preferred form for making modifications,
    including but not limited to software source code, documentation
    source, and configuration files.

    "Object" form shall mean any form resulting from mechanical
    transformation or translation of a Source form, including but
    not limited to compiled object code, generated documentation,
    and conversions to other media types.

    "Work" shall mean the work of authorship, whether in Source or
    Object form, made available under the License, as indicated by a
    copyright notice that is included in or attached to the work
    (an example is provided in the Appendix below).

    "Derivative Works" shall mean any work, whether in Source or Object
    form, that is based on (or derived from) the Work and for which the
    editorial revisions, annotations, elaborations, or other modifications
    represent, as a whole, an original work of authorship. For the purposes
    of this License, Derivative Works shall not include works that remain
    separable from, or merely link (or bind by name) to the interfaces of,
    the Work and Derivative Works thereof.

    "Contribution" shall mean any work of authorship, including
    the original version of the Work and any modifications or additions
    to that Work or Derivative Works thereof, that is intentionally
    submitted to Licensor for inclusion in the Work by the copyright owner
    or by an individual or Legal Entity authorized to submit on behalf of
    the copyright owner. For the purposes of this definition, "submitted"
    means any form of electronic, verbal, or written communication sent
    to the Licensor or its representatives, including but not limited to
    communication on electronic mailing lists, source code control systems,
    and issue tracking systems that are managed by, or on behalf of, the
    Licensor for the purpose of discussing and improving the Work, but
    excluding communication that is conspicuously marked or otherwise
    designated in writing by the copyright owner as "Not a Contribution."

    "Contributor" shall mean Licensor and any individual or Legal Entity
    on behalf of whom a Contribution has been received by Licensor and
    subsequently incorporated within the Work.

2.  Grant of Copyright License. Subject to the terms and conditions of
    this License, each Contributor hereby grants to You a perpetual,
    worldwide, non-exclusive, no-charge, royalty-free, irrevocable
    copyright license to reproduce, prepare Derivative Works of,
    publicly display, publicly perform, sublicense, and distribute the
    Work and such Derivative Works in Source or Object form.

3.  Grant of Patent License. Subject to the terms and conditions of
    this License, each Contributor hereby grants to You a perpetual,
    worldwide, non-exclusive, no-charge, royalty-free, irrevocable
    (except as stated in this section) patent license to make, have made,
    use, offer to sell, sell, import, and otherwise transfer the Work,
    where such license applies only to those patent claims licensable
    by such Contributor that are necessarily infringed by their
    Contribution(s) alone or by combination of their Contribution(s)
    with the Work to which such Contribution(s) was submitted. If You
    institute patent litigation against any entity (including a
    cross-claim or counterclaim in a lawsuit) alleging that the Work
    or a Contribution incorporated within the Work constitutes direct
    or contributory patent infringement, then any patent licenses
    granted to You under this License for that Work shall terminate
    as of the date such litigation is filed.

4.  Redistribution. You may reproduce and distribute copies of the
    Work or Derivative Works thereof in any medium, with or without
    modifications, and in Source or Object form, provided that You
    meet the following conditions:

    (a) You must give any other recipients of the Work or
    Derivative Works a copy of this License; and

    (b) You must cause any modified files to carry prominent notices
    stating that You changed the files; and

    (c) You must retain, in the Source form of any Derivative Works
    that You distribute, all copyright, patent, trademark, and
    attribution notices from the Source form of the Work,
    excluding those notices that do not pertain to any part of
    the Derivative Works; and

    (d) If the Work includes a "NOTICE" text file as part of its
    distribution, then any Derivative Works that You distribute must
    include a readable copy of the attribution notices contained
    within such NOTICE file, excluding those notices that do not
    pertain to any part of the Derivative Works, in at least one
    of the following places: within a NOTICE text file distributed
    as part of the Derivative Works; within the Source form or
    documentation, if provided along with the Derivative Works; or,
    within a display generated by the Derivative Works, if and
    wherever such third-party notices normally appear. The contents
    of the NOTICE file are for informational purposes only and
    do not modify the License. You may add Your own attribution
    notices within Derivative Works that You distribute, alongside
    or as an addendum to the NOTICE text from the Work, provided
    that such additional attribution notices cannot be construed
    as modifying the License.

    You may add Your own copyright statement to Your modifications and
    may provide additional or different license terms and conditions
    for use, reproduction, or distribution of Your modifications, or
    for any such Derivative Works as a whole, provided Your use,
    reproduction, and distribution of the Work otherwise complies with
    the conditions stated in this License.

5.  Submission of Contributions. Unless You explicitly state otherwise,
    any Contribution intentionally submitted for inclusion in the Work
    by You to the Licensor shall be under the terms and conditions of
    this License, without any additional terms or conditions.
    Notwithstanding the above, nothing herein shall supersede or modify
    the terms of any separate license agreement you may have executed
    with Licensor regarding such Contributions.

6.  Trademarks. This License does not grant permission to use the trade
    names, trademarks, service marks, or product names of the Licensor,
    except as required for reasonable and customary use in describing the
    origin of the Work and reproducing the content of the NOTICE file.

7.  Disclaimer of Warranty. Unless required by applicable law or
    agreed to in writing, Licensor provides the Work (and each
    Contributor provides its Contributions) on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
    implied, including, without limitation, any warranties or conditions
    of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
    PARTICULAR PURPOSE. You are solely responsible for determining the
    appropriateness of using or redistributing the Work and assume any
    risks associated with Your exercise of permissions under this License.

8.  Limitation of Liability. In no event and under no legal theory,
    whether in tort (including negligence), contract, or otherwise,
    unless required by applicable law (such as deliberate and grossly
    negligent acts) or agreed to in writing, shall any Contributor be
    liable to You for damages, including any direct, indirect, special,
    incidental, or consequential damages of any character arising as a
    result of this License or out of the use or inability to use the
    Work (including but not limited to damages for loss of goodwill,
    work stoppage, computer failure or malfunction, or any and all
    other commercial damages or losses), even if such Contributor
    has been advised of the possibility of such damages.

9.  Accepting Warranty or Additional Liability. While redistributing
    the Work or Derivative Works thereof, You may choose to offer,
    and charge a fee for, acceptance of support, warranty, indemnity,
    or other liability obligations and/or rights consistent with this
    License. However, in accepting such obligations, You may act only
    on Your own behalf and on Your sole responsibility, not on behalf
    of any other Contributor, and only if You agree to indemnify,
    defend, and hold each Contributor harmless for any liability
    incurred by, or claims asserted against, such Contributor by reason
    of your accepting any such warranty or additional liability.

END OF TERMS AND CONDITIONS

{cl.red}APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "[]"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.
{cl.blue}
Copyright 2022 aman_raj,amanraj-9077 and others

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    {br.red_1}   http://www.apache.org/licenses/LICENSE-2.0\033[0m{cl.white}

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.  


{br.blue_1}0) <---                          [e] speak               {br.red_1}--->(1
        ''')
        while True:
            self.install_step2 = str(input(
                f"\n\n{br.cyan_1}Installer{br.red_1}@{br.magenta_1}Phunisher{br.yellow_1}${br.white_1}: {br.white_1}"))
            if self.install_step2 == "e":
                say("""
                Copyright 2022 aman_raj,amanraj-9077 and others

Licensed under the Apache License, Version 2.0 (the "License")
you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
                """)
            elif self.install_step2 == "1" or self.install_step2 == "01":
                self.creator_version()
            elif self.install_step2 == "0":
                self.Install_1()
            elif self.install_step2 == "exit":
                exit(0)
            else:
                self.License_Copyright()

    def sprint(self, text) -> str:
        for words in text + '\n':
            stdout.write(words)
            stdout.flush()
            sleep(0.01)

    def Install_1(self) -> None:
        system("clear")
        print(f"""
        {br.cyan_1}   _                       _   _            
        {br.magenta_1}  | |                     | | | |           
        {br.green_1}  | | _  _    , _|_  __,  | | | |  _   ,_   
        {br.yellow_1}_ |/ / |/ |  / \_|  /  |  |/  |/  |/  /  |  
        {br.red_1}\_/\/  |  |_/ \/ |_/\_/|_/|__/|__/|__/   |_/
        {br.blue_1}
        {br.white_1}
        
        {br.red_1}[1] Packages          {br.cyan_1}[2] Module            {br.green_1}[3] ===> {br.blue_1}

        {br.white_1}99) <---(Back)
        """)
        while True:
            self.input_step_1 = str(input(
                f"\n\n{br.cyan_1}Installer{br.red_1}@{br.magenta_1}Phunisher{br.yellow_1}${br.white_1}: {br.white_1}"))
            if self.input_step_1 == "1" or self.input_step_1 == "01":
                self.interface_main()
                system(
                    'xterm -T "☢ INSTALL PYTHON3 ☢" -geometry 100x30 -e "sudo apt-get install python3 -y"')
                self.sprint(
                            f"{cl.blue}[{cl.green}+{cl.blue}] {cl.cyan}Package is Updated {cl.green} --> {cl.magenta}Python")
                system(
                    'xterm -T "☢ INSTALL PYTHON3 ☢" -geometry 100x30 -e "sudo apt-get install python3-pip -y"')
                self.sprint(
                            f"{cl.blue}[{cl.green}+{cl.blue}] {cl.cyan}Package is Updated {cl.green} --> {cl.magenta}preferred installer program(PIP)")
                system(
                    'xterm -T "☢ INSTALL C++ ☢" -geometry 100x30 -e "sudo apt-get install g++ -y"')
                self.sprint(
                            f"{cl.blue}[{cl.green}+{cl.blue}] {cl.cyan}Package is Updated {cl.green} --> {cl.magenta}G++ Compiler")
                system(
                    'xterm -T "☢ INSTALL C++ ☢" -geometry 100x30 -e "sudo apt-get install build-essential -y"')
                self.sprint(
                            f"{cl.blue}[{cl.green}+{cl.blue}] {cl.cyan}Package is Updated {cl.green} --> {cl.magenta}Build Essential")                
                system(
                    'xterm -T "☢ INSTALL Ruby ☢" -geometry 100x30 -e "sudo apt-get install ruby -y"')
                self.sprint(
                            f"{cl.blue}[{cl.green}+{cl.blue}] {cl.cyan}Package is Updated {cl.green} --> {cl.magenta}Ruby")  
            elif self.input_step_1 == "2" or self.input_step_1 == "02":
                self.interface_main()
                for modules in ['requests', 'halo', 'numpy', 'beautifulsoup4', 'pynput', 'PySocks', 'requests-futures', 'certifi', 'stem', 'torrequest', 'GitPython', 'keyboard', 'rarfile', 'pandas', 'pandas-profiling']:
                    try:
                        dist = get_distribution(modules)
                        self.sprint(
                            f"{cl.blue}[{cl.green}+{cl.blue}] {cl.cyan}Module is Found {cl.green} --> {dist.key}{cl.magenta}({dist.version})")
                    except DistributionNotFound and KeyboardInterrupt and Exception:
                        self.sprint(
                            f"{cl.red}[{cl.yellow}-{cl.red}] {cl.red}Module is not Found --> {cl.blue}{modules} ")
                        for installed in ['requests', 'halo', 'numpy', 'beautifulsoup4', 'pynput', 'PySocks', 'requests-futures', 'certifi', 'stem', 'torrequest', 'GitPython', 'keyboard', 'rarfile','pandas', 'pandas-profiling']:
                            call(['pip3', 'install', installed])
            elif self.input_step_1 == "3" or self.input_step_1 == "03":
                sleep(0.2)
                self.License_Copyright()
            elif self.input_step_1 == "99":
                self.interface_main_banner()
            elif self.input_step_1 == "exit":
                exit(0)
            else:
                self.Install_1()

    def interface_main_banner(self) -> None:
        system("chmod +x ../__init__.py")
        system("chmod +x ../run.sh")
        system("chmod +x ../script.sh")
        system("clear")
        self.sprint(f"""
        {br.cyan_1}   _                       _   _            
        {br.magenta_1}  | |                     | | | |           
        {br.green_1}  | | _  _    , _|_  __,  | | | |  _   ,_   
        {br.yellow_1}_ |/ / |/ |  / \_|  /  |  |/  |/  |/  /  |  
        {br.red_1}\_/\/  |  |_/ \/ |_/\_/|_/|__/|__/|__/   |_/
        {br.blue_1}
        {br.white_1}
        {br.red_1}[{br.yellow_1}1{br.red_1}] {br.yellow_1}Install {br.green_1}[Recommded]

        {br.white_1}99) Exit              [0]About
        """)
        while True:
            self.input = str(input(
            f"\n\n{br.cyan_1}Installer{br.red_1}@{br.magenta_1}Phunisher{br.yellow_1}${br.white_1}: {br.white_1}"))
            if self.input == "1" or self.input == "01":
                self.Install_1()
            elif self.input == "99":
                exit(0)
            elif self.input == "0":
                print(f"""{br.blue_1}Please go to my official website for more.
if any troubleshoot in this tool please give me feed back on {br.green_1}https://phunisher.io""")
            else:
                print()
    def internet(self) -> None:
        try:
            urlopen("https://www.google.com/",  timeout=5)
            return True
        except urllib.error.URLError:
            return False

    def interface_main(self) -> None:
        if self.internet():
            self.sprint(
                f"{br.red_1}[{br.yellow_1}*{br.red_1}] {br.yellow_1}Checking Your Internet")
            self.sprint(
                f"{br.blue_1}[{br.cyan_1}*{br.blue_1}] {br.green_1}Your Internet Connection Available\n")
        else:
            self.sprint(
                f"{br.red_1}[{br.yellow_1}*{br.red_1}] {br.yellow_1}Checking Your Internet")
            self.sprint(
                f"{br.red_1}[{br.yellow_1}*{br.red_1}] {br.red_1}Your Internet Connection Unavailable\n")
            exit(0)

if __name__ == '__main__':
    try:
        classes = Installer()
        classes.interface_main_banner()
    except KeyboardInterrupt and Exception:
        system("clear")
        print("")

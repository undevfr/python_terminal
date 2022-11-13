#version 1.01
import os
import shlex
from datetime import datetime
credit_msg = "hackxx Terminal :) version 1.01\ntype help to display  all commands\nBe careful ! this terminal is case sensitive , always print commands with lowercases letters"
username = "Mathias"

if os.getenv('COMPUTERNAME') == None:
    machine = "localhost"
else:
    machine = os.getenv('COMPUTERNAME')

help_msg = (
"AVALIABLES COMMANDS:\n"
"cd : change directory\n"
"clear : erase all terminal text\n"
"credit : display welcome message\n"
"date : display date and time\n"
"echo : display text\n"
"exit : quit terminal\n"
"help : get this menu\n"
"ls : display all files/folders on current directory\n"
"pwd : display current directory\n"
"shutdown : not avaliable now :/\n"
)

print(credit_msg)

while True:
    path = os.getcwd()
    cmd = input(f"{username}@{machine}:{path}$ ")
    cmd = shlex.split(cmd)
    match cmd[0]:
        case "cd":
            os.chdir(cmd[1])

        case "clear" | "cls":
            os.system("clear")

        case "date":
            now = datetime.now()
            print(now.strftime("%B %d, %Y %H:%M:%S"))

        case "credit":
            print(credit_msg)

        case "echo":
            print(' '.join(cmd[1:] or []))

        case "exit":
            print("exit successfully!")

        case "help":
            print(help_msg)

        case "ls":
            for i in os.listdir():
                print(i)

        case "pwd":
            print(path)
        case "shutdown":
            print("Not avaliable now :/")
        case _:
            print(f"{cmd[0]}: command not found")

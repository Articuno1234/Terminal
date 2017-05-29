import random
import os
import sys
import argparse
import subprocess

IS_WINDOWS = os.name == "nt"
IS_MAC = sys.platform == "darwin"
INTERACTIVE_MODE = not len(sys.argv) > 1  # CLI flags = non-interactive
def ver():
    subprocess.call(["uname", "-a"])
    wait()
    menu()
def ver(help):
    print("Shows the version of the pc you are using")
    wait()
    menu()
def sudo():
    subprocess.call(["sudo"])
    wait()
    menu()
def help():
    clear_screen()
    print("list of commands\n"
          "\n"
          "help [args]\n"
          "ver")
    wait()
    menu()
def menu():
    clear_screen()
    choice = user_choice()
    if choice == "help":
        help()
    if choice == "ver":
        ver()
    if choice == "help ver":
        ver(help)
    if choice == "sudo":
        sudo()

def clear_screen():
    if IS_WINDOWS:
        os.system("cls")
    else:
        os.system("clear")
        
def user_choice():
    return input("Terminal:~ $ ").lower().strip()

def wait():
    if INTERACTIVE_MODE:
        input("Press enter to continue.")

menu = menu()
print(menu)
    

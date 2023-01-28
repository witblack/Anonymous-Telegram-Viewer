#!/bin/python3
# coding: utf-8

try:
    from termcolor import colored
    from requests import get
    from time import sleep
    from os import remove
    from sys import exit
    import webbrowser
except ModuleNotFoundError:
    print("Some depends not installed. Run 'pip3 install requires.txt'")
else:
    # Ask
    ID = input("Please enter ID of Channel/Profile: ")

    # Get
    URL = "https://t.me/" + ID
    Request = get(URL)
    if Request.status_code == 404:
        print(colored("[!] Error:", "red"))
        print(colored("[-] Channel or profile not exists.", "red"))
    else:
        File = open("./Result.htm", "w")
        File.write(Request.text)
        File.close()
    # open content
    webbrowser.open("./Result.htm", new=2)

    # Clear and finish
    print(colored("[+] ", "green") + colored("Press enter for exit and delete tmp files.", "white"))
    input()
    try:
        remove("./Result.htm")
    except:
        pass
#!/usr/bin/python
# coding: utf-8
#💬 Telegram:
#Https://t.me/WitBlack_ch
#
#💻 Web:
#Https://BugZone.ir
#
#📹 YouTube:
#https://www.youtube.com/channel/UCIgk2ldVeelyaHW3s4UkIIg (WitBlack)
#
#🎥 Aparat:
#Https://aparat.com/WitBlack
#
#⌨️ Github:
#Https://github.com/WitBlack
#
#📧 E-Mail:
#admin@bugzone.ir💬 Telegram:
#Https://t.me/WitBlack_ch
#
#💻 Web:
#Https://BugZone.ir
#
#📹 YouTube:
#https://www.youtube.com/channel/UCIgk2ldVeelyaHW3s4UkIIg (WitBlack)
#
#🎥 Aparat:
#Https://aparat.com/WitBlack
#
#⌨️ Github:
#Https://github.com/WitBlack
#
#📧 E-Mail:
#admin@bugzone.ir
#Powered By WitBlack Hacker
#Version 1.0.3 - Meli Code Generator
#
#💬 Telegram:
#Https://t.me/WitBlack_ch
#
#💻 Web:
#Https://BugZone.ir
#
#📹 YouTube:
#https://www.youtube.com/channel/UCIgk2ldVeelyaHW3s4UkIIg (WitBlack)
#
#🎥 Aparat:
#Https://aparat.com/WitBlack
#
#⌨️ Github:
#Https://github.com/WitBlack
#
#📧 E-Mail:
#admin@bugzone.ir
#
try:
	from time import sleep
	from string import lower
	import os
	from termcolor import colored
except:
	print('Some deepends not installed!')
	exit(1)
if os.path.exists('/tmp'):
        OS = 'Linux'
elif os.path.exists('C:/'):
        OS = 'Windows'
else:
        print(colored("Your operation system don't suport! :(","red"))
        exit(1)
def Clear():
	if OS == 'Linux':
		os.system('clear')
	else:
		os.system('cls')
def Banner():
	Clear()
	print(colored(' __     __     __      __        __         ','magenta') + colored('|','red') + colored(' Anonymous Telegram Viewer','cyan'))
	print(colored('/\ \   /\ \   /\ \    /\_\      /\ \        ','magenta') + colored('|','red') + colored(' _-_-_-_-_-_-_-_-_-_-_-_','green'))
	print(colored('\ \ \  \ \ \  \ \ \   \/_/     _\_\_\____   ','magenta') + colored('|','red'))
	print(colored(' \ \ \  \ \ \  \ \ \     __   /\_________\  ','magenta') + colored('|','red') + 'Web Site:')
	print(colored('  \ \ \  \ \ \  \ \ \   /\ \  \/___/\ \__/  ','magenta') + colored('|','red') + '	- Https://BugZone.ir')
	print(colored('   \ \ \__\_\ \__\_\ \  \ \ \      \ \ \    ','magenta') + colored('|','red') + 'Email:')
	print(colored('    \ \_____________\_\  \ \_\      \ \_\   ','magenta') + colored('|','red') + '	- admin@bugzone.ir')
	print(colored('     \/_______________/   \/_/       \/_/   ','magenta') + colored('|_____________________________','red') + "\n")
	print(colored(' ________     __     _________     ____________      __','magenta'))
	print(colored('/\  ____ \   /\ \   /\  _____ \   /\  ________/\    /\ \    __','magenta'))
	print(colored('\ \ \__/\ \  \ \ \  \ \_\___/\ \  \ \ \______/\ \   \ \ \  / /\\','magenta'))
	print(colored(' \ \ \_\_\ \  \ \ \  \/_/___\_\ \  \ \ \     \/_/__  \ \ \/ / /','magenta'))
	print(colored('  \ \  ____ \  \ \ \   /\  _____ \  \ \ \       /\ \  \ \ \/_/____ ','magenta'))
	print(colored('   \ \ \__/\ \  \ \ \  \ \ \___/\ \  \ \ \      \ \ \  \ \  ___ \ \\','magenta'))
	print(colored('    \ \ \_\_\ \  \ \ \  \ \ \__\_\ \  \ \ \______\/  \  \ \ \  \ \ \\','magenta'))
	print(colored('     \ \_______\  \ \_\  \ \________\  \ \___________/   \ \_\  \ \_\\','magenta'))
	print(colored('      \/_______/   \/_/   \/________/   \/__________/     \/_/   \/_/','magenta'))
	print("\nProgramed By WitBlack HAcker. - Git ~> Https://GitHub.com/WitBlack")
	print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
	print(colored("Let's Good! Enjoy.",'yellow'))
	print(colored("VERSION ",'blue') + colored("1.0.1",'white'))
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n")
Banner()
ID = raw_input(colored("e.g:	WitBlack_ch\nEnter channel ID without '@': ","white"))
Banner()
Type = raw_input(colored("It's channel or just a profile [p/c] 0? ",'white'))
if str.lower(Type) == 'c' or str.lower(Type) == 'channel':
	print colored('Selected type => channel')
	Type = 'Channel'
else:
	print colored('Selected type => profile')
	Type = 'Profile'

if Type == 'Channel':
	try:
		Post_number = int(raw_input(colored("Enter Number of post: ( You can enter empty): ","white")))
	except:
		print(colored('Number is invalid or use empty. use 9999999 number. Wite to continue..','white'))
 		Post_number = 9999999
		sleep(3)

if Type == 'channel':
	Link = "https://t.me/" + ID + "/" + str(Post_number)
else:
	Link = "https://t.me/" + ID + "/"
Banner()
print(colored("If you want see all posts. open URL and click on 'Preview channel'.","white"))
print(colored("\nOpen: " + Link ,'yellow'))
Choose = raw_input(colored("Open automatically [y/n] ? ","white"))
if lower(Choose) == 'y' or lower(Choose) == 'yes':
	Choose = raw_input("firefox or chrome [f/c] ? ")
	if lower(Choose) == 'chrome' or lower(Choose) == 'c':
		os.system("chrome " + Link)
	else:
		os.system("firefox " + Link)

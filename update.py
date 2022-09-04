#!/bin/python3
import os



def main():


    print("----------")
    print("[*] Upgrading...")
    os.system("sudo apt upgrade")



    print("-----------")
    print("[*] Updating...")
    os.system("sudo apt update")



    print("-----------")
    print("[*] Cleaning...")
    os.system("sudo apt autoremove")

    print("-----------")
    print("[*] Upgrading...")
    os.system("sudo apt upgrade")

    

    print("-----------")
    print("[*] Updating...")
    os.system("sudo apt update")



    print("-----------")
    print("[*] Cleaning...")
    os.system("sudo apt autoremove")




if __name__ == "__main__":
    
    usr_id = int(os.getuid())

    if usr_id == 0:
        main()
    else:
        print("[*] Root access is required, quiting✌ ... ")


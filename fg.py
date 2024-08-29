#!/usr/env python3

import random
import string

PURPLE = '\033[95m'
CYAN = '\033[96m'
BLUE = "\033[94m"
GREEN = "\033[92m"
RED = "\033[91m"
ENDC = "\033[0m"

CTFname="CTF"

def banner():
    banner = f"""
{PURPLE}
       ___ _____ ___   ___ _                ___                       _           
      / __|_   _| __| | __| |__ _ __ _ ___ / __|___ _ _  ___ _ _ __ _| |_ ___ _ _ 
     | (__  | | | _|  | _|| / _` / _` |___| (_ / -_) ' \/ -_) '_/ _` |  _/ _ \ '_|
      \___| |_| |_|   |_| |_\__,_\__, |    \___\___|_||_\___|_| \__,_|\__\___/_|  
                                 |___/   {ENDC}
"""
    print(banner)

def options():
    options = f"""
    {RED}Dont forget to change the ctf name if needed{ENDC}
    {CYAN}
    [1]. Generate leet flags from text.
    [2]. Gneerate  random hex flags.
    [3]. Exit.{ENDC}
    """
    print(options)
    while True:
        choice = input(f"{PURPLE}>>{ENDC} ")
        if choice in ['1', '2','3']:
            return int(choice)
        else:
            print("Invalid choice")


def rand():
    randoms = []
    for i in range(5): 
        f = ''.join(random.choices(string.ascii_lowercase + string.digits, k = 10)) #change the K value according to the flag length you want
        randoms.append(wrap(f))
    return randoms

def leet():
    while True:
        text = input(f"What's your content? \n{PURPLE}>>{ENDC} ").strip()
        valid = set(string.ascii_letters + string.digits + '!' + '?' +' ') #no special chars except '?' and '!'
        
        if any(char not in valid for char in text):
            print("Invalid content, please use only letters, numbers, '?' and '!'")
            continue

        text = '_'.join(text.split())

        leet_dict = {
            'a': ['4', '@', 'q', 'ɐ'],
            'b': ['8', 'B', 'b'],
            'c': ['c', 'Ⓒ', 'C'],
            'd': ['d', 'D'],
            'e': ['3', '€'],
            'i': ['1', '|'],
            'l': ['L', 'l'],
            'o': ['0', '*', '¤'],
            'r': ['2', 'R', 'ɹ'],
            's': ['$', '5'],
            't': ['7', '†'],
        }

        leets = set()

        while len(leets) < 5:
            enc = ''.join(
                random.choice(leet_dict[char.lower()]) if char.lower() in leet_dict else char
                for char in text
            )
            leets.add(wrap(enc))

        return list(leets)


def wrap(content):
    return CTFname+"{"+content+"}"

def main():
    banner()
    while True:
        op=options()
        if op == 1 :
            flags=leet()
        elif op ==2:
            flags=rand()
        else:
            print("Bye :)")
            break
        print("Enjoy your flags: \n",flags)



if __name__ == "__main__":
    main()
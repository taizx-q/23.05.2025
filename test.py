from random import randint
from colorama import Fore
import threading
import time

elapsed_time = 0  #global

def timer():
    global elapsed_time
    start_time = time.time()
    while True:
        elapsed_time = time.time() - start_time
        time.sleep(1)

def generate():
    global elapsed_time
    while True:
        new = randint(1, 10)
        answer = input("Meģini izminēt, tas ir skaitlis ... ")

        print(f"Programma darbojas {elapsed_time:.2f} sekundes.")

        if not answer.strip():
            print("Nevar atstāt tukšu atbildi!")
            continue

        if answer.lower() == "exit":
            print("Tad beidzām...")
            break

        try:
            if int(answer) == new:
                print(f"{Fore.LIGHTGREEN_EX}Pareizi!{Fore.RESET} Ja gribēs iziet, uzspiež {Fore.CYAN}CTRL + C vai ievadi 'exit'{Fore.RESET}, nākamais skaitlis ir ...")
            else:
                print(f"{Fore.LIGHTRED_EX}Diemžēl{Fore.RESET}, nesanāca. Ja gribēs iziet, uzspiež {Fore.CYAN}CTRL + C vai ievadi 'exit'{Fore.RESET}. Turpinām!")
        except ValueError:
            print("Ievadi derīgu skaitli vai 'exit'!")
    
# Start
vards = input("Ievadi savu vārdu >> ")
print(f"Sveiki, {vards}! Man tev ir viena spēle – jāuzmin skaitlis, kuru es iedomājos (no 1 līdz 10).\nLai sāktu, ievadi 'y' vai 'Y'")
start_choice = input(">> ")
if start_choice.lower() == "y":
    timer_thread = threading.Thread(target=timer)
    timer_thread.daemon = True
    timer_thread.start()
    generate()
else:
    print("Tad beidzam...")

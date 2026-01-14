import webbrowser
from datetime import datetime
import os
# from difflib import get_close_matches


while True:
    print("Hello , how may i help you.")
    command = input("Enter command : ").lower()

    if (command == "youtube"):
        webbrowser.open("https://www.youtube.com/")
    elif (command.startswith("search")):
        search = command.replace("search" , "").strip()
        webbrowser.open(f"https://www.google.com/search?q={search}")
    elif (command.startswith("play")):
        play = command.replace("play" , "").strip()
        webbrowser.open(f"https://www.youtube.com/results?search_query={play}")
    elif(command == "google"):
        webbrowser.open("https://www.google.com/")
    elif(command == "github"):
        webbrowser.open("https://github.com/")
    elif(command == "time"):
        now = datetime.now().strftime("%I:%M:%P")
        print("time:" , now)
    elif(command == "date"):
        today = datetime.now().strftime("%d-%m-%Y")
        print("Date:" , today)
    elif (command == "calc"):
        os.system("gnome-calculator")
    elif(command == "editor"):
        os.system("gedit")
    elif(command == "help"):
        print("commands : youtube , goggle , github , search<___> , play<___>")
        print("time , date , calc(calculator), editor ")
    elif(command== "exit"):
        print("Thank you, Good bye")
        break
    if not command.strip():
        print("please type something or help for user guide...")
        continue
    else:
        print("unkown command")
    print("type exit for exit or continue , thank you ")



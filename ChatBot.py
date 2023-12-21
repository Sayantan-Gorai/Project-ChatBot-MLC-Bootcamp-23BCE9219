from datetime import datetime
a = input("Enter your name: ")
print("what's up! "+a)
b = ""
while("exit" or "quit" not in b):
    b = input("How can i help you?\n")
    if("hello" in b):
        print("Hiya back!")
    elif ('fine' in b):
        print("It sounds well! I am awesome!\n")
    elif ('name' in b):
        print("I'm your AI. You can change my name.")
    elif ('call' in b):
        print("It's a good name!")
    elif ('doing' in b):
        print("Nothing!")
    elif('time' in b):
        print("The date & time is: ",datetime.now())
    elif('mood' in b):
        print("Go for a walk or listen good songs!")
    elif ('made' in b):
        print("Mr."+a)
    elif( '69' in b):
        print("It's a very dangerous number!\n")
    elif ('tired' in b):
        print("Lol go to bed!\n")
    elif ('fuck' in b):
        print("What happened to you!\n")
    elif ('happy' in b):
        print("Nice to hear that!\n")
    elif ('eat' in b):
        print("Your data")
    elif ('thirsty' in b):
        print("Lol drink water!")
    elif ('hungry' in b):
        print("Lol eat something!")
    elif ('exit'.lower() or 'quit'.lower() in b):
        break
    else:
        print("Sorry, I can't understand that!")


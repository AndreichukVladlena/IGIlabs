from DataBase import DataBase

username = input("Enter your username: ")
answer = ''
status = "start"
db = DataBase()
while True:
    if status == "start":
        if not db.user_exists(username):
            db.add_user(username)
        status = "autorized"
        answer = input("Enter an action(add, remove, find, grep, switch, save, load, list, exit):")

    if status == "autorized":
        if answer.lstrip()[:3] == "add":
            db.add_item(username, answer.strip()[3:].strip())
            answer = input("Enter an action(add, remove, find, grep, switch, save, load, list, exit):")
        elif answer.lstrip()[:6] == "remove":
            db.remove_item(username, answer.strip()[6:].strip())
            answer = input("Enter an action(add, remove, find, grep, switch, save, load, list, exit):")
        elif answer.lstrip()[:4] == "find":
            db.find_item(username, answer.strip()[4:].strip())
            answer = input("Enter an action(add, remove, find, grep, switch, save, load, list, exit):")
        elif answer.lstrip()[:4] == "grep":
            db.grep_item(username, answer.strip()[4:].strip())
            answer = input("Enter an action(add, remove, find, grep, switch, save, load, list, exit):")
        elif answer.lstrip()[:4] == "load":
            db.load(username)
            answer = input("Enter an action(add, remove, find, grep, switch, save, load, list, exit):")
        elif answer.lstrip()[:4] == "save":
            db.save()
            answer = input("Enter an action(add, remove, find, grep, switch, save, load, list, exit):")
        elif answer.lstrip()[:4] == "list":
            print(db.dict_to_list(username))
            answer = input("Enter an action(add, remove, find, grep, switch, save, load, list, exit):")
        elif answer.lstrip()[:6] == "switch":
            answer = input("Would you like to save?(y/n)")
            if answer == "y" or answer == "Y":
                db.save()
                status = "start"
                username = input("Enter username to switch:")
            elif answer == "n" or answer == "N":
                status = "start"
                username = input("Enter username to switch:")
            else:
                print("Incorrect input!")
                answer = input("Enter an action(add, remove, find, grep, switch, save, load, list):")
        elif answer.lstrip()[:4] == "exit":
            break
        else:
            print("Incorrect input!")
            answer = input("Enter an action(add, remove, find, grep, switch, save, load, list):")
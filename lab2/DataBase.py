from distributions import MySet
import json
class DataBase():
    def __init__(self):
        self.dict_db = {}

    def add_user(self, name):
        self.dict_db[name] = MySet()

    def user_exists(self, name):
        for key in self.dict_db.keys():
            if key == name:
                return True
        return False

    def add_item(self, name, key):
        if key == "":
            print("Value field is empty!")
        else:
            self.dict_db[name].add(key)

    def remove_item(self, name, val):
        flag = False
        for item in self.dict_db[name]:
            if item == val:
                flag = True
        if flag:
            self.dict_db[name].remove(val)
        else:
            print("No such element!")


    def find_item(self, name, key):
        return self.dict_db[name].find(key)

    def grep_item(self, name, regex):
        return self.dict_db[name].grep(regex)

    def dict_to_list(self, name):
        return self.dict_db[name].to_list()

    def save(self):
        new_dict={}
        for key in self.dict_db.keys():
           new_dict[key] = self.dict_to_list(key)
        with open("db.json", "w") as file:
            json.dump(new_dict, file)

    def load(self, name):
        new_dict = {}
        with open("db.json", "r") as file:
            new_dict = json.load(file)
        for key in new_dict.keys():
            if key == name:
                self.dict_db[name].update(MySet(new_dict[key]))
                return True
        return False

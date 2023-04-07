import re
from typing import Set


class MySet (Set):
    def __init__(self, elements=()):
        super().__init__(elements)

    def find(self, key):
        for item in self:
            if item == key:
                return item
        return "No such elements"

    def to_list(self):
        result_list = []
        for item in self:
            result_list.append(item)
        return result_list

    def grep(self, regex):
        result = []
        for item in self:
            if re.findall(regex, item):
                result.append(item)
        return result

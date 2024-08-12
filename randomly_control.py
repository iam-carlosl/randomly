import math
import random

class RlyController:

    def __init__(self):
        self.last_result = None

    def result_size(self):
        result_size = 40
        if self.last_result is not None and len(str(self.last_result)) > 8:
            for i in range(8, len(str(self.last_result)), 3):
                result_size -= 4
                if result_size < 12:
                    break
        return result_size

class RlyNumbersController(RlyController):

    def __init__(self):
        super().__init__()
        self.min_limit = 0
        self.max_limit = 100

    def generate_result(self, limit_1:int, limit_2:int):

        self.min_limit = min(limit_1, limit_2)
        self.max_limit = max(limit_1, limit_2)
        self.last_result = random.randint(a=self.min_limit, b=self.max_limit)
        return self.last_result

class RlyChoicesController(RlyController):

    def __init__(self):
        super().__init__()
        self.choices:list[str] = []
        self.choices_listed = False

    def generate_result(self, filter:str=None):

        if filter is not None:
            tmp_choices = [choice for choice in self.choices if choice.startswith(filter)]
            if tmp_choices:
                self.last_result = random.choice(tmp_choices)
        else:
            if self.choices:
                self.last_result = random.choice(self.choices)
        return self.last_result
    
    def add_choice(self, choice:str):
        if choice and not choice in self.choices:
            self.choices = self.choices + [choice]
            return True
        return False

    def add_choices(self, choices:list[str]):
        new_choices = [choice.replace("\n","") for choice in choices if choice not in self.choices]
        self.choices = self.choices + new_choices
    
    def edit_choice(self, old:str, new:str):
        choice_index = self.choices.index(old)
        self.choices[choice_index] = new
    
    def remove_choice(self, choice:str):
        self.choices.remove(choice)

 

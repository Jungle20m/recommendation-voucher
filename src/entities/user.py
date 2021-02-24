


class User():
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age
        
    @classmethod
    def load_from_string(cls, text):
        id, name, age = text.split(" ")
        return cls(id, name, age)
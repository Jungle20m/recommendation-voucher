class Voucher():
    def __init__(self, id, name):
        self.id = id
        self.name = name
        
    @classmethod
    def load_from_string(cls, text):
        id, name = text.split(" ")
        return cls(id, name)
class Vehicle:
    id=0
    type=""
    max_passenger=3
    Ac=True
    size=7
    max_load=2500
    Available=True

    def __init__(self, id, type, max_passenger, Ac, size, max_load,Available):
        self.id=id
        self.type=type
        self.max_passenger=max_passenger
        self.Ac=Ac
        self.size=size
        self.max_load=max_load
        self.Available=Available

    def get_id(self):
        return self.id
    def get_type(self):
        return self.type
    def get_max_passenger(self):
        return self.max_passenger
    def get_Ac(self):
        return self.Ac
    def get_size(self):
        return self.size
    def get_max_load(self):
        return self.max_load
    def get_Available(self):
        return self.Available
    def set_Available(self):
        self.Available=False
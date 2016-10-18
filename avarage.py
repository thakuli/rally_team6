class Avarage():
    def __init__(self):
        self.values=-50
        self.prev1=-50
        self.prev2=-50
        self.prev3=-50

    def add(self, value):
        self.prev3=self.prev2
        self.prev2=self.prev1
        self.prev1=self.values
        self.values=value

    def get_avararage(self):

        return float(float(self.prev1) + float(self.prev2) + float(self.prev3) + float(self.values)) / 4
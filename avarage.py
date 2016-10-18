
MAX_ITEMS=5

class Average():
    def __init__(self):
        self.nums = []

    def add(self, num):
        self.nums.append(num)
        if len(self.nums) == MAX_ITEMS:
            self.nums.pop(0)
        
    def average(self):
        return reduce(lambda x,y: x+y, self.nums)/len(self.nums)


def testi():
    avg = Average()
    avg.add(10)
    avg.add(20)
    avg.add(30)
    avg.add(40)
    avg.add(50)
    avg.add(60)
    avg.add(70)

    exp_avg = (40+50+60+70)/4
    calc_avg = avg.average()
    
    print "exp={}, calculated={}".format(exp_avg, calc_avg)

# main
if __name__ == "__main__":
    testi()



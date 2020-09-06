class Test(object):
    temp2 = "This a another temp"

    def __init__(self,temp = "temp", *args, **kwargs):
        self.temp = temp
    
    def get_temp(self):
        return self.temp
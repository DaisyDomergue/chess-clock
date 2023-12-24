class timer(object):

    def __init__(self, name, time):
        super(timer, self).__init__()
        self.name = name
        self.initialTime = int(time)
        self.time = int(time)
    def getName(self):
        return self.name
    def getFormatedTime(self):
        min,sec = divmod(self.time, 60)
        formated_time = '{:02d}:{:02d}'.format(min,sec )
        return formated_time
    def getTime(self):
        return self.time
    def decrement_second(self):
        self.time -= 1
        print("Set "+ self.name + " timer to :"+ self.getFormatedTime())
    
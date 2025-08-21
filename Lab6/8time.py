class Time:
    def __init__(self,hour,minute,second):
        self.hour=hour
        self.minute=minute
        self.second=second

    def __eq__(self,other):
        return (self.hour==other.hour and self.minute==other.minute and self.second==other.second)
    
t1=Time(1,2,3)
t2=Time(1,2,3)
t3=Time(1,2,4)
print("t1==t2", t1==t2)
print("t1==t3", t1==t3 )


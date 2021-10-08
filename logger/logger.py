from datetime import date, datetime

def log(text) :
    
    now = datetime.now()
    with open('log.txt', 'a') as f:
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
        f.write(date_time)
        f.write(" ")
        f.write(text)
        f.write(" \n")
        print("logger logging complete")
        
        
        
def read():
    lines = []
    with open('log.txt') as f:
        lines = f.readlines()    
    
    return lines


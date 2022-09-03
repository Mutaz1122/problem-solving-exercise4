def convert_time(time: str) -> str:
    t=time.split()
    if len(t)==2: ##12 to 24
        if(t[1]=="am"):
            if t[0]=="12:00":
                return '0:00'
            return t[0]
        elif t[1]=="pm":
            hour=t[0][0:2]
            if not hour.isdigit():
                hour=t[0][0:1]
                hour=int(hour)+12
                return str(hour)+t[0][1:]

            hour=int(hour)+12
                
            return str(hour)+t[0][2:]

  
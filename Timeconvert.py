def convert_time(time:str) -> str:
    """function to convert_time 12hr time format to 24hr format"""
    am={'12':'00'}
    pm={'01':13, '02':14, '03':15, '04':16, '05':17, '06':18, '07':19, '08':20, '09':21, '10':22, '11':23, '12':12}
    if time[-2:]=='AM':
        if time[:2] != '12':
            return time[:8]
        elif time[:2] == '12':
            return str(am['12'])+time[2:8]
    elif time[-2:]=='PM':
        return str(pm[time[:2]])+time[2:8]
    
print(convert_time('09:13:15PM'))
print(convert_time('09:13:15AM'))
print(convert_time('12:13:15PM'))
print(convert_time('12:13:15AM'))

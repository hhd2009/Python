from urllib import parse
import random

def lookup_min(numbers):
    if numbers == []:
        return
    min_num = numbers[0]
    for number in numbers[1:len(numbers)]:
        if number < min_num:
            min_num = number
    return min_num

def lookup_max(numbers):
    if numbers == []:
        return
    max_num = numbers[0]
    for number in numbers[1:len(numbers)]:
        if number > max_num:
            max_num = number
    return max_num

def encipherment(msg):
    database=[]
    t=0
    for i in msg:
        #print(t)
        #print(i)
        # 判空处理
        if i in ['\n', '\r\n']:
            pass
        # 空行直接跳过
        elif i.strip()=="":
            pass
        database.append([i, t])
        #print(database)
        t+=1
    _database=database
    random.shuffle(_database)
    #print(_database)
    t1=0
    result=''
    for i1 in _database:
        #print(i1)
        result=result+i1[0]+" /\ "+str(i1[1])+" /\ "
        t1+=1
    #print(result)
    result=parse.quote(result)
    print(result)
    print(type(result))
    return result


def unencipherment(msg):
    #print(msg)
    msg=parse.unquote(msg)
    #print(msg)
    _msg=msg.split(" /\ ")
    #print(_msg)
    del(_msg[-1])
    #print(_msg)
    long=len(_msg)
    long=long/2
    long=int(long)
    #print(long)
    database=[]
    for i in range(0,long*2,2):
        #print(i+1)
        database.append(int(_msg[i+1]))
    #print(database)
    _result=[]
    for i1 in range(0,long):
        _min=lookup_min(database)
        #print(">",_min)
        place=database.index(_min)
        #print(">>",place)
        _result.append(_msg[place*2])
        #print(_msg)
        #print(">>>",place*2)
        #print(">>>",_msg[place*2])
        database[database.index(_min)]=lookup_max(database)+1
    result=''
    for i2 in range(0,len(_result)):
        #print(_result[i2])
        result=result+_result[i2]
    print(result)
    print(type(result))
    return result

def en(msg):
    return encipherment(msg)

def unen(msg):
    return unencipherment(msg)

import random
import string
import time
import numpy as np


INF = 50000
M_INF = -INF

Data = []


def count(src, substring, start= None,end=None):
    count = 0
    src_itr = 0
    c_src_itr = 0
    substring_itr = 0
    result = 0
    src_len = len(src)
    substring_len = len(substring)

    if start is not None and start > -src_len:
        if src_len > 0 and start < 0:
            start = start + src_len
        src_itr = start

    if end is not None and end < src_len:
        if end <= -src_len:
            end = 0
        elif src_len > 0 and end < 0 and end > -src_len:
            end = end + src_len
        src_len = end

    if substring_len == 0:
        result = src_len + 1 - src_itr
        if result < 0:
            result = 0
        return result

    if substring_len==1:
        while src_itr < src_len:
            if src[src_itr] == substring[0]:
                count+=1
            src_itr+=1
    else:
        while src_itr < src_len :
            if src[src_itr] == substring[0]:
                c_src_itr = src_itr
                substring_itr = 0

                while substring_itr < substring_len and c_src_itr < src_len and src[c_src_itr] == substring[substring_itr]:
                    c_src_itr += 1
                    substring_itr += 1

                if substring_itr == substring_len:
                    count += 1
                    src_itr = c_src_itr - 1

            src_itr+=1
    return count







def Test1():
    result = count("eeeea","e");
    print("Test 1: ", result==4);


def Test2():
    result = count("eeee","eeee");
    print("Test 2: ", result==1);

def Test3():
    result = count("eeadx","ead");
    print("Test 3: ", result==1);

def Test4():
    result = count("eeadx","sad");
    print("Test 4: ", result==0);

def Test5():
    result = count("ee","eee");
    print("Test 5: ", result==0);

def Test6():
    result = count("eaeae","eae")
    print("Test 6: ", result==1)

def Test7():
    result = count("eee","ee")
    print("Test 7: ", result==1)

def Test8():
    result = count("eee", "")
    print("Test 8: ", result == 4)

def Test9():
    result = count("", "")
    print("Test 9: ", result == 1)

def Test10():
    result = count("", "ea")
    print("Test 10: ", result == 0)

def TestOptional_1():
    result = count("eeee", "ee",1)
    print("TestOptional 1: ", result == 1)

def TestOptional_2():
    result = count("eeee", "ee", end=2)
    print("TestOptional 2: ", result == 1)

def TestOptional_3():
    result = count("eeee", "ee", 1, 3)
    print("TestOptional 3: ", result == 1)

def TestOptional_4():
    result = count("eeee", "ee", 2, 2)
    print("TestOptional 4: ", result == 0)

def TestOptional_5():
    result = count("eeee", "ee", 3, 1)
    print("TestOptional 5: ", result == 0)

def TestOptional_6():
    result = count("eeee", "", 1, 2)
    print("TestOptional 6: ", result == 2)

def TestOptional_7():
    result = count("eeee", "", 3, 1)
    print("TestOptional 7: ", result == 0)

def TestOptional_8():
    result = count("", "e", 3, 1)
    print("TestOptional 8: ", result == 0)

def TestOptional_9():
    result = count("", "", 1, 0)
    print("TestOptional 9: ", result == 0)

def TestOptional_10():
    result = count("", "", 0, 0)
    print("TestOptional 10: ", result == 1)

def TestOptional_11():
    result = count("eee", "e", end=5)
    print("TestOptional 11: ", result == 3)

def TestOptional_12():
    result = count("eee", "e", start=3)
    print("TestOptional 12: ", result == 0)

def TestOptional_13():
    result = count("eee", "e", start=-1)
    print("TestOptional 13: ", result == 1)

def TestOptional_14():
    result = count("eee", "e", end=-1)
    print("TestOptional 14: ", result == 2)

def TestOptional_15():
    result = count("eee", "e", start=-4)
    print("TestOptional 15: ", result == 3)

def TestOptional_16():
    result = count("eee", "e", end=-4)
    print("TestOptional 16: ", result == 0)

def TestOptional_17():
    result = count("eee", "e", start=5)
    print("TestOptional 17: ", result == 0)

def TestOptional_18():
    result = count("eee", "e", start=-4, end=4)
    print("TestOptional 18: ", result == 3)

def TestOptional_19():
    result = count("eee", "e", start=4, end=-4)
    print("TestOptional 19: ", result == 0)

def TestOptional_20():
    result = count("", "", start=-2, end=2)
    print("TestOptional 20: ", result == 1)
def TestOptional_21():
    result = count("UopIcFIdtQFYjODqeukuPvSxT", "", start=-639, end=-607)
    print("TestOptional 21: ", result == 1)


def RandomString( lowerLimit,upperLimit):
    return ''.join(random.choice(string.ascii_letters) for _ in range(random.randint(lowerLimit,upperLimit)))


def GenerateData():
    with open("Test_data","w") as file_object:
        for i in range(1000):
            src = RandomString(20,INF)
            substringUpperLimit = len(src)+10
            if substringUpperLimit > INF:
                substringUpperLimit = INF
            substring = RandomString(20,substringUpperLimit)
            start = random.randint(M_INF,2000)
            end = random.randint(0,INF)

            result = src.count(substring,start,end)
            file_object.write("{};{};{};{};{}\n".format(result,start,end,substring,src))

        for _ in range(1000):
            src = RandomString(2,INF)
            substringUpperLimit = 12
            substring = RandomString(2,substringUpperLimit)
            start = random.randint(M_INF,INF)
            end = random.randint(M_INF,INF)

            result = src.count(substring,start,end)

            file_object.write("{};{};{};{};{}\n".format(result, start, end, substring, src))

        for _ in range(1000):
            src = RandomString(0,INF)
            substringUpperLimit = 1
            substring = RandomString(0,substringUpperLimit)
            start = random.randint(-1000,1000)
            end = random.randint(-1000,1000)

            result = src.count(substring,start,end)

            file_object.write("{};{};{};{};{}\n".format(result,start,end,substring,src))


def LoadData():
    with open("Test_data", "r") as file_object:
        for line in file_object:
            record = line.split(';')
            record[4] = record[4].rstrip('\n')
            Data.append(record)
    print 'Data loaded'


def CheckMyCountFunction():
    with open("error_Case", "w") as file_object:
        for result,start,end,substring,src in Data:
            myresult = count(src,substring,int(start),int(end))
            if(myresult!=int(result)):
                file_object.write("{};{};{};{};{};{}\n".format(result,myresult, start, end, substring, src))
                print 'Error'

    print 'Data Checked'


def TimeTest():
    t = 0
    with open("resultPython", "w") as file_object:
        for i in range(0,4):
            before = time.clock()
            for record in Data:
                start = int(record[1])
                end = int(record[2])
                substring = record[3]
                src = record[4]

                for _ in range(0,1000):
                    t += 1
            after = time.clock()

            loopTime = after - before

            before = time.clock()
            for record in Data:
                start = int(record[1])
                end = int(record[2])
                substring = record[3]
                src = record[4]

                for _ in range(0,1000):
                    t += 1
                    count(src,substring,start,end)

            after = time.clock()

            myImplTime = after - before

            before = time.clock()
            for record in Data:
                start = int(record[1])
                end = int(record[2])
                substring = record[3]
                src = record[4]

                for _ in range(0, 1000):
                    t += 1
                    src.count(substring, start, end)

            after = time.clock()

            builtInTime = after - before
            file_object.write("{};{};{}\n".format(builtInTime,myImplTime,loopTime))
            print 'BuiltIn: {} Implementation: {} loop time: {} Data Size: {} '.format(builtInTime,myImplTime,loopTime,len(Data))



def UnitTest():

    Test1()
    Test2()
    Test3()
    Test4()
    Test5()
    Test6()
    Test7()
    Test8()
    Test9()
    Test10()
    TestOptional_1()
    TestOptional_2()
    TestOptional_3()
    TestOptional_4()
    TestOptional_5()
    TestOptional_6()
    TestOptional_7()
    TestOptional_8()
    TestOptional_9()
    TestOptional_10()
    TestOptional_11()
    TestOptional_12()
    TestOptional_13()
    TestOptional_14()
    TestOptional_15()
    TestOptional_16()
    TestOptional_17()
    TestOptional_18()
    TestOptional_19()
    TestOptional_20()
    TestOptional_21()

#UnitTest()
#GenerateData()# uncomment to make package

LoadData()
#CheckMyCountFunction()# uncomment for checking builtin function with my implementation
TimeTest()

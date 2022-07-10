import os
from time import sleep
import cv2
import numpy as np

#목표 
def solt(list_,c):
    put = []
    put_raw = []
    co = 0
    pu = 0
    max = len(list_)
    l = 0
    while len(list_) != 0:
        for i in range(len(list_)):
            co = list_[i][1]
            if co >= pu:
                pu = co
                l = i
        
        #print(list_[l])
        put.append(list_[l])
        put_raw.append(list_[l][0])
        del list_[l]
        pu = 0
        l = 0
    #print(put)
    return put, put_raw

def voiger(lise_):
    #print(lise_)
    pri = ""
    
    for i in lise_:
        for l in i:
            if l == 1:
                pri += "■"
            else:
                pri += "□"
        pri += "    "
    print(pri)


    


def random():
    i = np.random.randint(0,9)
    if i == 0:
        l = 1
    else:
        l = 0
    return l

def set_s():
    i = []
    for l in range(4):
        i.append(random())
    
    return i

def seting():
    print("\n\n --- ---초기화 및 생성--- --- ")

    i = []
    for o in range(10):
        i.append(set_s())

    voiger(i)
    return i

def counter_to_Selection(ID , select = 4): #순위기반 선택, 개수입력
    print("\n\n--- --- --- 선택 --- --- ---")

    point = 0
    points = []
    put = []
    for i in ID:
        point = 0
        for l in i:
            if l == 1:
                point = point+ 1
        #print(i, " : ", point)
        points.append([i,point])
    #print(solt(points,1))
    _,pointz =  solt(points,1)
    for i in range(select):
        put.append(_[i][0])
    '''
    for i in range(len(pointz)):
        if i < 4:
            print(pointz[i], " | ", put[i])
        else:
            print(pointz[i], " | ")'''
    voiger(pointz)
    print( " ------------- | -------------")
    print( " ------------- V -------------")
    voiger(put)

    return put

def Crossover(ID) :
    Id = counter_to_Selection(ID)
    print("\n\n--- --- ---  교차  --- --- ---")
    co = len(Id)
    put = []
    iut = []
    lc = []
    rc = []
    
    for i in range(10):
        randf = np.random.randint(0,co)
        ld = Id[randf]
        lc.append(ld)
        
        randf = np.random.randint(0,co)
        rd = Id[randf]
        rc.append(rd)
        for l in range(4):
            if ld[l] == rd[l]:
                put.append(ld[l])
            elif random() == 0:
                put.append(ld[l])
            else:
                put.append(rd[l])
        iut.append(put)
        #print(ld," + ",rd, " = ", put)
        put = []
    
    voiger(lc)
    print(" |       |       |       |       |       |       |       |       |       |  ")
    print(" v       v       v       v       v       v       v       v       v       v  ")
    voiger(rc)
    print(" ||      ||      ||      ||      ||      ||      ||      ||      ||      ||  ")
    voiger(iut)

    return Id, iut
    

def mutation(ID):
    i,b = Crossover(ID)
    print("\n\n--- --- --- 돌연변이 --- --- ---")
    for l in range(len(b)):

        randf = np.random.randint(0,5)
        
        if randf == 0: # 결실
            rand = np.random.randint(0,4)
            b[l][rand] = np.random.randint(0,2)
            #print(b[l])
    
    voiger(b)
    return 0 , b
        

        

    
    

def main():
    il = int(input(" 실행할 횟수를 입력하시오. : "))
    os.system('cls')


    print("\n --------------------------------------------------------", 1," 세대\n")
    i = seting()

    for l in range(il):
        
        print("\n --------------------------------------------------------", l+2," 세대\n")
        _,i = mutation(i)
        print("\n\n--- --- ---  결과  --- --- ---")
        voiger(i)
        #cv2.waitKey()
        sleep(1)

    """

    □
    ■


    """

if __name__=="__main__":
    main()
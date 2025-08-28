import time
import random
class First:
    comprehensive={}
    first=[]
    step=[]
    layer1=[]
    layer2=[]
    layer3=[]
    collective_Characters=[]
    lock=""
    mess=""
    total_Positions=""
    wheel=""
    test=""
    frustration=""
    folder=0
    count_Down=0
    decision=0
    
    

    #lock=input("input KEY: ")

    #This is a test string, should be removed after testing. Or rendered inert
    lock="1415plfao17vansepm17eifnpae14anva"

    step=list(lock)

    folder=int(step.pop(0))
    for x in range(folder):
            total_Positions=total_Positions+str(step.pop(0))

    count_Down=int(total_Positions)

    while (count_Down!=0):
        folder=int(step.pop(0))
        safe=""
        wheel=""
        for x in range(folder):
            safe=safe+step.pop(0)
        layer1.append(safe)
        for x in range(int(safe)):
            wheel=wheel+step.pop(0)
        layer2.append(wheel)
        for char in wheel:
            collective_Characters.append(char)
        count_Down=count_Down-1


    mess=input("Place your message here: ")


    for char in mess:
            first.append(char)
    if first != collective_Characters:
         #Dud classification
        print("7")

    for char in mess:
        frustration=first.pop(0)
        layer3.clear()
        for i in range(len(collective_Characters)):
            if collective_Characters[i] == frustration:
                #refrencing the entire collective_Characters in order to find its position
                layer3.append(i)
                print(layer3)
        if len(layer3)>1:
            #this is for deciding which position is to be chosen if there are multiple
            decision=random.randint(1,len(layer3))
            a=layer3.pop(decision-1)
            layer3.clear()
            layer3.append(a)
            print(layer3)
            print(decision)





    print(frustration)
    print(layer1)


    # 1
    # 2
    # 3



    time.sleep(100)


'''
    question0=""    
    answer1=0

    while answer1==0:
        question0=input("Encode or Decode? ")
        if "1" == question0:
            #encode
            answer1=1  
        elif "2" == question0:
            #decode
            answer1=2
        else:
            print("Not a valid answer")    

            

    length_Number_Characters=[]
    wheel=[]
    length_Bite_Size=[]    
    distributor=[]
    intermeditary=[]
    
    while count_Down>0:
    distributor=lock.pop()
    intermeditary=len(distributor)
    length_Number_Characters.append(intermeditary)
    wheel.append(distributor)
    for char in distributor:
        length_Bite_Size.append(char)
'''


"""
    for i, x in enumerate(layer2):
         print(f"Index {i}: {x}")
"""



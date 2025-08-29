import time
import random
class First:
    comprehensive={}
    first=[]
    step=[]
    length_Of_Positions=[]
    positions=[]
    current_Number_Needed=[]
    collective_Characters=[]
    lock=""
    mess=""
    total_Positions=""
    wheel=""
    test=""
    frustration=""
    folder=0
    count_Down=0
    count_Up=0
    decision=0
    b=0
    switch_State=True
    
    

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
        length_Of_Positions.append(safe)
        for x in range(int(safe)):
            wheel=wheel+step.pop(0)
        positions.append(wheel)
        for char in wheel:
            collective_Characters.append(char)
        count_Down=count_Down-1


    mess=input("Place your message here: ")


    for char in mess:
            first.append(char)
    """if first != collective_Characters:
         #Dud classification
        print("7")"""
    
    for char in mess:
        frustration=first.pop(0)
        current_Number_Needed.clear()
        for i in range(len(collective_Characters)):
            if collective_Characters[i] == frustration:
                #refrencing the entire collective_Characters in order to find its position
                current_Number_Needed.append(i)
                print("ih")
        if len(current_Number_Needed)>1:
            #this is for deciding which position is to be chosen if there are multiple
            decision=random.randint(1,len(current_Number_Needed))
            a=current_Number_Needed.pop(decision-1)
            current_Number_Needed.clear()
            current_Number_Needed.append(a)
            print("hi")
        while switch_State==True:
            print(current_Number_Needed)
            print(length_Of_Positions)
            b=int(current_Number_Needed[count_Up])-int(length_Of_Positions[count_Up])
            if b>0:
                current_Number_Needed=b
                count_Up=count_Up+1
            else:
                 switch_State==False
            print(b)
            print(count_Up)
            print(current_Number_Needed)
    print("paint")
    time.sleep(100)



    print(length_Of_Positions)
    print(positions)
    print(current_Number_Needed)

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
    for i, x in enumerate(positions):
         print(f"Index {i}: {x}")
"""



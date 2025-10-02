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
    beeg_Number=[]
    lil_Number=[]
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
    not_Temporary=0
    barracuda=0
    switch_State=True
    
    def peeking_Curtain(sugma):
         print("Peeking: ", sugma)

    #lock=input("input KEY: ")

    #This is not_Temporary test string, should be removed after testing. Or rendered inert
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
        print("Start- ", frustration)
        current_Number_Needed.clear()
        for i in range(len(collective_Characters)):
            if collective_Characters[i] == frustration:
                #refrencing the entire collective_Characters in order to find its position
                current_Number_Needed.append(i)
                peeking_Curtain(current_Number_Needed)
        if len(current_Number_Needed)>1:
            #this is for deciding which position is to be chosen if there are multiple
            decision=random.randint(1,len(current_Number_Needed))
            peeking_Curtain(decision)
            not_Temporary=current_Number_Needed.pop(decision-1)
        else:
            not_Temporary=current_Number_Needed.pop(0)
            print("odd? ", not_Temporary)
        print("Round one: ", not_Temporary)
        current_Number_Needed.clear()
        count_Up=0
        while switch_State==True:
            barracuda=not_Temporary
            print("Next up: ", not_Temporary)
            not_Temporary=not_Temporary-int(length_Of_Positions[count_Up])
            if not_Temporary>0:
                count_Up=count_Up+1
            elif count_Up%2:
                #Odd
                print("stop it")
                beeg_Number.append(count_Up)
                lil_Number.append(barracuda)
                switch_State=False
            else:
                #Even
                beeg_Number.append(count_Up)
                lil_Number.append(barracuda+1)
                switch_State=False
        print("Second up: ", not_Temporary)
        switch_State=True



    print("FNL: ", length_Of_Positions)
    print("FNL: ", positions)
    print("FNL: ", current_Number_Needed)
    print("FNL: ", beeg_Number)
    print("FNL: ", lil_Number)
    print("FNL: ", comprehensive) #this is the final result

    # 1
    # 2
    # 3



    time.sleep(1000)

'''
    while switch_State==True:
            barracuda=not_Temporary
            print("Next up: ", not_Temporary)
            not_Temporary=not_Temporary-int(length_Of_Positions[count_Up])
            if not_Temporary>0:
                count_Up=count_Up+1
            else:
                beeg_Number.append(count_Up)
                lil_Number.append(barracuda)
                switch_State=False
        print("Second up: ", not_Temporary)
        switch_State=True
'''


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
            print("Not not_Temporary valid answer")    

            

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



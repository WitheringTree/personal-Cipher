import time
import random
class First:
    initial=[]
    wheel=[]
    number_Of_Characters_List=[]
    individual_Characters=[]
    characters_Length=0
    counter_Up=0
    electric_Boogalo=0
    test=["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
    key=""
    question=""
    question2=""
    haver=""
    
    
    question=input("Do you want to edit a previous key? Y/N ")
    if "y" in question:
        question2=input("Please input held key: ")
        print(question2)
    else:
        print("Continue as normal")
        
    number_Of_Positions=int(input("Specify number of positions: "))
    static_Number=number_Of_Positions

    time.sleep(0)
    while number_Of_Positions>0:
        counter_Up=1+counter_Up
        number_Of_Positions=number_Of_Positions-1
        print(counter_Up, " / ", static_Number)
        characters=input("What do you want in the position: ")
        characters_Length=len(characters)
        number_Of_Characters_List.append(characters_Length)
        wheel.append(characters)
        for char in characters:
            individual_Characters.append(char)
        key=key+f'{len(str(characters_Length))}{characters_Length}{characters}'

    electric_Boogalo=len(wheel)
    
    key=f'{len(str(electric_Boogalo))}{electric_Boogalo}'+key
    
    #this is to give the key maker something usable, so they don't have to keep inputing for testing
    print(key)


    #individual_Characters=[*wheel]
    #original_Wheel=["1il","26zr","3e","4a","5s","6g","7lt","8b","9jp","o0d","kcsx","f","h","m","n","u","v","w"]
    #random_Integer=0

    
    #encodr=[i for i,x in enumerate(wheel)if x==a]

    #Numbers in each position
    print(number_Of_Characters_List)
    #Intact
    print(wheel)
    #Broken into individual letters
    print(individual_Characters)


#numberofcharacterslist, 


    #While ssem>0:
    #    ssem==ab
    
    time.sleep(100)
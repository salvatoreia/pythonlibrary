#json
import json
ingredients=[]

user_choice=""
while user_choice!="end":
    print("What do u want to do?")
    print("1. load")
    print("2. view")
    print("end to exit")
    user_choice=input("")
    if user_choice=="1":

        choice="yes"
        while choice=="yes":
            ingredient=input("insert the ingredient")
            ingredients.append(ingredient)
            print(ingredients)
            if len(ingredients) >0:
                y=json.dumps(ingredients)
                choice= input("Do u want add other ingredients? yes/no")
            else:
                print("no data added")    
                choice= input("Do u want to add proper data? yes/no")
    elif user_choice=="2":
        print("these are the ingredients:")
        print(ingredients)
        choice="yes"
        while choice=="yes":
            if len(ingredients) >0:
                y=json.dumps(ingredients)
                z=json.loads(y)
                view_choice= int(input("How many ingredients do u want to see?"))
                for n in range(view_choice):
                    print(z[n])    
                break
            else:
                print("no data added")    
                choice= input("Do u want to add proper data? yes/no")


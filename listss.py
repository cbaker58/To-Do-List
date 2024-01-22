#Cora Baker
#1/18/23
#Shopping list

#Initialize
print("Hello, Welcome to the Shopping list")
mylist = ["apples"]
#Functions
def shoppinglist():
    Answer = input("1.Add a task \n2.View List \n3.Mark task complete  \n4.Remove one task \n5. Remove all items from list \n6. Sort items alphabetically \n7. Print the number of items on the list\n8.exit")
    if (Answer== "1"):
        item = str(input("What would you like to add: "))
        mylist.append(item)
        shoppinglist()
        
    elif (Answer == "2"):
        print(mylist)
        shoppinglist()
    
    elif (Answer == "3"):
        change = input("What is the item you would like to mark as complete?: ")
        i = mylist.index(change)
        mylist[i] = change + "X"
        shoppinglist()
    elif(Answer == "4"):
        rem = input("What would you like to remove?: ")
        mylist.remove(rem)
        shoppinglist()
    elif(Answer == "5"):
        mylist.clear()
        shoppinglist()
    elif(Answer == "6"):
        mylist.sort()
        shoppinglist()
    elif(Answer == "7"):
        size = len(mylist)
        print(size)
        shoppinglist()
    elif(Answer == "8"):
        print("Thank You for using the list")

#Main
shoppinglist()
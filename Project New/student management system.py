


while True:
        print("***** Welcome to student management system *****")
        print("=========================================================")
        print("Please choose any one option")
        print("1. To view student list")
        print("2. To add new to list")
        print("3. To remove the data")
        print("4. To search the data")
        print("5. Exit")
        choice=input("Enter an integer between 1 and 5: ")
        if choice == '1':
            file1 = open('myfile.txt', 'r')
            print(file1.read())
            file1.close()
           
                

        elif choice == '2':
            file1 = open("myfile.txt","a")
            userInput = input("enter name")
            file1.write(userInput+ "\n")
            print("Name is added")
            file1.close


        elif choice == '3':
            itemToDelete = input("Enter username")
            file1 = open("myfile.txt","r+")
            #take name to delete
            #search through all the name if this name is present
            allLines = file1.readlines()

            newOutput = ""
            for line in allLines:
                item = line.strip()
                if (itemToDelete == item):
                    continue
                newOutput =newOutput+ line
            #sara output newOutput me aagy
            file1.seek(0)
            file1.truncate(0)
            file1.write(newOutput)
            print("Item is removed")
            file1.close

        elif choice == '4':
            itemToSearch = input("Enter username")
            file1 = open('myfile.txt', 'r')
            allLines = file1.readlines()
            itemIsNotFound = True
            for line in allLines:
                line = line.strip()
                if (itemToSearch == line):
                    itemIsNotFound = False
                    print("user found")

            if (itemIsNotFound):
                print("user is not found")

        elif choice == '5' :
                exit()
                
            

        again_using = input("Do u wish to continue Y or N : ")
        if again_using == "Y":
            continue
        else:
            break 
            



        

    
        

    

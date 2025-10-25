tasks = []
def main():
    print("\n\t***TO DO LIST APP***")
    print("\tby @PAYAL RAMDAS SUNE\n")
    while True:
        print("1.ADD")
        print("2.DELETE")
        print("3.VIEW")
        print("4.UPDATE")
        print("5.EXIT")
        choice = int(input("Enter your choice : "))
        print("\n")

        if (choice == 1):
            item = input("Add your task : ")
            add(item)

        elif (choice == 2):
            if (len(tasks) > 0):
                print("YOUR TO DO TASKS : ")
                for i in range(len(tasks)):
                    print(f"{i + 1}." + tasks[i])
                index = int(input("Enter the Task No. that you want to delete :"))
                delete(index)
            else:
                print("No Tasks to remove\n")

        elif (choice == 3):
            show()

        elif (choice == 4):
            print("YOUR TO DO TASKS : ")
            for i in range(len(tasks)):
                print(f"{i + 1}." + tasks[i])
            index = int(input("Enter the Task No. that you want to update :"))
            update(index)

        elif (choice == 5):
            print("Saving & Exiting ......\n")
            break;

        else:
            print("Enter valid input , please try again..\n")



def add(new_item):
    tasks.append(new_item)
    print("Added Task Successfully!!\n")


def delete(ind):
    tasks.pop(ind - 1)
    print("Removed Task Successfully!!\n")


def show():
    if (len(tasks) == 0):
        print("No Tasks to show\n")
    else:
        print("YOUR TASKS:")
        for i in range(len(tasks)):
            print(i + 1, end=".")
            print(tasks[i])
        print("Shown your Tasks Succesfully!!\n")


def update(ind):
    tasks.pop(ind - 1)
    upd_task = input("Enter your new task : ")
    tasks.insert(ind - 1, upd_task)
    print("Updated Task Successfully!!\n")

if __name__ == "__main__":
    main()




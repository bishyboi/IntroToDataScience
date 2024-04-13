def hello():
    print("hello")
    
def add(x,y):
    print(x+y)

def print_menu():
    print()
    print("1. Print Hello")
    print("2. Add")
    print("3. Exit")
    option = int(input("Please enter an option: "))
    
    return option
    


def main():
    answer = print_menu()
    
    while answer != 3:
        if answer == 1:
            hello()
        if answer == 2:
            add(3,4)
        
        answer = print_menu()
    
    print("\nbye have a nice time")
        
    
if __name__ == "__main__":
    main()
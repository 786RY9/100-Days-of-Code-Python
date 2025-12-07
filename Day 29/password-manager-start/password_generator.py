#Password Generator Project
import random
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # print("Welcome to the PyPassword Generator!")
    # nr_letters= int(input("How many letters would you like in your password?\n")) 
    # nr_symbols = int(input(f"How many symbols would you like?\n"))
    # nr_numbers = int(input(f"How many numbers would you like?\n"))

    #Eazy Level - Order not randomised:
    #e.g. 4 letter, 2 symbol, 2 number = JduE&!91
    # random_letters =[]
    # random_symbols = []
    # random_numbers = []
    letters_length = random.randint(8,10)
    random_letters = [random.choice(letters) for _ in range(letters_length) ]
    # for i in range(8):
    #     random_letters.append(random.choice(letters))
    symbols_length = random.randint(5,10)
    random_symbols = [random.choice(symbols) for _ in range(symbols_length)]
    # for i in range(5):
    #     random_symbols.append(random.choice(symbols))
    numbers_length = random.randint(5,10)
    random_numbers = [random.choice(numbers) for _ in range(numbers_length)]
    # for i in range(7):
    #     random_numbers.append(random.choice(numbers))

    # print('Easy Password')
    # print("".join(random_letters+random_symbols+random_numbers))

    #Hard Level - Order of characters randomised:
    #e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

    password = random_letters+random_symbols+random_numbers

    password_length = letters_length+symbols_length+numbers_length
    random_password = []
    for i in range(password_length):
        choice = random.choice(password)
        random_password.append(choice)
        password.remove(choice)
    # print("".join(random_password))
    return ("".join(random_password))
        
    # print("Difficult Password")   
    





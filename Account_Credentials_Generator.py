import random
import string

def generator():
    print("what Name or Names du you want?")
    Nameinput = input(":")
    print("how many accounts do you wish for each name?")
    Numberinput = int(input(":"))
    Names = [  Nameinput ]
    Numbers = Numberinput
    Numberx = list(range(1,Numbers + 1))
    for Names in Names:
        for Numberx in Numberx:
            print(Names + str(Numberx))

def passlist_generator():
    print("Passlist-Gen")
    print("how long should the passwords be?")
    passwordlength = int(input(":"))
    count = 0
    while count != 10:
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(passwordlength))   
        print(result_str)
        count = count + 1

def pass_generator():
    print("Pass-Gen")
    print("how long should the password be?")
    passwordlength = int(input(":"))
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(passwordlength))   
    print(result_str)

print("GENERATOR")
    
print("Password [P]")
print("Userlists [UL]")
print("Passlists [PL]")
passwordgen = input(":")
if passwordgen == 'P':
    pass_generator()
elif passwordgen == "UL":
    generator()
elif passwordgen == 'PL':
    print("ok")
    passlist_generator()  




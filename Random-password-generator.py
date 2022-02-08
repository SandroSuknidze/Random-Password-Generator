import random
import string

print("Welcome to the password generator")
f_input = input("Would you like to generate the new password?\nyes/no\n")

if f_input == "yes":
    print("1) Only small letters\n2) Only big letters\n3) Only symbols\n4) Only numbers\n5) Small letters and big letters\n6) Mixed")
    s_input = input("What kind of symbols do you want in your password? Choose one\n")
    if s_input == "1":
         list1 = []

         x = int(input("How many letters do you want in your password?\n"))
         for i in range(1, x + 1):
              y = random.choice(string.ascii_lowercase)
              list1.append(y)
              lst_new = [str(a) for a in list1]
         print("Your password is: ", "".join(lst_new))
    elif s_input == "2":
         list1 = []

         x = int(input("How many letters do you want in your password?\n"))
         for i in range(1, x + 1):
              y = random.choice(string.ascii_uppercase)
              list1.append(y)
              lst_new = [str(a) for a in list1]
         print("Your password is: ", "".join(lst_new))
    elif s_input == "3":
         list1 = []

         x = int(input("How many letters do you want in your password?\n"))
         for i in range(1, x + 1):
              y = random.choice(string.punctuation)
              list1.append(y)
              lst_new = [str(a) for a in list1]
         print("Your password is: ", "".join(lst_new))
    elif s_input == "4":
         list1 = []

         x = int(input("How many letters do you want in your password?\n"))
         for i in range(1, x + 1):
              y = random.choice(string.digits)
              list1.append(y)
              lst_new = [str(a) for a in list1]
         print("Your password is: ", "".join(lst_new))
    elif s_input == "5":
         list1 = []

         x = int(input("How many letters do you want in your password?\n"))
         for i in range(1, x + 1):
              y = random.choice(string.ascii_letters)
              list1.append(y)
              lst_new = [str(a) for a in list1]
         print("Your password is: ", "".join(lst_new))
    elif s_input == "6":
         list1 = []

         x = int(input("How many letters do you want in your password?\n"))
         for i in range(1, x + 1):
              y = random.choice(string.ascii_letters + string.hexdigits + string.punctuation)
              list1.append(y)
              lst_new = [str(a) for a in list1]
         print("Your password is: ", "".join(lst_new))


else:
    print("Okay, no problem, have a nice day ;)")





import random

def password_generator():
    lower="abcdefghijklmnopqrstuvwxyz"
    upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers="0123456789"
    symbols="[]{}()*;/_-@"

    all=lower+upper+numbers+symbols
    length=int(input("enter the length of the password"))
    password="".join(random.sample(all,length))
    print(password)
    print("want to generate more passwords? Y/N")
    i=input().upper()
    if i=="Y":
        password_generator()
    else:
        exit("Thankyou for using password!!!")

password_generator()

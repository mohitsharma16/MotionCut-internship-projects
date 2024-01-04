import string
def word_count():
    text=input("Please enter text:")
    print("The original string is :" + text)
    final = sum([i.strip(string.punctuation).isalpha() for i in text.split()])
    print("The number of words in string are :"+ str(final))
    print("want to count again to continue press Y to exit press N")
    ans = input().upper()
    if ans=="Y":
        word_count()
    else:
        exit("Thankyou for using our program!!!!")
word_count()
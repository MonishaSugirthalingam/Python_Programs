def reverse(string):
    letter=" "
    for word in string:
        letter=word+letter
    print("reverced string",letter)
string=input()
print("given string: ",string)
reverse(string)

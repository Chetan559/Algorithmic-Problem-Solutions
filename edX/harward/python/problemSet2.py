'''
In some languages, it’s common to use camel case (otherwise known as “mixed case”) for variables’ names when those names comprise multiple words, whereby the first letter of the first word is lowercase but the first letter of each subsequent word is uppercase. For instance, whereas a variable for a user’s name might be called name, a variable for a user’s first name might be called firstName, and a variable for a user’s preferred first name (e.g., nickname) might be called preferredFirstName.
Python, by contrast, recommends snake case, whereby words are instead separated by underscores (_), with all letters in lowercase. For instance, those same variables would be called name, first_name, and preferred_first_name, respectively, in Python.
In a file called camel.py, implement a program that prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case. Assume that the user’s input will indeed be in camel case.
'''
string = input("camelCase: ")
print("snake_case: ",end="")

for c in range(len(string)):
    if "a" <= string[c] <= "z":
        print(string[c],end ="")
    else:
        print("_",string[c].lower(),sep="",end="")

print()

'''
Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.
In a file called coke.py, implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due. Once the user has inputted at least 50 cents, output how many cents in change the user is owed. Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.
'''

t_money =0
while t_money < 50:
    iMoney = int(input("Insert coin: "))
    if iMoney == 5 or iMoney == 10 or iMoney == 25:
        t_money = t_money + iMoney
        if t_money == 50:
            break
    DueMoney = 50 - t_money
    print("Amount Due:",DueMoney)

OweMoney = t_money -50
print("Change Owed:",OweMoney)


'''
When texting or tweeting, it’s not uncommon to shorten words to save time or space, as by omitting vowels, much like Twitter was originally called twttr. In a file called twttr.py, implement a program that prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.
'''
string = input("Input: ")

for c in range(len(string)):
    if string[c] == 'A' or string[c] == 'E' or string[c] == 'I' or string[c] == 'O' or string[c] == 'U':
        continue
    elif string[c] == 'a' or string[c] == 'e' or string[c] == 'i' or string[c] == 'o' or string[c] == 'u':
        continue
    else:
        print(string[c],end="")

print()

'''
In Massachusetts, home to Harvard University, it’s possible to request a vanity license plate for your car, with your choice of letters and numbers instead of random ones. Among the requirements, though, are:

“All vanity plates must start with at least two letters.”
“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
“No periods, spaces, or punctuation marks are allowed.”
In plates.py, implement a program that prompts the user for a vanity plate and then output Valid if meets all of the requirements or Invalid if it does not. Assume that any letters in the user’s input will be uppercase. Structure your program per the below, wherein is_valid returns True if s meets all requirements and False if it does not. Assume that s will be a str. You’re welcome to implement additional functions for is_valid to call (e.g., one function per requirement).
'''

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 2 <= len(s) <= 6:
        if s.isalnum():
            if s[0:2].isalpha():
                return is_valid2(s)
    else:
        return False

def is_valid2(s):
    i =0
    while i < len(s) and s[i].isalpha():
        i += 1
    if i == len(s):
        return True
    numbers = s[i:len(s)]
    if numbers.isdigit() and not numbers.startswith("0"):
        return True
    else:
        return False


main()


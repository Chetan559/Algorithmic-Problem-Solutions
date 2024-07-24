# implement a program that prompts the user for the answer to the Great Question of Life, 
# the Universe and Everything, outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two.
# Otherwise output No.

answer = input("Your answer to the Great Question of Life, the Universe and Everything")
answer = answer.lower().strip()

if answer == '42' or answer == "forty-two" or answer == "forty two":
    print("Yes")
else:
    print("No")

# In season 7, episode 24 of Seinfeld, Kramer visits a bank that promises to give $100 to anyone who isn’t greeted 
# with a “hello.” Kramer is instead greeted with a “hey,” which he insists isn’t a “hello,” and so he asks for $100.
# The bank’s manager proposes a compromise: “You got a greeting that starts with an ‘h,’ how does $20 sound?” Kramer accepts.

# In a file called bank.py, implement a program that prompts the user for a greeting. 
# If the greeting starts with “hello”, output $0. If the greeting starts with an “h” (but not “hello”), output $20.
# Otherwise, output $100. Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.

greeting = input("hello, there").strip().lower()

ans = greeting.find('hello')
ans2 = greeting.find('h')

if ans == 0:
    print("$0")
elif ans2 == 0:
    print("$20")
else:
    print("$100")

# In a file called extensions.py, implement a program that prompts the user for the name of a file and 
# then outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:
# .gif, .jpg, .jpeg, .png, .pdf, .txt, .zip
# If the file’s name ends with some other suffix or has no suffix at all, output application/octet-stream instead,
# which is a common default.


filename = input("File Name: ").strip().lower()

fname,sep,extention = filename.rpartition('.')
# str.rpartition(sep)  :Split the string at the last occurrence of sep, and return a 3-tuple containing the part before the separator, the separator itself, and the part after the separator. If the separator is not found, return a 3-tuple containing two empty strings, followed by the string itself.

match extention:
    case 'gif':
        print("image/" + extention)
    case 'jpg' | 'jpeg':
        print("image/" + "jpeg")
    case 'png':
        print("image/" + extention)
    case 'pdf':
        print("application/" + extention)
    case 'txt':
        print("text/" + fname)
    case 'zip':
        print("application/" + extention)
    case 'bin':
        print( "application/octet-stream" )
    case filename :
        print( "application/octet-stream" )

# in a file called interpreter.py, implement a program that prompts the user for an arithmetic expression and then calculates and outputs the result as a floating-point value formatted to one decimal place. 
# Assume that the user’s input will be formatted as x y z, with one space between x and y and one space between y and z, wherein:
# x is an integer
# y is +, -, *, or /
# z is an integer
# For instance, if the user inputs 1 + 1, your program should output 2.0. Assume that, if y is /, then z will not be 0.
# Note that, just as python itself is an interpreter for Python, so will your interpreter.py be an interpreter for math!

expression = input("Expression:")

x,y,z = expression.split("")
# https://docs.python.org/3/library/stdtypes.html#str.split

x = float(x)
z = float(z)
match y:
    case '+':
        print(f"{(x+z):.1f}")
    case '-':
        print(f"{(x-z):.1f}")
    case '*':
        print(f"{(x*z):.1f}")
    case '/':
        print(f"{(x/z):.1f}")


# In meal.py, implement a program that prompts the user for a time and outputs whether it’s breakfast time, lunch time, or dinner time. If it’s not time for a meal, don’t output anything at all. Assume that the user’s input will be formatted in 24-hour time as #:## or ##:##. And assume that each meal’s time range is inclusive. For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime in between, it’s time for breakfast.

# Structure your program per the below, wherein convert is a function (that can be called by main) that converts time, a str in 24-hour format, to the corresponding number of hours as a float. For instance, given a time like "7:30" (i.e., 7 hours and 30 minutes), convert should return 7.5 (i.e., 7.5 hours).
# Challenge
# If up for a challenge, optionally add support for 12-hour times, allowing the user to input times in these formats too:
#:## a.m. and ##:## a.m.
#:## p.m. and ##:## p.m.
def main():
    ftime = input("what time is it? ")
    time1,sep,time2 = ftime.rpartition(" ")
    if sep == " ":
        time = convert(time1)
        if (8 >= time >= 7) and time2 == "a.m.":
            print("breakfast time")
        elif (13 > time >= 12 or 2 > time >= 1) and  time2 == "p.m.":
            print("lunch time")
        elif (7 >= time >= 6) and time2 == "p.m.":
            print("dinner time")
    else :
        time = convert(time2)
        if 8 >= time >= 7:
            print("breakfast time")
        elif 13 >= time >= 12:
            print("lunch time")
        elif 19 >= time >= 18:
            print("dinner time")

def convert(time):
    hours, minutes =  time.split(":")
    timeY = float(hours) + float(minutes)/60
    return timeY

if __name__ == "__main__":
    main()

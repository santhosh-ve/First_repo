##time converter
total_secs = int(input("How many seconds, in total?"))
hours = total_secs // 3600
secs_still_remaining = total_secs % 3600
minutes = secs_still_remaining // 60
secs_finally_remaining = secs_still_remaining % 60
print("Hrs=", hours, " mins=", minutes,"secs=", secs_finally_remaining)

##Compound interest
#Get data from user
p = float(input('Enter principle amount='))
r = float(input('Enter interest rate='))
n = float(input('number of iterations='))
t = float(input('number of years='))
#calculate
a=p*(1+(r/float(n)))**(n*t)
print ('Compound interest rate is =',a)

##time
time_now = input("What time is it?" )
hours_to_wait = input("How long to wait?" )
alarm_time = int(time_now) + int(hours_to_wait)
print(alarm_time %24)

##turtle 
##math
##random
##time

day_dict = {0: 'Sunday',1: 'Monday',2: 'Tuesday',3: 'Wednesday',4: 'Thursday',5: 'Friday',6: 'Saturday'}

def day_num_to_day_string(num):
    try:
        return day_dict[num]
    except:
        return None
print(day_num_to_day_string(6))


endhour = start_hour + (length // 60)
endminute = start_minute + (length % 60)
endhour += endminute // 60
endminute = endminute % 60
endhour = endhour % 24
print('{}:{}'.format(endhour, endminute)

##leap year or not
def leap_year(year):
    if year%4==0:
        if year %100:
            if year%400:
                print(year, "is leap year")
            else:
                print(year, "not a leap year")
        else:
            print(year,"is leap year")
    else:
        print(year,"is leap year")

##another method
year = int(input("Enter the year:"))
if ((year%4==0 and year%100 !=0) or year%400==0):
    print(year, "is leap year")
else:
    print(year, "is not leap year")		


largestNumber = -99999999
counter = 0

number = int(input("Enter a number or type -1 to end program: "))

while number != -1:
    counter += 1

    if number > largestNumber:
        largestNumber = number
    number = int(input("Enter a number or type -1 to end program: "))

if counter:
    print("The largest number is", largestNumber)
else:
    print("You haven't entered any number.")
	
blocks = int(input("Enter the number of blocks: "))

height = 0
inlayer = 1
while inlayer <= blocks:
    height += 1
    blocks -= inlayer
    inlayer += 1

print("The height of the pyramid:", height)

c0 = int(input("Enter c0: "))

if c0 > 1:
	steps = 0
	while c0 != 1:
		if c0 %2 != 0:
			cnew = 3 * c0 + 1
		else:
			cnew = c0 // 2
		print(c0)
		c0 = cnew
		steps += 1
	print("steps =",steps)
else:
	print("Bad c0 value")
	
drawn = [5, 11, 9, 42, 3, 49]
bets = [3, 7, 11, 42, 34, 49]
hits = 0

for number in bets:
    if number in drawn:
        hits += 1

print(hits)

myList = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
newList = []
for number in myList:  # Browse all numbers from the source list.
	if number not in newList:  # If the number doesn't appear within the new list...
		newList.append(number)  # ...append it here.
myList = newList[:]  # Make a copy of newlist.
print("The list with unique elements only:")
print(myList)

def isYearLeap(year):
	if year % 4 != 0:
		return False
	elif year % 100 != 0:
		return True
	elif year % 400 != 0:
		return False
	else:
		return True

def isPrime(num):
    for i in range(2, int(1 + num ** 0.5)):
        if num % i == 0:
            return False
    return True

##pounds to kilo
def lbtokg(lb):
    return lb * 0.45359237

print(lbtokg(1))

##feet inch
def ftintom(ft, inch):
    return ft * 0.3048 + inch * 0.0254

print(ftintom(1, 1)

##bmi
def bmi(weight, height):
    if height < 1.0 or height > 2.5 or \
    weight < 20 or weight > 200:
        return None
    
    return weight / height ** 2

##triangle
def isItATriangle(a, b, c):
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if c + a <= b:
        return False
    return True

print(isItATriangle(1, 1, 1))

def isItATriangle(a, b, c):
	return a + b > c and b + c > a and c + a > b

def isItATriangle(a, b, c):
    if a + b <= c or b + c <= a or \
    c + a <= b:
        return False
    return True

##factorial
def factorialFun(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    
    product = 1
    for i in range(2, n + 1):
        product *= i
    return product

for n in range(1, 6): # testing
    print(n, factorialFun(n))


# Recursive implementation of the factorial function
def factorial(n):
    if n == 1:    # the base case (termination condition)
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(4)) # 4 * 3 * 2 * 1 = 24


# define Python user-defined exceptions
class Error(Exception):
    """Base class for other exceptions"""
    pass

class ValueTooSmallError(Error):
    """Raised when the input value is too small"""
    pass

class ValueTooLargeError(Error):
    """Raised when the input value is too large"""
    pass

# you need to guess this number
number = 10

# user guesses a number until he/she gets it right
while True:
    try:
        i_num = int(input("Enter a number: "))
        if i_num < number:
            raise ValueTooSmallError
        elif i_num > number:
            raise ValueTooLargeError
        break
    except ValueTooSmallError:
        print("This value is too small, try again!")
    except ValueTooLargeError:
        print("This value is too large, try again!")

print("Congratulations! You guessed it correctly.")
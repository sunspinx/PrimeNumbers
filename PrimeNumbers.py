import os
from sys import stdout

# Default values
num_max = 25000
num_min = 2
first_number_in_line = True
last_number_in_line = False
numbers = []
i = 0

# if text file already exists
if os.path.exists('primenumber_list.txt'):
    # we open file for read-only
    f = open('primenumber_list.txt', 'r')
    # we save the content of file to variable
    data = f.read().replace('\n', '')
    # we create array of 'numbers' saved as string
    numbers_string = data.split(',')

    # loop goes through nummbers saved as string
    for number in numbers_string:
        # if numbers from previous search are saved properly -> they are integer
        if number.isdigit():
            # we add them to new array which contains numbers
            numbers.append(int(number))
    # we find the biggest saved number
    # we iterate it by 1 so we won't check for the same number again
    num_min = max(numbers)
    num_min += 1

# loop starts from the number_minimum which is the biggest one from text file or the default value
for number in range(num_min, num_max+1):
    # we open file for write (not overwrite)
    f = open('primenumber_list.txt', 'a')
    # loop go trough numbers 2 to current number (divisor can't be higher than current number)
    for divisor in range(2, number):
        # if current number modulo divisor is 0 then it's not primenumber and we don't have check other divisors
        if((number % divisor) == 0):
            break
    # numbers which are primenumbers
    else:
        # every 20th number will be on new line
        if i == 20:
            # write number to text file
            f.write('\n')
            # reset variable
            i = 0
        else:
            # write number to text file
            f.write('%d,' % number)
        # iterate variable
        i += 1
        # close the file
        f.close()

    # show current number
    stdout.write("\rChecking number: " + str(number) + " ...")
    stdout.flush()

stdout.write("\rApplication checked " + str(num_max - num_min) + " numbers\n")
print("Text file with all prime number is being opened")
## open text file with primenumbers
os.startfile('primenumber_list.txt')
input("Press any button to terminate this file!")
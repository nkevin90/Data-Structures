""" program to convert mobile number into words
"""

def mobile_to_words(number):
    global digits
    digits = ['zero', 'one ', 'two ', 'three ', 'four ', 'five ', 'six ', 'seven ', 'eight ', 'nine ']
    if number == 0:
        return ''
    else:
        small = digits[number % 10]
        ans = mobile_to_words(int(number / 10)) + small + ''
        return ans


number = int(input('Hi User,Kindly enter your mobile number:\n '))
print('Mobile Number entered was \n', end='')
print(mobile_to_words(number))

'''List Examples'''
# Create a 5 x 5 matrix using a list of lists: matrix
matrix = [[0,1,2,3,4] for col in range (5)]

# Print the matrix
for row in matrix:
    print(row)


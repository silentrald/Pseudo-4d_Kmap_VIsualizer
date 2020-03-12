# FUNCTIONS
def to_decimal(bit):
    decimal = 0
    power2 = 1
    while bit > 0:
        decimal += bit % 10 * power2
        power2 *= 2
        bit //= 10
    return decimal

def convert(string):
    c1 = 0
    c2 = 0
    for c in string:
        c1 *= 10
        c2 *= 10
        if c == '0':
            c1 += 1
            c2 += 1
        elif c == '1':
            c2 += 1
    print(c1, ' ', c2)
    c1 = to_decimal(c1)
    c2 = to_decimal(c2)
    return [c1, c2]

def pow2(n):
    return 1 << n

def to_string_bits(decimal, size):
    bits = ''
    for i in range(size):
        bits += str(decimal & 1)
        decimal = decimal >> 1
    return bits[::-1]

# MAIN

filename = input('Input a filename: ')
# get how many input variables are there
input_var = int(input('How many input variables are there: '))
terms = pow2(input_var)

# what conditions will make the output true
# condition 1 xoring
# condition 2 anding
n_conditions = int(input('How many conditions are there: '))

print('1 - true, 0 - false, x - does not matter')
conditions = []
for i in range(n_conditions):
    conditions.append(convert(input('Condition ' + str(i + 1) + ': ').lower()))
    print(conditions[i])

minterms = []
for term in range(terms):
    for condition in conditions:
        if (term ^ condition[0]) & condition[1] == condition[1]:
            minterms.append(term)
            break

print(minterms)

with open('./' + filename + '.txt', 'w') as fp:
    for term in minterms:
        fp.write(str(term) + ', ')
    

# expression = ''
# # convert to string minterms
# for term in minterms:
#     # convert decimal to string bits
#     string = to_string_bits(term, input_var)
#     char = 97
#     for c in string:
#         if c == '0':
#             expression += '~'
#         expression += chr(char) + ' '
#         char += 1
    
#     expression += '+ '

# # remove the last ' + '
# expression = expression[0:-3]
# print(expression)

# with open('./' + filename + '_str.txt', 'w') as fp:
#     fp.write(expression)
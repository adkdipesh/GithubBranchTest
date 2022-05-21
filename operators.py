# Operators are special symbols in Python 

# Arithmetic operators  ( +, -, *, /, %, //, ** ) - (in Lowest to Highest precedence)
# - used with numeric values to perform common mathematical operations

# Assignment operators  ( =, +=, -=, *=, /=, //=, **=, &=, |=, ^=, >>=, <<= )
# - used to assign values to variables

# Comparison operators  ( ==, !=, >, <, >=, <= )
# - used to compare two values

# Logical operators     ( and, or, not )
# - used to combine conditional statements

# Identity operators    ( is, is not )
# - used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location

# Membership operators      ( in, not in )
# - used to test if a sequence is presented in an object

# Bitwise operators     ( &, |, ^, ~, <<, >> )  





# Arithmetic operators
# /     (Modulus-Returns FLoat whatsoever in whole number)
# //    (Floored Division - Returns quotient in whole number)
# %     (Remainder - Returns Remainder)
# **    (Exponent - left operand raised to the power of right)

print('5 + 2 =',5+2)
print(5.555-2)
print(5*2.0001)
print(7/3)
print (17//3)
print(17%3)
print('15**4=',15**4)

print(10%7//2*20-25+5)



# Assignment Operators
a = 5
print('a=',a)
# Error: print(a+=5)    <- cannot use augmented assignment statement inside print statement
a += 5      # a = a + 5
print('a += 5 =',a)

a =+ 10      # a = +5 ie. a = 10
print('a =',a)
print('a =+ 5 =',a)
# Error: a++  -> Python donot allow increment/decrement operator, unlike c,c++/Java/Javascript
a -= 5
print('a -= 5 =',a)
a *= 5
print('a *= 5 =',a)
a /= 5
print('a /= 5 =',a)
a %= 5
print('a %= 5 =',a)


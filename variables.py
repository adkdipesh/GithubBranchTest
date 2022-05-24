
#Variables
# - are containers for storing data values that may take on one or more values during a program’s runtime. 
# - is created the momemt value is assigned
# - python has no command for declaring a variable


# Naming a variable

# - must be single word, consisting letters/numbers/_
# - cannot begin with number
# - Variables in Python which start with _ (underscore) are considered as “Unuseful” ie. should not be used again in the code


# Examples:

#Error 5a = 10
a = 5
print(a)
abc = "I'm a string type variable"
print(abc)
a55 = 'string type variable-2'
print(a55)
_a55 = 'Unuseful variable'
print(_a55)

print(abc + a55 + _a55)

a=b=c = "one value to multiple variable"
print('\na=b=c=', a)

x, y, z = "many value ", 2, " multiple variable"
print('\nx=',x, '\ny=',y, '\nz=',z)






# PB95-ToBasic
PyToBasic converts python code to a language used in game Progressbar95 called PBasic.
Since python code is much more readable, you will create scripts much faster.

> [!NOTE]  
> This is a fun little project that shouldn't be taken seriously.
> PBasic is very limited, you can't concatonate strings, create functions, create while loops, create classes, 
> use most compare operators, create local variables and much more. Take it as a small tool for experimenting.

## Contents
  - [Usage](#usage)
  - [Documentation](#documentation)
  - [Contribution](#contribution)
  - [License](#license)

## Usage
Write your code in programm.py and then execute main.py file. The console output is your PBasic programm.

Note that you need to manually input instructions in game. There are save files for written code 
(/data/data/com.spookyhousestudios.progressbar95/app_data on android), but if you change them, game will execute code incorrectly.

## Documentation

This part will go over operations you can do in the converter.

### Binary Operations
Currently, you can only add, substract, multiply and divide as many numbers as you want.
Brackets will be placed accordingly.

```python
# Implemented
10 + 5
a + b
a * (12 + 3) - 12
10 / (100 * 25)

# Not implemented
10 % 2
10 // 2
10 ** 2
```

### Boolean operations
Are not supported at all. You can only use compare operators ==, >, <

### Assingment
You can assing string and numbers to variables. Converter will translate them to appropriate names.
Unlike strings, you can do math operations on numbers.

```python
# Implemented
a = "PBasic"
a = 25 + 25
a, b = c, d

# Not implemented
a = True
a = "P" + "Basic"
a = a or b
```

### Print
You can output your variables, binary operations or results of in-build functions. Multiple print arguments will split into multiple lines.

```python
# Implemented
print(20)
print(a)
print(a + b)
print(cos(12))

# Not implemented
print(f"F string {a}")
print(a or b)
```

### Input
You can get input from user by using input(). Note that it will only properly work as a single statement. Commets are ignored.

```python
# Implemented
a = input()
a = input("Comments are ignored")

# Not implemented
print(input())
a, b = input()
```

### If statemets
You can create as many if statements as you want. If they take single actions, code will be optimised. 
Note that you're required to use compare operator as condition.

```python
if a > b:
    print(a)
    if a == 10:
        print(10)
elif 5 < 0:
    print("No way")
else:
    print(b)
```

### For loops
You can create multiple for loops. You need to use range() as an iterator object. You can't use break and else statements.
Note that in PBasic the first value in iteration is 1, but it's changed for compatibility. Make sure to specify the start number when neccessary.

```python
# Implemented
for i in range(10):
    for j in range(1, 11):
        print(j)

# Not implemented
for letter in "any other iterator":
    print(letter)
```

### Functions
You can use everything said above plus functions provided in src.aliases. Sadly you can't create your own functions. 
Technically it's possible but it's really unstable.

```python
from src.aliases import *

cls()
for i in range(1, 17):
    background(i)

print(tan(30))
print(cos(30 + rnd(25)))  # !!! Addition will happen only after cos will work. You can still create code like this
```

## Contribution
I don't think many people will use this converter, I created it for myself in the first place, 
but if you want to improve already existing code or implement your own functionality, then go ahead. If you want to 
reach me, there's a Discord link in my profile.

## License
This project uses MIT License. See [LICENSE](https://github.com/Lemon4ksan/PB95-PyToBasic/blob/master/LICENSE) for details.
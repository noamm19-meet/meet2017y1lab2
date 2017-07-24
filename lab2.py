Python 3.5.2 (default, Nov 17 2016, 17:05:23) 
[GCC 5.4.0 20160609] on linux
Type "copyright", "credits" or "license()" for more information.
>>> a=5
>>> b=10
>>> a=5
>>> b=a-5
>>> b
0
>>> a
5
>>> a=5
>>> a
5
>>> a=a+5
>>> 
>>> a
10
>>> b=a-5
>>> b
5
>>> a=b
>>> b=a
>>> a
5
>>> b
5
>>> 
>>> 
>>> a=5
>>> b=10
>>> a=b
>>> a
10
>>> b
10
>>> 
>>> 
>>> a=5
>>> b=10
>>> b=a
>>> a
5
>>> b
5
>>> 
>>> 
>>> a=5
>>> b=10
>>> c=a
>>> a=b
>>> a
10
>>> b=c
>>> b
5
>>> a
10
>>> five=4
>>> print(five)
4
>>> print(five*3)
12
>>> 
>>> 
>>> my_name='student'
>>> print('Hi,' + myname')
      
SyntaxError: EOL while scanning string literal
>>> print('Hi '+'myname')
Hi myname
>>> print('Hi '+'my_name')
Hi my_name
>>> 'my_name'='sudent'
SyntaxError: can't assign to literal
>>> my_mame=student
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    my_mame=student
NameError: name 'student' is not defined
>>> my_name='student
SyntaxError: EOL while scanning string literal
>>> my_name='student'
>>> print('Hi '+my_name)
Hi student
>>> 
>>> 
>>> 
>>> my_name=15
>>> print('I am '+)
SyntaxError: invalid syntax
>>> 
>>> 
>>> 
>>> 
>>> my_age=15
>>> print('I am'+my_age+'years old')
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    print('I am'+my_age+'years old')
TypeError: Can't convert 'int' object to str implicitly
>>> print('I am'+my_age+('years old'))
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    print('I am'+my_age+('years old'))
TypeError: Can't convert 'int' object to str implicitly
>>> print('I am'+my_age +'years old')
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    print('I am'+my_age +'years old')
TypeError: Can't convert 'int' object to str implicitly
>>> print('I am '+my_age+'years old')
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    print('I am '+my_age+'years old')
TypeError: Can't convert 'int' object to str implicitly

>>> 
>>> 
>>> my_age='15'
>>> print('I am '+my_age +'years old')
I am 15years old
>>> 
>>> 
>>> 
>>>  print('I am '+my_age+'years old')
 
SyntaxError: unexpected indent
>>> print('I am '+my_age +'years old')
I am 15years old
>>>  print('I am '+my_age+'years old')
 
SyntaxError: unexpected indent
>>> print('I am '+my_age+'years old')
I am 15years old
>>> print('I am '+my_age+'years old')
I am 15years old
>>> print('I am '+my_age+'  years old')
I am 15  years old
>>> 

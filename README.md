![](https://img.shields.io/badge/license-MIT-yellowgreen)
![](https://img.shields.io/badge/python-3.8-red)

# pyculas

# Installation Instruction
use pip or pip3 to install the library.
```
pip install pyculas
```
# Note:
Currently this library support only algebraic fuction. Soon we will come with other function like Trigonometry, logarithm etc.

## Usage

This class takes a list of terms in a polynomial expression

example -

If you have 4x^3 - 2x + 6, then create the object as follows -

A = algebric(['4x^3' , '-2x' , '6'])

This method differentiates a polynomial expression at a given value and outputs the final expression.

i.e you can use it like this
```
from pyculas import Expression
A = Expression.algebric(['4x^3' , '-2x' , '6'])
print(A.differentiate())
```
output -

`12x^2-2`
        
1.If only final expression required

Q. `2x^2+2`

```
from pyculas import Expression
A = Expression.algebric(['2x^2' , '2'])
print(A.differentiate())
```
output -

`['4x']`

2.To get value at a point

Q. `2x^2+2`

```
from pyculas import Expression
A = Expression.algebric(['2x^2' , '2'])
print(A.differentiate())
```

A = algebric(['2x^2 , '2'] , value=3 , level=1)

output-

`(['4x'] , 12)`        



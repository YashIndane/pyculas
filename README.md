![](https://img.shields.io/badge/license-MIT-yellowgreen)
![](https://img.shields.io/badge/python-3.8-red)

# pyculas

# Installation Instruction
use pip or pip3 to install the library.
```
pip install pyculas
```
# Note:
Currently this library support only algebric expressions. Soon we will update for trigonometric, logarithmic expressions , etc.

## Usage

This class takes a list of terms in a polynomial expression

## Importing

```
from pyculas import Expression
```

example -

If you have 4x^3 - 2x + 6, then create the object as follows -

A = Expression.algebric(['4x^3' , '-2x' , '6'])

This method differentiates a polynomial expression at a given value and outputs the final expression.

output -

`(['12x^2','-2'])`
        
1.If only final expression required

Q. `2x^2+2`

```
A = Expression.algebric(['2x^2' , '2'])
print(A.differentiate())
```
output -

`['4x']`

2.To get value at a point

Q. Find the diffrenciation of `2x^2+2` at x=3. 

```
A = Expression.algebric(['2x^2' , '2'])
print(A.differentiate(value=3,level=1))
```
output-

`(['4x'] , 12)`     

Here `value` means at which point you want to differentaite and `level` means the nth derivative.



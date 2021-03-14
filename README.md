![](https://img.shields.io/badge/license-MIT-yellowgreen)
![](https://img.shields.io/badge/python-3.8-red)

# pyculas

# Installation Instructions
use pip or pip3 to install the library.
```
pip install pyculas
```
# Note:
Currently this library support only algebraic expressions. Soon we will update for trigonometric, logarithmic expressions , etc.

## Usage

This class takes a list of terms in a polynomial expression

## Importing

```
from pyculas import Expression
```

## Examples of usage:

If you have 4x^3 - 2x + 6, then create the object as follows -

A = Expression.algebraic(["4x^3 - 2x + 6"])

This method differentiates a polynomial expression at a given value and outputs the final expression.

Output:

`('12x^2 - 2' , None)`
        
1.If only final expression required

Q. `2x^2+2`

```
A = Expression.algebraic(["2x^2 + 2"])
print(A.differentiate())
```
Output:

`('4x' , None)`

2.To get value at a point

Q. Find the differentiation of `2x^2+2` at x=3. 

```
A = Expression.algebraic(["2x^2 + 2"])
print(A.differentiate(value=3,level=1))
```
Output:

`('4x' , 12)`     

Here `value` means at which point you want to differentiate and `level` means the nth derivative.

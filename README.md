![](https://img.shields.io/badge/license-MIT-yellowgreen)
![](https://img.shields.io/badge/python-3.8-red)

# pyculas

```
pip install pyculas
```

## Usage

This class takes a list of terms in a polynomial expression

example -

If you have 4x^3 - 2x + 6, then create the object as follows -

A = algebric(['4x^3' , '-2x' , '6'])

This method differentiates a polynomial expression at a given value and outputs the final expression.
        
1.If only final expression required

example -

A = algebric(['2x^2' , '2'])

print(A.differentiate())

output -

`['4x']`

2.To get value at a point

A = algebric(['2x^2 , '2'] , value=3 , level=1)

output-

`(['4x'] , 12)`        

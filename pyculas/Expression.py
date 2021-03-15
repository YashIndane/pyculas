import re
from pyculas.formats import simplify , toarray , tostring

class algebraic:
    """
        This class takes a string of the polynomial expression 
        example -
        If you have 4x^3 - 2x + 6, then create the object as follows -
        A = algebraic(["4x^3 - 2x + 6"])
    """

    def __init__(self, expressionString : str):
        # simplifying the algebraic expression
        self.expressionList = simplify(toarray(expressionString))
        
    def differentiate(self , value : float = None , level : int = 1) -> tuple:
        """
        This method differentiates a polynomial expression at a given value and 
        outputs the final expression.
        
        1.If only final expression required
        example -
        A = algebraic(["2x^2 + 2"])
        print(A.differentiate())
        output -
        ('4x' , None)
        2.To get value at a point
        A = algebraic(["2x^2 + 2"] , value=3 , level=1)
        output-
        ('4x' , 12)
        """
        
        exList = self.expressionList

        for level_ in range(1 , level + 1):

                diff_exp = []
                diff_value = []

                just_digits = r'\-?\d+\.?\d*$'
                power_one_decimal = r'\-?\d+\.?\d*x$'
                coefficient_power_posi_d = r'\-?\d+\.?\d*x\^\-?\d+\.?\d*'
                only_power = r'\-?x\^\-?\d+\.?\d*'

                for terms in exList:

                    if terms == 'x':
                        diff_exp.append('1')
                        if level_ ==  level :
                            diff_value.append(1)

                    elif terms == '-x':
                        diff_exp.append('-1')
                        if level_ == level :
                            diff_value.append(-1)

                    elif bool(re.match(just_digits , terms)) : pass    
                    
                    #for coefficients and power as one (+ve or -ve)
                    elif bool(re.match(power_one_decimal , terms)) :
                        diff_exp.append(terms[:-1])
                        if level_ == level:
                            diff_value.append(float(terms[:-1]))

                    #for coefficient and power as any number (+ve or -ve ) 
                    elif bool(re.match(coefficient_power_posi_d , terms)) :
                        power = float(terms[terms.index('^') + 1 : ])
                        coefficient = float(terms[ : terms.index('x')])
                        final_coefficient = power * coefficient
                        final_power = power - 1
                        if value != None and level == level_:
                            diff_value.append(final_coefficient * (value ** final_power))
                        if final_coefficient != 0:

                            final_coefficient = "{0:.3f}".format(final_coefficient)  
                            final_power = "{0:.3f}".format(final_power) 
                            final_exp = f'{final_coefficient}x^{final_power}' if final_power != 1 else f'{final_coefficient}x'  
                            final_exp = final_exp.replace("x^1.000", "x")
                            final_exp = final_exp.replace("x^0.000" , "")  
                            diff_exp.append(final_exp)

                    #for no coefficient but with any power 
                    elif bool(re.match(only_power , terms)) :
                        power = float(terms[terms.index('^') + 1 : ])
                        final_coefficient = power if terms.index('x') == 0 else -power 
                        final_power = power - 1  
                        if value != None and level == level_: 
                            diff_value.append(final_coefficient * (value ** final_power ))
                        if final_coefficient != 0:    
                            final_coefficient = "{0:.3f}".format(final_coefficient)
                            final_power = "{0:.3f}".format(final_power)
                            final_exp = f'{final_coefficient}x^{final_power}' if final_power != 1 else f'{final_coefficient}x'
                            final_exp = final_exp.replace("x^1.000", "x")
                            final_exp = final_exp.replace("x^0.000" , "") 
                            diff_exp.append(final_exp)

                    exList = diff_exp    
        
        try:
           return (tostring(diff_exp) , float("{0:.3f}".format(sum(diff_value)))) if value != None else (tostring(diff_exp) , None)
        except Exception as e:
           return (tostring(diff_exp) , "{0:.3f}".format(sum(diff_value)))

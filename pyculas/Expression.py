import re
from pyculas.formats import simplify , toarray , tostring

#regex for various type of expressions
just_digits = r'\-?\d+\.?\d*$'
power_one_decimal = r'\-?\d+\.?\d*x$'
coefficient_power_posi_d = r'\-?\d+\.?\d*x\^\-?\d+\.?\d*'
only_power = r'\-?x\^\-?\d+\.?\d*'

class algebraic:
    """
        This class takes a string of the polynomial expression 
        example -
        If you have 4x^3 - 2x + 6, then create the object as follows -
        A = algebraic("4x^3 - 2x + 6")
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
        A = algebraic("2x^2 + 2")
        print(A.differentiate())
        output -
        ('4.000x', None)
        2.To get value at a point
        print(A.differentiate(value = 2, level = 1))
        output-
        ('4.000x', 8.0)
        """
        
        exList = self.expressionList

        for level_ in range(1 , level + 1):

                diff_exp = []
                diff_value = []

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

    def integrate(self, lower_limit : float = None , upper_limit : float = None) -> tuple :

                """
                This method integrates a polynomial expression and outputs the
                final expression.
        
                1.If only final expression required
                example -
                A = algebraic("2x^2 + 2")
                print(A.integrate())
                output -
                ('0.667x^3.000 + 2.0x + c', None)
                2.To evaluate when limits are given
                print(A.integrate(upper_limit=4 , lower_limit=2))
                output-
                ('0.667x^3.000 + 2.0x + c', 41.352)
                """

                exList = self.expressionList

                inte_value = []
                fin_val =[]

                for terms in exList:
                    if terms == 'x':
                        inte_value.append('0.5x^2')
                        if upper_limit is not None and lower_limit is not None:
                          val = (upper_limit ** 2) - (lower_limit ** 2)
                          fin_val.append(0.5 * val)
                    
                    elif terms == '-x':
                        inte_value.append('-0.5x^2')
                        if upper_limit is not None and lower_limit is not None:
                          val = (upper_limit ** 2) - (lower_limit ** 2)
                          fin_val.append(-0.5 * val)

                    elif bool(re.match(just_digits , terms)):
                        inte_value.append(f'{terms}x')
                        if upper_limit is not None and lower_limit is not None:
                          val = upper_limit - lower_limit
                          fin_val.append(float(terms) * val)

                    #for coefficients and power as one (+ve or -ve)
                    elif bool(re.match(power_one_decimal , terms)) :    
                        coefficient = float(terms[:-1])
                        new_coefficient = '{0:.3f}'.format(coefficient / 2)
                        inte_value.append(f'{new_coefficient}x^2')
                        if upper_limit is not None and lower_limit is not None:
                          val = (upper_limit ** 2) - (lower_limit ** 2)
                          fin_val.append(float(new_coefficient) * val)

                    #for coefficient and power as any number (+ve or -ve ) 
                    elif bool(re.match(coefficient_power_posi_d , terms)) :
                        power = float(terms[terms.index('^') + 1 : ])
                        coefficient = float(terms[ : terms.index('x')])
                        final_power = power + 1
                        final_coefficient = coefficient / final_power
                        final_coefficient = "{0:.3f}".format(final_coefficient)  
                        final_power = "{0:.3f}".format(final_power) 
                        final_exp = f'{final_coefficient}x^{final_power}' if final_power != 1 else f'{final_coefficient}x'  
                        final_exp = final_exp.replace("x^1.000", "x")
                        final_exp = final_exp.replace("x^0.000" , "")  
                        inte_value.append(final_exp)
                        if upper_limit is not None and lower_limit is not None:
                          val = (upper_limit ** float(final_power)) - (lower_limit ** float(final_power))
                          fin_val.append(float(final_coefficient) * val)
                        
                    #for no coefficient but with any power 
                    elif bool(re.match(only_power , terms)) :
                        power = float(terms[terms.index('^') + 1 : ])
                        final_power = power + 1  
                        final_coefficient = 1 / power if terms.index('x') == 0 else -1 / power 
                        final_coefficient = "{0:.3f}".format(final_coefficient)
                        final_power = "{0:.3f}".format(final_power)
                        final_exp = f'{final_coefficient}x^{final_power}' if final_power != 1 else f'{final_coefficient}x'
                        final_exp = final_exp.replace("x^1.000", "x")
                        final_exp = final_exp.replace("x^0.000" , "") 
                        inte_value.append(final_exp)
                        if upper_limit is not None and lower_limit is not None:
                          val = (upper_limit ** float(final_power)) - (lower_limit ** float(final_power))
                          fin_val.append(float(final_coefficient) * val)

                return (tostring(inte_value) + " + c", float('{0:.3f}'.format(sum(fin_val)))) if upper_limit != None and lower_limit != None else (tostring(inte_value) + " + c" , None)

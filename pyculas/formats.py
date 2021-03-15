from collections import Counter

def simplify(w : list) -> list:
    num_sum = 0
    w1 = []
    for i in range(len(w)) :

        if w[i][0] == 'x' : w1.append('1' + w[i])
        elif w[i][ : 2] == '-x' : w1.append('-1' + w[i][w[i].index('x') : ])   
        elif 'x' not in w[i] :  num_sum += float(w[i])
        else : w1.append(w[i])

    p = w1
    w1 = [a[a.index('x') : ] for a in w1]

    x = Counter(w1)
    similar = []

    if any([ x > 1 for x in list(x.values())]) :
        for h in x.keys() :
            temp = [float(p[t][ : p[t].index('x')]) for t in range(len(w1)) if w1[t] == h]
            temp_sum = sum(temp)
            if temp_sum != 0:
               if temp_sum == -1 : final_exp =  '-' + h
               elif temp_sum == 1 : final_exp = h
               else : final_exp = str(temp_sum) + h 
               similar.append(final_exp)
        
        if num_sum != 0 : similar.append(str(num_sum))    
        return similar

    else :
        if num_sum != 0 : p.append(str(num_sum))   
        return p
       

def toarray(w : str) -> list :

    w = w.replace(" ","")
    q = []
    s = "+"
    old = s
    c=0

    for x in range(len(w)) :
        if w[x] == "-" and w[x-1] != "^" and x != 0 :
            old = s
            temp = old+w[x-c:x]
            temp = temp.replace("+","")
            q.append(temp)
        
            s = "-"
            c = 0

        elif w[x] == "+" and x != 0:
            old = s
            temp = old+w[x-c:x]
            temp = temp.replace("+","")
            q.append(temp)
            
            s = "+"
            c = 0  

        elif x == len(w)-1:
            old = s
            temp = old+w[x-c:x+1]
            temp = temp.replace("+","")
            q.append(temp)

        else : c += 1

    return q  


def tostring(q : list) -> str:        
            
    fin_exp = ""

    for x in range(len(q)):

        if x != 0 :

            if '-' == q[x][0] : fin_exp +=  f'- {q[x][1:]} '    

            else : fin_exp += f'+ {q[x]} '                   

        else : fin_exp += f'{q[x]} ' 

    return fin_exp[:-1]

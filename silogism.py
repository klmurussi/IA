class Rule:
    def __init__(self, variable, conclusion):
        self.variable = variable
        self.conclusion = conclusion

# Define the variables
variables = {'gregos', 'homens', 'mortais',
         'macacos', 'mamiferos', 'animais',
         'rosas', 'flores', 'plantas',
         'circo', 'palhaço', 'elefante'}

# Define the premisses
premisses = [
    Rule(variable=['gregos', 'homens'], conclusion='os gregos são homens'),
    Rule(variable=['homens', 'mortais'], conclusion='os homens são mortais'), 
    Rule(variable=['macacos', 'mamiferos'], conclusion='os macacos são mamiferos'),
    Rule(variable=['mamiferos', 'animais'], conclusion='os mamiferos são animais'),
    Rule(variable=['rosas', 'flores'], conclusion='as rosas são flores'),
    Rule(variable=['flores', 'plantas'], conclusion='as flores são plantas'),
]

def proven (a, b, c):
    check1 = False
    check2 = False
    check3 = False
    for p in premisses:
        if p.variable == [a,b]:
            check1 = True
        if p.variable == [b,c]:
            check2 = True
        if p.variable == [a,c]:
            check3 = True
    if check1 and check2 and check3==False:
        return True
    else:
        return False

def is_proved (variables):
    for a in variables:
        for b in variables:
            for c in variables:
                if proven (a, b, c):
                    print ("Conclusão:") 
                    print (a + " são " + b)
                    print (b + " são " + c)
                    premisse = "Logo, " + a + " são " + c
                    print (premisse + '\n')
                    premisses.append(Rule(variable=[a,c], conclusion=premisse))
                    continue
is_proved(variables)

#for v in premisses:
    #print (v.conclusion)
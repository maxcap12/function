# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

def derive(exp1: str, exp2: str, sign: str):
    
    if sign == '+':
        return val_deriv(exp1) + val_deriv(exp2)
    
    elif sign == '-':
        return val_deriv(exp1) - val_deriv(exp2)
    
    elif sign == '/':
        return calcul( ( val_deriv(exp1) * exp2 - val_deriv(exp2) * exp1 ) / pow(exp2, 2) )
    
    elif sign == '*':
        return calcul( val_deriv(exp1) * exp2 + val_deriv(exp2) * exp1 )
        
    elif sign == '^':
        return calcul( calcul( val_deriv(exp1), exp2, '*'), calcul( exp1, exp2, '**'), '*')
    

def calcul(exp1, exp2, sign):
    pass


def val_deriv(exp: str) -> int:
    
    if exp.isdigit():
        return 0
    
    elif exp == 'x':
        return 1
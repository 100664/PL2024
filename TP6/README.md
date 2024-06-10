# Autor

Martim Redondo, a100664

## TERMINAIS 
T = {'?','=', '!', '+', '-', '*', '/', '(', ')', id, num}

## Não Terminais

N = {Z, Exps, Exp, Exp2, OP, OP1}

## Símbolo Inicial

Z

## Produções


 S -> '?' id           
    | '!' Exps             
    | id '=' Exp         
Exps -> Exp OP        
OP -> &
    |'+' Exps         
    | '-' Exps                        
Exp -> Exp2 Op1         
Op1 -> &
    |'*' Exp          
    | '/' Exp                             
Exp2 -> '(' Exps ')'     
    | num                
    | id                


## Exemplo

?a 
b=a*2/(27-3)
!a+b
c=a*b/(a/b)

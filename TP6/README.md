T =  {'?','=', '!', '+', '-', '*', '/', '(', ')', id, num}
N = {Z, Exps, Exp, Exp2, OP, OP1}
Z = Z
P = {
    S -> '?' id           
      | '!' Exps             
      | id '=' Exp         
    Exps -> Exp OP        
    OP -> '+' Exps         
        | '-' Exps          
        | &                
    Exp -> Exp2 Op1         
    Op1 -> '*' Exp          
        | '/' Exp           
        | &                   
    Exp2 -> '(' Exps ')'     
        | num                
        | id                
}
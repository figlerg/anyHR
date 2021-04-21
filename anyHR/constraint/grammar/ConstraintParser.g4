parser grammar ConstraintParser ;

options {
	tokenVocab = ConstraintLexer ;
}

lra
    :
    expression LEQ expression                                           #LRA_LEQ
    | expression GEQ expression                                         #LRA_GEQ
    | expression LESS expression                                        #LRA_Less
    | expression GREATER expression                                     #LRA_Greater
    | expression EQ expression                                          #LRA_Eq
    | expression NEQ expression                                         #LRA_Neq
    | expression IN LPAREN expression COMMA expression RPAREN           #LRA_In
    ;

expression
	:
	Identifier                                                          #ExpressionVariable
	| literal                                                           #ExpressionConstant
	| LPAREN expression RPAREN                                          #ExpressionParanthesis
	| EULER EXP expression                                              #ExpressionExponential
    | expression TIMES expression                                       #ExpressionMultiplication
	| expression PLUS expression                                        #ExpressionAddition
	| expression MINUS expression                                       #ExpressionSubtraction
    ;

literal
	: IntegerLiteral		
	| RealLiteral
	| MINUS literal
	;

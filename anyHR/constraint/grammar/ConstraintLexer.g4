lexer grammar ConstraintLexer ;

EULER
    : 'e' ;

EXP
    : '**' ;

MINUS
    : '-' ;

PLUS
    : '+' ;

TIMES
    : '*' ;

LPAREN
	: '(' ;

RPAREN
	: ')' ;

LSQBRACKET
    : '[' ;

RSQBRACKET
    : ']' ;

LEQ
    : '<=' ;

GEQ
    : '>=' ;

LESS
    : '<' ;

GREATER
    : '>' ;

EQ
    : '==' ;

NEQ
    : '!=' ;


COMMA
    : ',' ;

IN
    : 'in' ;

IntegerLiteral
	: DecimalNumeral
	| HexNumeral
	| BinaryNumeral ;

fragment DecimalNumeral
	: '0'
	| NonZeroDigit (Digits? | Underscores Digits) ;

fragment Digits
	: Digit (DigitsAndUnderscores? Digit)? ;

fragment Digit
	: '0'
	| NonZeroDigit ;

fragment NonZeroDigit
	: [1-9] ;

fragment DigitsAndUnderscores
	: DigitOrUnderscore+ ;

fragment DigitOrUnderscore
	: Digit
	| '_' ;

fragment Underscores
	: '_'+ ;

fragment HexNumeral
	: '0' [xX] HexDigits ;

fragment HexDigits
	: HexDigit (HexDigitsAndUnderscores? HexDigit)? ;

fragment HexDigit
	: [0-9a-fA-F] ;

fragment HexDigitsAndUnderscores
	: HexDigitOrUnderscore+ ;

fragment HexDigitOrUnderscore
	: HexDigit
	| '_' ;

fragment BinaryNumeral
	: '0' [bB] BinaryDigits ;

fragment BinaryDigits
	: BinaryDigit (BinaryDigitsAndUnderscores? BinaryDigit)? ;

fragment BinaryDigit
	: [01] ;

fragment BinaryDigitsAndUnderscores
	: BinaryDigitOrUnderscore+ ;


fragment BinaryDigitOrUnderscore
	: BinaryDigit
	| '_' ;

RealLiteral
	: DecimalRealLiteral ;

fragment DecimalRealLiteral
	: Digits '.' Digits? ExponentPart?
	| '.' Digits ExponentPart?
	| Digits ExponentPart
	;

fragment ExponentPart
	: ExponentIndicator SignedInteger ;

fragment ExponentIndicator
	: [eE] ;

fragment SignedInteger
	: Sign? Digit+ ;

fragment Sign
	: [+-] ;


Identifier
	: ((IdentifierStart)(IdentifierPart)*) ;


fragment IdentifierStart
	: (LetterOrUnderscore | '$') ;

fragment IdentifierPart
	: ( IdentifierStart | Digit | '.' | '/' ) ;

fragment LetterOrUnderscore
	: (Letter | '_') ;

fragment Letter
	: [A-Za-z] ;

// Whitespace and comments
//
LINE_TERMINATOR
	: [\n] -> skip ;

WHITESPACE
	: [ \t\r\u000C]+ -> skip ;

COMMENT
	: '/*' .*? '*/' -> skip ;

LINE_COMMENT
	: '//' ~[\r\n]* -> skip ;


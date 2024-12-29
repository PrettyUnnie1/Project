// Sample.g4
grammar Sample;

// Parser Rules
sentence
    : word+ EOF
    ;

// Lexer Rules
word
    : POSITIVE
    | NEGATIVE
    | OTHER
    ;

// Define Positive Words (Case-Insensitive)
POSITIVE
    : [Aa][mM][aA][zZ][iI][nN][gG]
    | [Aa][wW][eE][sS][oO][mM][eE]
    | [Aa][pP][pP][rR][eE][cC][iI][aA][tT][eE]
    | [Bb][eE][aA][uU][tT][iI][fF][uU][lL]
    | [Bb][rR][iI][lL][lL][iI][aA][nN][tT]
    | [Cc][hH][eE][eE][rR][fF][uU][lL]
    | [Cc][hH][eE][rR][iI][sS][hH]
    | [Cc][oO][mM][fF][oO][rR][tT]
    | [Dd][eE][lL][iI][gG][hH][tT]
    | [Dd][eE][lL][iI][gG][hH][tT][fF][uU][lL]
    | [Ee][xX][cC][eE][lL][lL][eE][nN][tT]
    | [Ff][aA][nN][tT][aA][sS][tT][iI][cC]
    | [Ff][rR][iI][eE][nN][dD][lL][yY]
    | [Gg][oO][oO][dD]
    | [Gg][rR][eE][aA][tT]
    | [Hh][aA][pP][pP][yY]
    | [Hh][aA][nN][dD][lL][oO][vV][eE]
    | [Ii][nN][cC][rR][eE][dD][iI][bB][lL][eE]
    | [Jj][oO][yY]
    | [Jj][oO][yY][fF][uU][lL]
    | [Kk][iI][nN][dD]
    | [Ll][iI][kK][eE]
    | [Ll][oO][vV][eE]
    | [Ll][oO][vV][eE][lL][yY]
    | [Mm][aA][rR][vV][eE][lL][oO][uU][sS]
    | [Nn][iI][cC][eE]
    | [Oo][uU][tT][sS][tT][aA][nN][dD][iI][nN][gG]
    | [Pp][eE][rR][fF][eE][cC][tT]
    | [Pp][lL][eE][aA][sS][aA][nN][tT]
    | [Pp][eE][aA][cC][eE]
    | [Ss][aA][tT][iI][sS][fF][aA][cC][tT][oO][rR][yY]
    | [Ss][uU][pP][eE][rR][bB]
    | [Ss][uU][cC][cC][eE][sS][sS]
    | [Tt][rR][iI][uU][mM][pP][hH]
    | [Vv][aA][lL][uU][eE]
    | [Bb][eE][nN][eE][fF][iI][tT]
    | [Bb][lL][eE][sS][sS][iI][nN][gG]
    | [Cc][oO][mM][fF][oO][rR][tT]
    | [Ee][nN][jJ][oO][yY][mM][eE][nN][tT]
    | [Hh][aA][pP][pP][iI][nN][eE][sS][sS]
    | [Hh][oO][nN][oO][rR]
    | [Pp][eE][aA][cC][eE]
    | [Ss][uU][cC][cC][eE][sS][sS]
    | [Tt][rR][iI][uU][mM][pP][hH]
    ;


// Define Negative Words (Case-Insensitive)
NEGATIVE
    : [Aa][bB][hH][oO][rR]
    | [Aa][bB][uU][sS][eE]
    | [Aa][nN][gG][eE][rR]
    | [Aa][nN][nN][oO][yY][iI][nN][gG]
    | [Aa][wW][fF][uU][lL]
    | [Bb][aA][dD]
    | [Bb][lL][aA][mM][eE]
    | [Cc][rR][iI][tT][iI][cC][iI][zZ][eE]
    | [Dd][iI][sS][gG][uU][sS][tT][iI][nN][gG]
    | [Dd][iI][sS][lL][iI][kK][eE]
    | [Dd][iI][sS][aA][pP][pP][oO][iI][nN][tT][mM][eE][nN][tT]
    | [Dd][rR][eE][aA][dD][fF][uU][lL]
    | [Ff][rR][uU][sS][tT][rR][aA][tT][iI][nN][gG]
    | [Hh][aA][tT][rR][eE][dD]
    | [Hh][aA][tT][eE]
    | [Hh][oO][rR][rR][iI][bB][lL][eE]
    | [Ii][gG][nN][oO][rR][eE]
    | [Ii][rR][rR][iI][tT][aA][tT][iI][nN][gG]
    | [Ii][nN][sS][uU][lL][tT]
    | [Ll][oO][sS][sS]
    | [Mm][iI][sS][eE][rR][yY]
    | [Mm][iI][sS][sS][eE][rR][iI][eE]
    | [Nn][aA][sS][tT][yY]
    | [Nn][eE][gG][aA][tT][iI][vV][eE]
    | [Pp][aA][iI][nN][fF][uU][lL]
    | [Pp][rR][oO][bB][lL][eE][mM]
    | [Rr][eE][gG][rR][eE][tT]
    | [Rr][eE][jJ][eE][cC][tT]
    | [Ss][oO][rR][rR][oO][wW]
    | [Ss][tT][rR][eE][sS][sS]
    | [Tt][eE][rR][rR][iI][bB][lL][eE]
    | [Tt][rR][oO][uU][bB][lL][eE]
    | [Uu][nN][pP][lL][eE][aA][sS][aA][nN][tT]
    | [Uu][nN][sS][aA][tT][iI][sS][fF][aA][cC][tT][oO][rR][yY]
    | [Uu][gG][lL][yY]
    | [Ww][oO][rR][tT][hH][lL][eE][sS][sS]
    | [Ww][oO][rR][sS][tT]
    | [Hh][oO][rR][rR][eE][nN][dD][oO][uU][sS]
    | [Aa][wW][fF][uU][lL][nN][eE][sS][sS]
    | [Aa][wW][fF][uU][lL][nN][eE][sS][sS][nN][eE][sS][sS]
    ;

// Match any other word (consisting of alphabetic characters)
OTHER
    : [a-zA-Z]+
    ;

// Whitespace handling (skip spaces, tabs, newlines)
WS
    : [ \t\r\n]+ -> skip
    ;

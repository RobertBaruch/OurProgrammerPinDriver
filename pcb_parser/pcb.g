grammar pcb;

// Parser rules

// The first WORD is the name of the node.
// Everything else is the node's content.

node : '(' WORD content* ')' ;

content : WORD | STRING | node ;

// Lexer rules. These are matched in order from top to bottom,
// except strings from parser rules which are matched first.

// Strings are double-quoted. You can put anything in a string, but
// double-quotes, backslashes, newlines, and tabs are escaped with
// a backslash.

STRING : '"' ( ESCAPED | . )*? '"' ;
fragment ESCAPED : '\\' [rnt"\\] ;

WORD : ~[ \n\t\r()"]+ ;

// skip whitespace (they just separate tokens)

WS : [ \n\t\r]+ -> skip;

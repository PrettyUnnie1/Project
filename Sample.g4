grammar Sample;

// Quy tắc bắt đầu
program: WORD+;

// Quy tắc lexer để nhận diện từ
WORD: [a-zA-Z]+ | [a-zA-Z];  // Để nhận diện từ gồm một chữ cái đơn

// Quy tắc bỏ qua khoảng trắng
WS: [ \t\r\n]+ -> skip;

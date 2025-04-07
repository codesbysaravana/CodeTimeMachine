Identification Division.
Program-id. HELLO-WORLD.
Data Division.
Working-Storage Section.
01 User-Num1 PIC 9(9).
01 User-Num2 PIC 9(9).
01 User-Address.
05 User-City PIC X(5).
05 User-Country PIC X(5).
05 User-Index PIC 9(6).
05 User-Phone PIC 9(6).
Procedure Division.
000-Main-Logic.
Perform 100-Print-User.
Stop Run.
100-Print-User.
Move 123456789 To User-Num1.
Move User-Num1 To User-Num2.
Move 'Wenceslav Square 846/1' To User-Address.
Move 'Prague' To User-City.
Move 'CZ' To User-Country.
Move 11000 To User-Index.
Move 777123456 To User-Phone.
Display "User-Num1     : " User-Num1.
Display "User-Num2     : " User-Num2.
Display "User-Address  : " User-Address.
Display "User-City     : " User-City.
Display "User-Country  : " User-Country.
Display "User-Index    : " User-Index.
Display "User-Phone    : " User-Phone.
End program HELLO-WORLD.
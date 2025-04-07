Identification Division.
Program-id. HELLO-WORLD.
Data Division.
Working-Storage Section.
01 SUBNAME PIC 9(9).
01 Variable PIC 9(9).
Procedure Division.
call SUBNAME  using VARIABLE.
call SUBNAME using by VALUE Variable.
call SUBNAME  using by content VARIABLE.
call SUBNAME  using by reference VARIABLE.
End program HELLO-WORLD.
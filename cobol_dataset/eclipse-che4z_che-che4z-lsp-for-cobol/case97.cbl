       IDENTIFICATION DIVISION.
       PROGRAM-ID.    PROG.
       PROCEDURE DIVISION.
           EXEC SQL WHENEVER SQLERROR GOTO HANDLE-SQL-ERROR  END-EXEC.
           GO TO CALCULATION
           GOBACK.

       CALCULATION SECTION.
           EXEC SQL ROLLBACK WORK END-EXEC.

       CALCULATION-END.
           GOBACK.

       HANDLE-SQL-ERROR.
           DISPLAY "HANDLE SQL ERROR".

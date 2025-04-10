000100 IDENTIFICATION DIVISION.
000100 PROGRAM-ID. HELLO.
000100
000100 DATA DIVISION.
000100 WORKING-STORAGE SECTION.
000100   EXEC SQL
000100     INCLUDE SQLSCRIPT
000100   END-EXEC.
000100
000100   EXEC SQL
000100     INCLUDE TEACHER
000100   END-EXEC.
000100
000100   EXEC SQL BEGIN DECLARE SECTION
000100   END-EXEC.
000100     01 WS-TEACHER-REC.
000100     05 WS-TEACHER-ID PIC 9(10).
000100   EXEC SQL END DECLARE SECTION
000100   END-EXEC.
000100
000100 PROCEDURE DIVISION.
000100   EXEC SQL
000100     SELECT TEACHER-ID
000100       INTO :WS-TEACHER-ID FROM TEACHER
000100       WHERE TEACHER-ID=1
000100   END-EXEC.
000100
000100   IF SQLCODE=0
000100   DISPLAY WS-TEACHER-RECORD
000100   ELSE DISPLAY 'Error'
000100   END-IF.
000100   STOP RUN.
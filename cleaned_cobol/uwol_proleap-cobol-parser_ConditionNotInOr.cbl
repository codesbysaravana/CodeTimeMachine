IDENTIFICATION DIVISION.
PROGRAM-ID. CONDTN.
PROCEDURE DIVISION.
IF SOME-DATA IN SOME-OTHER-DATA NOT = ('A' OR 'B')
STOP RUN
END-IF.
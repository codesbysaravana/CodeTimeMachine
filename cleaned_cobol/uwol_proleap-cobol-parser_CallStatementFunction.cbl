IDENTIFICATION DIVISION.
PROGRAM-ID. CALLSTMT.
PROCEDURE DIVISION.
CALL "C$TOUPPER"
USING
TEXT-VALUE-2
BY VALUE LENGTH 1.
CALL "C$JUSTIFY"
USING
TEXT-VALUE-2
"C".
CALL "C$TOUPPER"
USING TO-UPPER-CASE
BY VALUE
LENGTH TO-UPPER-CASE.
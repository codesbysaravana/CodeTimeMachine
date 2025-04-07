IDENTIFICATION DIVISION.
PROGRAM-ID.  Listing15-9.
AUTHOR.  Michael Coughlan.
DATA DIVISION.
WORKING-STORAGE SECTION.
01 OrdPos        PIC 99.
01 TableValues   VALUE "123411457429130938637306851419883522700467".
02 Num       PIC 99 OCCURS 21 TIMES.
01 idx           PIC 9.
01 xString       PIC X(45)
VALUE "This string is 33 characters long".
01 xWord         PIC X(10).
01 CharCount     PIC 99.
01 TextLength    PIC 99.
PROCEDURE DIVISION.
Begin.
DISPLAY "eg1. The character in position 88 is = " FUNCTION CHAR(88)
DISPLAY SPACES
DISPLAY "eg2. My name is " FUNCTION CHAR(78)  FUNCTION CHAR(106)
FUNCTION CHAR(108) FUNCTION CHAR(102)
DISPLAY SPACES
MOVE FUNCTION ORD("A") TO OrdPos
DISPLAY "eg3. The ordinal position of A is = " OrdPos
DISPLAY SPACES
DISPLAY "eg4. The sixth letter of the alphabet is "
FUNCTION CHAR(FUNCTION ORD("A") + 5)
DISPLAY SPACES
MOVE FUNCTION ORD-MAX("t" "b" "x" "B" "4" "s" "b") TO OrdPos
DISPLAY "eg5. Highest character in the list is at pos " OrdPos
DISPLAY SPACES
MOVE FUNCTION ORD-MIN("t" "b" "x" "B" "4" "s" "b") TO OrdPos
DISPLAY "eg6. Lowest character in the list is at pos " OrdPos
DISPLAY SPACES
MOVE FUNCTION ORD-MAX(Num(ALL)) TO OrdPos
DISPLAY "eg7. Highest value in the table is at pos " OrdPos
DISPLAY SPACES
DISPLAY "eg8. Highest value in the table = " Num(FUNCTION ORD-MAX(Num(ALL)))
DISPLAY SPACES
DISPLAY "eg9."
PERFORM VARYING idx FROM 1 BY 1 UNTIL idx > 3
DISPLAY "TopPos " idx " = " Num(FUNCTION ORD-MAX(Num(ALL)))
MOVE ZEROS TO Num(FUNCTION ORD-MAX(Num(ALL)))
END-PERFORM
DISPLAY SPACES
DISPLAY "eg10. The length of xString is " FUNCTION LENGTH(xString) " characters"
DISPLAY SPACES
INSPECT FUNCTION REVERSE(xString) TALLYING CharCount
FOR LEADING SPACES
COMPUTE TextLength = FUNCTION LENGTH(xString) - CharCount
DISPLAY "eg11. The length of text in xString is " TextLength " characters"
DISPLAY SPACES
DISPLAY "eg12."
MOVE ZEROS TO CharCount
DISPLAY "Enter a word - " WITH NO ADVANCING
ACCEPT xWord
INSPECT FUNCTION REVERSE(xWord) TALLYING CharCount
FOR LEADING SPACES
IF FUNCTION UPPER-CASE(xWord(1:FUNCTION LENGTH(xWord) - CharCount)) EQUAL TO
FUNCTION UPPER-CASE(FUNCTION REVERSE(xWord(1:FUNCTION LENGTH(xWord)- CharCount)))
DISPLAY xWord " is a palindrome"
ELSE
DISPLAY xWord " is not a palindrome"
END-IF
STOP RUN.
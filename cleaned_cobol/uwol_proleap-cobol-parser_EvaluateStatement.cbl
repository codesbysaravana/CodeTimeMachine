IDENTIFICATION DIVISION.
PROGRAM-ID. EVALSTMT.
PROCEDURE DIVISION.
EVALUATE SOMEAGE ALSO SOMEAGE2 ALSO SOMEAGE3
WHEN 0 THROUGH 25 PERFORM SOMEPROC1
WHEN 25 THROUGH 50 PERFORM SOMEPROC2
WHEN 50 THROUGH 74 ALSO 75 PERFORM SOMEPROC3
WHEN OTHER PERFORM SOMEPROC4
END-EVALUATE.
IDENTIFICATION DIVISION.
PROGRAM-ID. LINECONT.
DATA DIVISION
77   SQL-INS            PIC X(150) VALUE
"INSERT INTO EMP (EMPNO,ENAME,JOB,SAL,DEPTNO)
-        " VALUES (:EMPNO,:ENAME,:JOB,:SAL,:DEPTNO)".
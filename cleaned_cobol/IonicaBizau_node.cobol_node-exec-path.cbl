IDENTIFICATION DIVISION.
PROGRAM-ID. EXEC_NODEJS_FILE.
DATA DIVISION.
WORKING-STORAGE SECTION.
01 COMMAND_TO_RUN PIC X(200) value SPACES.
LINKAGE SECTION.
01 NODEJS_FILE_PATH PIC X(100).
PROCEDURE DIVISION USING NODEJS_FILE_PATH.
STRING 'node ' DELIMITED BY SPACE
' '   DELIMITED BY SIZE
NODEJS_FILE_PATH DELIMITED BY SPACE
INTO COMMAND_TO_RUN
CALL 'SYSTEM' USING COMMAND_TO_RUN
END-CALL
EXIT PROGRAM.
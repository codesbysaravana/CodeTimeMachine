IDENTIFICATION DIVISION.
PROGRAM-ID.  Listing4-1.
AUTHOR.  Michael Coughlan.
DATA DIVISION.
WORKING-STORAGE SECTION.
01  UserName           PIC X(20).
01 CurrentDate.
02  CurrentYear     PIC 99.
02  CurrentMonth    PIC 99.
02  CurrentDay      PIC 99.
01 DayOfYear.
02  FILLER          PIC 99.
02  YearDay         PIC 9(3).
01 CurrentTime.
02  CurrentHour     PIC 99.
02  CurrentMinute   PIC 99.
02  FILLER          PIC 9(4).
01 Y2KDate.
02 Y2KYear          PIC 9(4).
02 Y2KMonth         PIC 99.
02 Y2KDay           PIC 99.
01 Y2KDayOfYear.
02 Y2KDOY-Year      PIC 9(4).
02 Y2KDOY-Day       PIC 999.
PROCEDURE DIVISION.
Begin.
DISPLAY "Please enter your name - " WITH NO ADVANCING
ACCEPT  UserName
DISPLAY "**********************"
ACCEPT CurrentDate  FROM DATE
ACCEPT DayOfYear    FROM DAY
ACCEPT CurrentTime  FROM TIME
ACCEPT Y2KDate      FROM DATE YYYYMMDD
ACCEPT Y2KDayOfYear FROM DAY YYYYDDD
DISPLAY "Name is " UserName
DISPLAY "Date is " CurrentDay "-"  CurrentMonth "-" CurrentYear
DISPLAY "Today is day " YearDay " of the year"
DISPLAY "The time is " CurrentHour ":" CurrentMinute
DISPLAY "Y2KDate is " Y2kDay SPACE Y2KMonth SPACE Y2KYear
DISPLAY "Y2K Day of Year is " Y2KDoy-Day " of " Y2KDOY-Year
STOP RUN.
MOVE COND TO COND-BACKUP
MOVE 1 TO COND
$conditions$
IF COND NOT = 0
    CALL "LootTables-ExplosionDecay" USING ITEM-COUNT(POOL-SIZE)
END-IF
MOVE COND-BACKUP TO COND

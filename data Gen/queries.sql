-- Query to print last n rows in table without sorting 
-- First store number of rows to some variable
-- Then print last n rows using offset
Declare @cont as bigint

SELECT count(*) FROM table_name to @count;
SELECT * FROM table_name LIMIT @count OFFSET @count - n;

sotr
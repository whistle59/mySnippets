-- count consecutives days
-- https://stackoverflow.com/questions/26117179/sql-count-consecutive-days

SELECT
    UserName,
    UserDate,
    UserCode,
    GroupingSet = DATEADD(DAY, 
                     -ROW_NUMBER() OVER(PARTITION BY UserName 
                      ORDER BY UserDate), UserDate)
    FROM    UserTable;


-- option 2: Calculate the serie length
WITH groups AS ( 
SELECT  RANK() OVER (ORDER BY date_completed) AS row_number, 
            date_completed, 
            DATEADD (day, -RANK() OVER (ORDER BY date_completed), 
            date_completed) AS date_group 
FROM lesson_completed) 

SELECT  COUNT(*) AS days_streak, 
        MIN (date_completed) AS min_date, 
        MAX (date_completed) AS max_date 
FROM groups 
GROUP BY date_group; 

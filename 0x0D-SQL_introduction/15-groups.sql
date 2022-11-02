-- groups

SELECT score, count(*) AS NUMBER FROM second_table GROUP BY score ORDER BY NUMBER DESC;

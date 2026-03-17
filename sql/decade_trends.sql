SELECT 
    CAST(FLOOR(Released_Year / 10) * 10 AS INT64) AS Decade, 
    COUNT(*) AS Movie_Count, 
    SUM(No_of_Votes) AS Total_Votes
FROM 
    `imdb-movies-project.imdb_movies_data.Movies_Table`
GROUP BY 
    Decade
ORDER BY 
    Decade DESC;

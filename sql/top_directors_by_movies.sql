SELECT 
    Director, 
    COUNT(Series_Title) AS Total_Movies, 
    ROUND(AVG(IMDB_Rating), 2) AS Average_Rating
FROM 
    `imdb-movies-project.imdb_movies_data.Movies_Table`
GROUP BY 
    Director
HAVING 
    Total_Movies > 5
ORDER BY 
    Average_Rating DESC
LIMIT 10;
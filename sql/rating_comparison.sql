SELECT 
    Series_Title, 
    IMDB_Rating, 
    (Meta_score / 10) AS Normalized_Meta_score,
    ABS(IMDB_Rating - (Meta_score / 10)) AS Rating_Gap
FROM `imdb-movies-project.imdb_movies_data.Movies_Table`
WHERE Meta_score IS NOT NULL
ORDER BY Rating_Gap DESC;

🎬 IMDB Top 1000 Movies: ETL & Cinematic Intelligence
An end-to-end Data Engineering and Analytics project. This repository demonstrates a complete pipeline: cleaning raw movie data with Python, processing it in Google BigQuery, and visualizing multi-dimensional cinematic insights in Looker Studio.

📊 Market Insights & Visualizations
The following analysis was performed to uncover trends in movie production, director performance, and the gap between audience and critics.

1. Top 10 Directors by Movie Count(page1.png)
Description: A Bar Chart identifying the most consistent directors in the top 1000 list.

Insight: Highlights legends like Akira Kurosawa and Martin Scorsese, showcasing their long-term dominance and impact on cinema history.

2. Audience (IMDb) vs. Critics (Metascore) Gap
Description: A Grouped Bar Chart comparing Audience Ratings against Normalized Meta Scores (scaled to 10).

Insight: Reveals the "Rating Gap"; identifying movies that were "Audience Favorites" (like I Am Sam) despite being panned by professional critics.

3. Cinema Growth & Production Trends by Decade
Description: An Area Chart showing the distribution of top-rated movies across different decades (1920s - 2020s).

Insight: Visualizes the "Golden Age" of cinema and the exponential growth in high-quality productions during the 1990s and 2000s.

📂 Project Structure
Plaintext
├── data/
│   ├── imdb_top_1000.csv       # Raw dataset (Input)
│   └── Cleandimdb_top_1000.csv # Cleaned dataset (Output)
├── scripts/
│   └── clean_data.py           # Python ETL logic & cleaning
├── sql/
│   ├── director_analytics.sql  # Ranking top directors with > 5 movies
│   ├── decade_trends.sql       # Logic for grouping movies into decades
│   └── rating_comparison.sql   # Normalizing Metascore for fair comparison
├── page1.png                   # Chart: Top Directors
├── page2.png                   # Chart: Rating Gap
├── page3.png                   # Chart: Decade Analysis
└── README.md                   # Project documentation
🛠️ Technical Stack
Language: Python 3.x (Pandas for ETL)

Database: Google BigQuery (SQL)

Visualization: Looker Studio

Environment: VS Code

⚙️ How to Reproduce
Clone the Repo: git clone https://github.com/MohammedAlrehaili/IMDB-Movies-ETL-Analysis.git

Run ETL: Execute python scripts/clean_data.py to generate the cleaned dataset.

BigQuery: Upload the cleaned CSV to BigQuery and execute scripts found in the /sql folder.

Dashboard: Connect BigQuery to Looker Studio to view the visualizations.

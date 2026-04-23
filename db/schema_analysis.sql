CREATE MATERIALIZED VIEW hn_analysis AS 
SELECT 
    author, 
    COUNT(*) AS num_posts, 
    AVG(score) AS avg_score
FROM hn_clean
GROUP BY author; 
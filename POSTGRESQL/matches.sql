CREATE TABLE matches (
    match_id SERIAL PRIMARY KEY,
    home_team VARCHAR(100),
    away_team VARCHAR(100),
    closing_odds_1 DECIMAL(5,2), -- Απόδοση για νίκη γηπεδούχου στο κλείσιμο
    result VARCHAR(10)          -- '1', 'X', '2'
);
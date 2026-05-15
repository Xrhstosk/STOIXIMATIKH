CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    user_type_label VARCHAR(20) -- Εδώ θα γράψουμε μετά "Sharp" ή "Casual" για επαλήθευση
);
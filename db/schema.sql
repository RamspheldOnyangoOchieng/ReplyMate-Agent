CREATE TABLE IF NOT EXISTS products (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    embedding VECTOR
);

CREATE TABLE IF NOT EXISTS chat_log (
    id SERIAL PRIMARY KEY,
    sender TEXT,
    message TEXT,
    response TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
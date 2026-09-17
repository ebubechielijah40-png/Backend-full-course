-- Library Catalog schema
-- Run against a PostgreSQL database, e.g.:
--   createdb library_catalog
--   psql library_catalog -f schema.sql

CREATE TABLE authors (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    author_id INTEGER REFERENCES authors(id),
    available BOOLEAN DEFAULT TRUE
);

CREATE TABLE borrowers (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE loans (
    id SERIAL PRIMARY KEY,
    book_id INTEGER REFERENCES books(id),
    borrower_id INTEGER REFERENCES borrowers(id),
    loaned_on DATE NOT NULL
);

-- Sample data
INSERT INTO authors (name) VALUES ('Octavia Butler'), ('Ursula K. Le Guin');

INSERT INTO books (title, author_id, available) VALUES
    ('Kindred', 1, FALSE),
    ('Parable of the Sower', 1, TRUE),
    ('The Left Hand of Darkness', 2, TRUE);

INSERT INTO borrowers (name) VALUES ('Sam Rivera'), ('Jordan Lee');

INSERT INTO loans (book_id, borrower_id, loaned_on) VALUES
    (1, 1, '2026-09-01');

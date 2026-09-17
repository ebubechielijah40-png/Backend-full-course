-- Library Catalog: required queries
-- Run against the database created by schema.sql

-- 1. List every book with its author's name (JOIN)
SELECT books.title, authors.name AS author
FROM books
JOIN authors ON books.author_id = authors.id;

-- 2. List only available books
SELECT title FROM books WHERE available = TRUE;

-- 3. List all books by a specific author (JOIN + WHERE)
SELECT books.title
FROM books
JOIN authors ON books.author_id = authors.id
WHERE authors.name = 'Octavia Butler';

-- 4. List every book currently on loan, with the borrower's name
--    (JOIN across three tables)
SELECT books.title, borrowers.name AS borrower, loans.loaned_on
FROM loans
JOIN books ON loans.book_id = books.id
JOIN borrowers ON loans.borrower_id = borrowers.id;

-- 5. Mark a book as unavailable (UPDATE)
UPDATE books SET available = FALSE WHERE id = 2;

-- 6. Add a new loan (INSERT)
INSERT INTO loans (book_id, borrower_id, loaned_on)
VALUES (2, 2, '2026-09-10');

-- 7. Return a book: delete its loan record and mark it available again
DELETE FROM loans WHERE book_id = 1 AND borrower_id = 1;
UPDATE books SET available = TRUE WHERE id = 1;

-- 8. Count how many books each author has written (JOIN + GROUP BY)
SELECT authors.name, COUNT(books.id) AS book_count
FROM authors
LEFT JOIN books ON books.author_id = authors.id
GROUP BY authors.name;

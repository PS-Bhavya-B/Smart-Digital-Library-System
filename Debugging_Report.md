# Debugging Report

## Project Title
Smart Digital Library System

---

## 1. Introduction
The Smart Digital Library System is a Python-based application developed using Object-Oriented Programming (OOP) concepts. It manages a collection of books and provides recommendations based on the user's preferred genre.

As part of the project requirements, an intentional bug was introduced and later resolved using debugging techniques.

---

## 2. Bug Description
A bug was intentionally introduced in the book recommendation feature. The system displayed all books instead of filtering them based on the user's preferred genre.

---

## 3. Expected Result
The system should recommend only books that match the user's favorite genre.

**Example:**
If the preferred genre is "Fantasy", only Fantasy books should be shown.

**Expected Output:**
Recommended Books:
Harry Potter


---

## 4. Actual Result
The system displayed all books, regardless of the genre.

**Actual Output:**
Recommended Books:
Harry Potter
Data Structures
AI Basics


---

## 5. Root Cause
The error occurred due to an incorrect condition used in the recommendation logic.

**Faulty Code:**
```python
if book.get_rating() > 0:

---
## 6. Debugging Steps

1. Ran the program to observe the output.  
2. Noticed that all books were being recommended incorrectly.  
3. Added debug print statements to check values:

```python
print(book.get_genre(), user.get_favorite_genre())

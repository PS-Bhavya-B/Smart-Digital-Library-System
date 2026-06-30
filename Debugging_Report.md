# Debugging Report

## Project Title
Smart Digital Library System

---

## 1. Introduction
The Smart Digital Library System is a Python-based application developed using Object-Oriented Programming (OOP) concepts. The system manages a collection of books and provides recommendations based on the user's preferred genre.

As part of the project requirement, an intentional bug was introduced and later fixed using a structured debugging process.

---

## 2. Bug Description
A bug was introduced in the recommendation feature of the system. Instead of recommending books based on the user's preferred genre, the system displayed all books available in the library.

---

## 3. Expected Result
The system should recommend only those books that match the user's favorite genre.

Expected Output:

Recommended Books:
Harry Potter

---

## 4. Actual Result
The system displayed all books regardless of the genre.

Actual Output:

Recommended Books:
Harry Potter
Data Structures
AI Basics

---

## 5. Root Cause
The issue occurred due to an incorrect condition used in the recommendation logic.

Faulty Code:

if book.get_rating() > 0:

This condition always evaluates to true because all books have ratings greater than 0. As a result, every book was displayed without checking the genre.

---

## 6. Debugging Steps

1. Ran the program to observe the output.
2. Noticed that all books were being recommended incorrectly.
3. Added debug print statements to check values:
   
   print(book.get_genre(), user.get_favorite_genre())

4. Observed that the book genre and user preference were different.
5. Checked the condition used in the recommendation function.
6. Identified that the condition was not comparing genres.
7. Located the incorrect line of code causing the issue.

---

## 7. Screenshots

The following screenshots are included in the project:

- 1_bug_output.png – shows incorrect output
- 2_correct_output.png – shows correct output after fixing the bug
- 3_bug_code.png – shows faulty code
- 4_fixed_code.png – shows corrected code


All screenshots are placed inside the screenshots/ folder.

---

## 8. Final Fix

Corrected Code:

if book.get_genre().lower() == user.get_favorite_genre().lower():
    print(book.get_title())

This ensures that only books matching the user's preferred genre are displayed.

---

## 9. Result After Fix

After applying the fix, the system correctly recommends books based on the user's preference.

Correct Output:

Recommended Books:
Harry Potter

---

## 10. Conclusion

The bug was successfully identified and resolved using a systematic debugging approach. The issue was caused by incorrect logic in the condition statement, and after correcting it, the system now works as expected.

This demonstrates effective debugging skills along with proper implementation of Object-Oriented Programming concepts.

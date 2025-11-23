# Student Management System

A Python-based Command Line Interface (CLI) application designed to solve the real-world problem of manual data record-keeping. This project implements a persistent file-based database system to Add, View, and Search student records efficiently.

---

## 📋 Project Overview

### Problem Statement
Managing student data (Roll Numbers, Names, Marks) using physical paper or temporary variables is inefficient and prone to data loss.

### Solution
This application automates the process by storing data in a structured text file (`students.txt`). It demonstrates the Computer Science concept of **Data Persistence**—ensuring data remains available even after the program terminates.

---

## ⚙️ Technical Specifications

* **Language:** Python 3.x
* **Database:** Flat File System (`.txt`)
* **Data Delimiter:** Pipe symbol (`|`)
* **Interface:** CLI (Command Line Interface)
* **Modules:** `os` (Operating System interaction)

---

## 💻 Code Structure & Logic

The source code is modularized into specific functions to ensure readability and maintainability.

### 1. Data Serialization Format
The system uses a custom delimited format to store records.

> **Format:** `RollNo|Name|Marks`

**Why `|` (Pipe)?**
The pipe symbol is chosen over a comma (`,`) to prevent parsing errors if a student's name contains a comma (e.g., "Doe, John").

### 2. Module Breakdown

| Function | Logic & Complexity | Mode Used |
| :--- | :--- | :--- |
| **`add_student()`** | Accepts user input, formats the string using f-strings, and appends it to the file. | Append (`a`) |
| **`view_students()`** | Checks file existence using `os.path`, reads lines into a list, splits strings by delimiter, and formats output. | Read (`r`) |
| **`search_student()`** | Iterates linearly through the file (**O(n)** complexity). Stops execution (`break`) immediately upon finding a match to save resources. | Read (`r`) |
| **`main()`** | Contains the driver loop (`while True`) that keeps the application running until the user chooses to exit. | - |

---

## 🚀 Setup & Installation Instructions

Follow these steps to run the project on your local machine.

### Prerequisites
* Python (Version 3.0 or higher)

### Step 1: Download
Clone this repository or download the `main.py` file to your folder.

```bash
git clone [https://github.com/your-username/student-management-system.git](https://github.com/your-username/student-management-system.git)
cd student-management-system
```

### Step 2: Run the Application
Execute the script using the terminal:

Bash
```
python main.py
```
Note: The system will automatically create the students.txt database file upon the first entry. You do not need to create it manually.

### 📊 Usage Example
## Input:

Plaintext
```
Enter Roll No: 101
Enter Name: Amit Sharma
Enter Marks: 85
Stored Data (students.txt):
```
Plaintext

101|Amit Sharma|85
### Output (View Mode):

Plaintext
```
Roll       Name                 Marks     
----------------------------------------
101        Amit Sharma          85
```

import os

Data_base = "students.txt"

def add_student():
    print("\n--- Add New Student ---")
    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")

    line = f"{roll}|{name}|{marks}\n"

    with open(Data_base, "a") as f:
        f.write(line)
    
    print("Student saved successfully.")

def view_students():
    print("\n--- All Students ---")
    if not os.path.exists(Data_base):
        print("No data found.")
        return

    with open(Data_base, "r") as f:
        lines = f.readlines()
        
        print(f"{'Roll':<10} {'Name':<20} {'Marks':<10}")
        print("-" * 40)

        for line in lines:
            data = line.strip().split("|")
            if len(data) == 3:
                print(f"{data[0]:<10} {data[1]:<20} {data[2]:<10}")

def search_student():
    target = input("\nEnter Roll No to search: ")
    found = False

    if not os.path.exists(Data_base):
        print("No data found.")
        return

    with open(Data_base, "r") as f:
        for line in f:
            data = line.strip().split("|")
            if len(data) == 3:
                if data[0] == target:
                    print(f"Found: {data[1]} (Marks: {data[2]})")
                    found = True
                    break
    
    if not found:
        print("Student not found.")

def main():
    while True:
        print("\n1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Exit")
        
        ch = input("Enter choice: ")

        if ch == '1':
            add_student()
        elif ch == '2':
            view_students()
        elif ch == '3':
            search_student()
        elif ch == '4':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
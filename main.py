import json
import os

FILE = "attendance.json"

# Load data
def load_data():
    if not os.path.exists(FILE):
        return {}
    with open(FILE, "r") as f:
        return json.load(f)

# Save data
def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

attendance = load_data()

def add_subject():
    name = input("Enter subject name: ")
    if name in attendance:
        print("Subject already exists!")
    else:
        attendance[name] = {"present": 0, "total": 0}
        save_data(attendance)
        print("Subject added successfully!")

def mark_attendance():
    name = input("Enter subject name: ")
    if name not in attendance:
        print("Subject not found!")
        return

    status = input("Present? (y/n): ").lower()
    attendance[name]["total"] += 1

    if status == "y":
        attendance[name]["present"] += 1

    save_data(attendance)
    print("Attendance marked!")

def view_attendance():
    if not attendance:
        print("No subjects found!")
        return

    for subject, data in attendance.items():
        total = data["total"]
        present = data["present"]
        percent = (present / total * 100) if total > 0 else 0

        print(f"\n{subject}")
        print(f"Present: {present}")
        print(f"Total: {total}")
        print(f"Percentage: {round(percent, 2)}%")

        if percent < 75:
            print("⚠️ Warning: Low Attendance!")

def main():
    while True:
        print("\n--- Attendance Tracker ---")
        print("1. Add Subject")
        print("2. Mark Attendance")
        print("3. View Attendance")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_subject()
        elif choice == "2":
            mark_attendance()
        elif choice == "3":
            view_attendance()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()

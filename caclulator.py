import tkinter as tk

def calculate_gpa():
    grades = {
        'A': 4.0,
        'B': 3.0,
        'C': 2.0,
        'D': 1.0,
        'F': 0.0
    }

    total_credits = 0
    total_grade_points = 0

    for subject in subjects_entries:
        grade = subject['grade'].get()
        credits = int(subject['credits'].get())

        if grade.upper() in grades:
            grade_point = grades[grade.upper()]
            total_grade_points += grade_point * credits
            total_credits += credits

    if total_credits == 0:
        gpa_result.set("GPA: N/A")
    else:
        gpa = total_grade_points / total_credits
        gpa_result.set("GPA: {:.2f}".format(gpa))

def add_subject():
    subject_frame = tk.Frame(root)
    subject_frame.pack(pady=10)

    tk.Label(subject_frame, text="Grade:").grid(row=0, column=0, padx=5)
    grade_entry = tk.Entry(subject_frame, width=5)
    grade_entry.grid(row=0, column=1)

    tk.Label(subject_frame, text="Credits:").grid(row=0, column=2, padx=5)
    credits_entry = tk.Entry(subject_frame, width=5)
    credits_entry.grid(row=0, column=3)

    subject_entry = {'frame': subject_frame, 'grade': grade_entry, 'credits': credits_entry}
    subjects_entries.append(subject_entry)

def remove_subject():
    if subjects_entries:
        last_subject = subjects_entries.pop()
        last_subject['frame'].destroy()

# Create the main window
root = tk.Tk()
root.title("GPA Calculator")

# Create a list to store subject entries
subjects_entries = []

# Create the GPA result label
gpa_result = tk.StringVar()
gpa_result.set("GPA: N/A")
tk.Label(root, textvariable=gpa_result, font=("Helvetica", 14)).pack(pady=10)

# Create "Add Subject" button
tk.Button(root, text="Add Subject", command=add_subject).pack(pady=5)

# Create "Remove Subject" button
tk.Button(root, text="Remove Subject", command=remove_subject).pack(pady=5)

# Create "Calculate GPA" button
tk.Button(root, text="Calculate GPA", command=calculate_gpa).pack(pady=5)

# Run the Tkinter event loop
root.mainloop()

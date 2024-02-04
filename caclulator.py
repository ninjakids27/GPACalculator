import tkinter as tk

def calculate_unweighted_gpa():
    grades = {
        'A': 4.0,
        'B': 3.0,
        'C': 2.0,
        'D': 1.0,
        'F': 0.0
    }

    total_credits = 0
    total_grade_points = 0

    for subject in unweighted_subjects_entries:
        grade = subject['grade'].get()
        credits = int(subject['credits'].get())

        if grade.upper() in grades:
            grade_point = grades[grade.upper()]
            total_grade_points += grade_point * credits
            total_credits += credits

    if total_credits == 0:
        unweighted_gpa_result.set("Unweighted GPA: N/A")
    else:
        gpa = total_grade_points / total_credits
        unweighted_gpa_result.set("Unweighted GPA: {:.2f}".format(gpa))

def calculate_weighted_gpa():
    grades = {
        'A': 4.0,
        'B': 3.0,
        'C': 2.0,
        'D': 1.0,
        'F': 0.0
    }

    total_weighted_credits = 0
    total_weighted_grade_points = 0

    for subject in weighted_subjects_entries:
        grade = subject['grade'].get()
        credits = int(subject['credits'].get())
        weight = float(subject['weight'].get())

        if grade.upper() in grades:
            grade_point = grades[grade.upper()]
            weighted_grade_point = grade_point * weight
            total_weighted_grade_points += weighted_grade_point * credits
            total_weighted_credits += credits

    if total_weighted_credits == 0:
        weighted_gpa_result.set("Weighted GPA: N/A")
    else:
        weighted_gpa = total_weighted_grade_points / total_weighted_credits
        weighted_gpa_result.set("Weighted GPA: {:.2f}".format(weighted_gpa))

def add_unweighted_subject():
    subject_frame = tk.Frame(unweighted_frame)
    subject_frame.pack(pady=10)

    tk.Label(subject_frame, text="Grade:").grid(row=0, column=0, padx=5)
    grade_entry = tk.Entry(subject_frame, width=5)
    grade_entry.grid(row=0, column=1)

    tk.Label(subject_frame, text="Credits:").grid(row=0, column=2, padx=5)
    credits_entry = tk.Entry(subject_frame, width=5)
    credits_entry.grid(row=0, column=3)

    subject_entry = {'grade': grade_entry, 'credits': credits_entry}
    unweighted_subjects_entries.append(subject_entry)

def add_weighted_subject():
    subject_frame = tk.Frame(weighted_frame)
    subject_frame.pack(pady=10)

    tk.Label(subject_frame, text="Grade:").grid(row=0, column=0, padx=5)
    grade_entry = tk.Entry(subject_frame, width=5)
    grade_entry.grid(row=0, column=1)

    tk.Label(subject_frame, text="Credits:").grid(row=0, column=2, padx=5)
    credits_entry = tk.Entry(subject_frame, width=5)
    credits_entry.grid(row=0, column=3)

    tk.Label(subject_frame, text="Weight:").grid(row=0, column=4, padx=5)
    weight_entry = tk.Entry(subject_frame, width=5)
    weight_entry.grid(row=0, column=5)

    subject_entry = {'grade': grade_entry, 'credits': credits_entry, 'weight': weight_entry}
    weighted_subjects_entries.append(subject_entry)

def remove_unweighted_subject():
    if unweighted_subjects_entries:
        last_subject = unweighted_subjects_entries.pop()
        last_subject.destroy()

def remove_weighted_subject():
    if weighted_subjects_entries:
        last_subject = weighted_subjects_entries.pop()
        last_subject.destroy()

# Create the main window
root = tk.Tk()
root.title("GPA Calculator")

# Create unweighted GPA section
unweighted_frame = tk.Frame(root)
unweighted_frame.pack(pady=10)

tk.Label(unweighted_frame, text="Unweighted GPA Calculator", font=("Helvetica", 14)).pack(pady=5)

# Create a list to store unweighted subject entries
unweighted_subjects_entries = []

# Create the Unweighted GPA result label
unweighted_gpa_result = tk.StringVar()
unweighted_gpa_result.set("Unweighted GPA: N/A")
tk.Label(unweighted_frame, textvariable=unweighted_gpa_result, font=("Helvetica", 12)).pack(pady=5)

# Create "Add Unweighted Subject" button
tk.Button(unweighted_frame, text="Add Subject", command=add_unweighted_subject).pack(pady=5)

# Create "Remove Unweighted Subject" button
tk.Button(unweighted_frame, text="Remove Subject", command=remove_unweighted_subject).pack(pady=5)

# Create "Calculate Unweighted GPA" button
tk.Button(unweighted_frame, text="Calculate GPA", command=calculate_unweighted_gpa).pack(pady=5)

# Create weighted GPA section
weighted_frame = tk.Frame(root)
weighted_frame.pack(pady=10)

tk.Label(weighted_frame, text="Weighted GPA Calculator", font=("Helvetica", 14)).pack(pady=5)

# Create a list to store weighted subject entries
weighted_subjects_entries = []

# Create the Weighted GPA result label
weighted_gpa_result = tk.StringVar()
weighted_gpa_result.set("Weighted GPA: N/A")
tk.Label(weighted_frame, textvariable=weighted_gpa_result, font=("Helvetica", 12)).pack(pady=5)

# Create "Add Weighted Subject" button
tk.Button(weighted_frame, text="Add Subject", command=add_weighted_subject).pack(pady=5)

# Create "Remove Weighted Subject" button
tk.Button(weighted_frame, text="Remove Subject", command=remove_weighted_subject).pack(pady=5)

# Create "Calculate Weighted GPA" button
tk.Button(weighted_frame, text="Calculate GPA", command=calculate_weighted_gpa).pack(pady=5)

# Run the Tkinter event loop
root.mainloop()

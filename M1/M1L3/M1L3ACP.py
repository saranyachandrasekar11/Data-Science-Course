# Program to check Exam Eligibility

# Step 1: Get user data
attendance = float(input("Enter your attendance percentage: "))
score = float(input("Enter your previous exam score (out of 100): "))

# Step 2: Define thresholds
min_attendance = 75.0
min_score = 45.0

# Step 3: Check eligibility
if attendance >= min_attendance and score >= min_score:
    print("\nStatus: ELIGIBLE")
    print("You meet all requirements to sit for the exam.")
else:
    print("\nStatus: NOT ELIGIBLE")
    
    # Optional: Provide specific feedback
    if attendance < min_attendance:
        print(f"- Your attendance ({attendance}%) is below the required {min_attendance}%.")
    if score < min_score:
        print(f"- Your score ({score}) is below the required {min_score} marks.")

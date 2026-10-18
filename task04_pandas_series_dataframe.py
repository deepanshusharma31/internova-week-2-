"""Task 4: Pandas Series & DataFrame"""
import pandas as pd

# Series
marks = pd.Series([85, 92, 78, 66, 90], index=["Amit", "Riya", "Karan", "Neha", "Sara"],
                  name="Maths Marks")
print("Pandas Series:\n", marks)
print("Series mean:", marks.mean())

# DataFrame - student information
data = {
    "Student_ID": [101, 102, 103, 104, 105],
    "Name": ["Amit", "Riya", "Karan", "Neha", "Sara"],
    "Age": [20, 21, 20, 22, 21],
    "Course": ["Economics", "Statistics", "Economics", "Commerce", "Statistics"],
    "Marks": [85, 92, 78, 66, 90],
}
df = pd.DataFrame(data)
print("\nDataFrame:\n", df)
print("\nColumn names:", list(df.columns))
print("Index:", df.index)

# Add new column
df["Result"] = ["Pass" if m >= 70 else "Needs Improvement" for m in df["Marks"]]
df["Percentage"] = df["Marks"] / 100 * 100
print("\nUpdated DataFrame:\n", df)

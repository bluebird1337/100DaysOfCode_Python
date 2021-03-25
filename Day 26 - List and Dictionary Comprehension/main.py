import pandas

student_dict = {
    "student": ["Howard", "Angela", "James"],
    "score": [56, 76, 98],
}
# # looping through dictionary
# for (key, value) in student_dict.items():
#     print(value)

# loop through data frame by row
student_df = pandas.DataFrame(student_dict)
for (index, row) in student_df.iterrows():
    print(row.student)

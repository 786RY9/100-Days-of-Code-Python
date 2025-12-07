
student_dict = {
    'student':['aj','jj','ali','ans','hamza','ry'],
    'score':[90,90,92,90,90,90]
}

# for (key,value) in student_dict.items():
#     print(value)

import pandas

student_df = pandas.DataFrame(student_dict)

# print(student_df)

# for (key,value) in student_df.items():
#     print(value)


# loop through rows of a data frame
for (index,row) in student_df.iterrows():
    if row.score>=60:
        print(row.student, row.score)




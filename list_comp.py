
# Task 1:Use a list comprehension to filter all the scores above 60 and store them in a new list called pass

scores = [45, 78, 88, 56, 90, 62, 33, 99, 70, 50]

passed = [score for score in scores if score > 60]

print (passed)


# Task 2: Use another list comprehension to convert all scores into "Pass" or "Fail" using a threshold of 50.

Pass_failed = ["Pass" if score >= 50 else "Fail"  for score in scores ]

print(Pass_failed)


#Dictionary Comprehension 

#Task 1: Create a dictionary using comprehension that pairs each student with their mark.

students = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']
marks = [82, 48, 79, 65, 91]

students_marks = {students: marks for (students, marks) in zip(students, marks)}

print(students_marks)

#Task 2: Create a second dictionary that stores only students who scored more than 70.


Passed_students = {students: marks for (students, marks) in zip (students, marks) if marks >70}

print(Passed_students)


#Task 3: Create a third dictionary that maps each student to "Pass" or "Fail" (threshold: 50).

threshold_marks = {students : "Pass" if marks > 50 else "Fail" for (students, marks) in zip (students, marks)}

print(threshold_marks)


#Bonus Challenge 

#Given a sentence:

sentence = "Data science is fun and insightful"

#Write a dictionary comprehension that maps each word to its length.


word_lengths = {word: len(word) for word in sentence.split()}

print(word_lengths)

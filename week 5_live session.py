# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 18:40:43 2022

@author: Saubhik
"""
#using a txt file
# with open('test.txt','r') as f:
#     data= f.readlines()
# data=[i.rstrip() for i in data]


#reading the input string line by line to make a list
inp=input()
data=[]
while inp:
    data.append(inp.rstrip())
    inp=input()

# making a grade point dictionary
gp={'A':10, 'AB':9, 'B':8, 'BC':7, 'C':6, 'CD':5, 'D':4}

# getting the starting index of scores info, student info and grade info
course_idx=0
stud_idx=0
grade_idx=0

for idx, i in enumerate(data):
    if i== "Courses":
        course_idx=idx+1
    elif i== "Students":
        stud_idx=idx+1
    elif i== 'Grades':
        grade_idx=idx+1

#making the course dictionary
courses=data[course_idx:stud_idx-1]
courses=[i.split('~')[0] for i in courses]
courses={i:0 for i in courses}

#making the student dictionary for recording scores
students=data[stud_idx:grade_idx-1]
students_scores={}
for stud in students:
    roll=stud.split('~')[0]
    name=stud.split('~')[1]
    students_scores[roll]=[name,dict(courses)]

#recording grades in student score dictionary
grades=data[grade_idx:-1]
for g in grades:
    course=g.split('~')[0]
    roll=g.split('~')[-2]
    grade=g.split('~')[-1]
    students_scores[roll][1][course]=gp[grade]

#adding the GPA
for roll in students_scores:
    score_dict=students_scores[roll][1]
    students_scores[roll].append(round(sum(score_dict.values())/len(score_dict),2))

#printing the output
for roll in students_scores:
    print(roll,students_scores[roll][0],students_scores[roll][-1], sep='~')

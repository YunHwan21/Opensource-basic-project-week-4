def get_total(a, b ,c):
    return a + b + c

def get_average(total):
    return total/3

def get_grade(average):
    if average >= 90:
     return 'A'

    elif average >= 80:
     return 'B'

    elif average >= 70:
     return 'C'

    elif average >= 60:
     return 'D'

    else:
     return 'F'

def get_rank(total):
  rank = sorted(total, reverse = True)
  return [rank.index(x) + 1 for x in total]

def print_Students(Students):
  print("             성적관리 프로그램")
  print("====================================================================")
  print("\n학번       이름       영어  C-언어  파이썬   총점   평균  학점  등수 \n")
  print("====================================================================")
  for i, Student in enumerate(Students):
   print(f"\n{Student['학번']}      {Student['이름']}      {Student['영어']}  {Student['C-언어']}  {Student['파이썬']}    {Student['총점']}   {Student['평균']}    {Student['학점']}     {rank[i]}")
   

Students = []

for i in range(5): 
    Number = input("학번 :")
    Name = input("이름 :")
    English = float(input("영어 :"))
    C_language = float(input("C-언어 : "))
    Python = float(input("파이썬 :"))

    total = get_total(English, C_language, Python)
    average = get_average(total)
    grade =get_grade(average)

    Students.append({'학번': Name, '이름': Name, '영어' : English, 'C-언어': C_language
                     , '파이썬' : Python, '총점': total, '평균': average, '학점': grade})

rank = get_rank([Student['총점'] for Student in Students])

print_Students(Students)

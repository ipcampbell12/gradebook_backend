import sqlite3 


def get_grades():
    connection = sqlite3.connect('boardgames.db')
    cursor = connection.cursor()

    query = '''
    SELECT s.fname || ' ' || s.lname AS student, AVG(a.score), a.name, su.name FROM students s
    JOIN students_assessments sa
    ON s.id = sa.student_id
    JOIN assessments a
    ON sa.assessment_id = a.id 
    JOIN subjects su 
    ON a.subject_id = su.id
    GROUP BY student
    '''

    cursor.execute(query)
    total = cursor.fetchall()
    num = total
    print(num)

    if num: 
        return num[0]
    else:
        return []
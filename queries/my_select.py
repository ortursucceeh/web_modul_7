import sys
import os
sys.path.append(os.getcwd())

from db.models import Class, Student, Teacher, Subject, Grade
from db.connect_db import session

from sqlalchemy import select, func, desc



def query_1():
    q = session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_rate'))\
        .select_from(Student).join(Grade).filter(Grade.student_id == Student.id).group_by(Student.id).order_by(desc('avg_rate')).limit(5).all()
    return q


def query_2():
    q = session.query(Student.fullname, Subject.name, Grade.grade).select_from(Grade).join(Student, Subject).filter(
        Student.id == Grade.student_id and Subject.id == Grade.subject_id).filter(Subject.id == 7).order_by(desc(Grade.grade)).limit(1).all()
    return q

def query_3():
    return session.query(Class.name, func.round(func.avg(Grade.grade), 2)).select_from(Grade).join(Student, Subject, Class).filter(
        Grade.student_id == Student.id and Subject.id == Grade.subject_id and Class.id == Student.class_id).filter(Subject.id == 3).group_by(
            Class.name).order_by(Class.name).all()

def query_4():
    return session.query(func.round(func.avg(Grade.grade), 2)).select_from(Grade).all()

def query_5():
    return session.query(Teacher.fullname, Subject.name).select_from(Subject).join(Teacher).filter(Subject.teacher_id == Teacher.id).order_by(Teacher.fullname).all()

def query_6():
    return session.query(Class.name, Student.fullname).select_from(Student).join(Class).filter(Student.class_id == Class.id).filter(Class.id == 1).order_by(Student.fullname).all()

def query_7():
    return session.query(Class.name, Student.fullname, Subject.name, Grade.grade).select_from(Grade).join(Student, Class, Subject).filter(
        Student.class_id == Class.id and Student.id == Grade.student_id and Subject.id == Grade.subject_id).filter(Class.id == 3).filter(Subject.id == 4).order_by(desc(Grade.grade)).all()

def query_8(): # some problems
    return session.query(Teacher.fullname, Subject.name, func.round(func.avg(Grade.grade), 2)).select_from(Grade).join(Teacher, Subject).filter(Teacher.id == Subject.teacher_id and
     Grade.subject_id == Subject.id).filter(Teacher.id == 5).group_by(Subject.name).all()

def query_9(): # .distinct()
    return session.query(Student.fullname, Subject.name).select_from(Student).join(Grade, Subject).filter(Student.id == Grade.student_id and Subject.id == Grade.subject_id).filter(Student.id == 50).order_by(Subject.name)
    

def query_10():
    return session.query(Student.fullname, Teacher.fullname, Subject.name).select_from(Grade).join(Subject, Student, Teacher).filter(Subject.id == Grade.subject_id and Student.id == Grade.student_id 
    and Teacher.id == Subject.teacher_id).filter(Student.id == 42).filter(Teacher.id == 3).order_by(Subject.name).all()

    
for r in query_10():
    print(r)
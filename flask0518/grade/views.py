from flask import Blueprint, render_template
from utils.functions import db
from grade.models import Grade

# 创建名为grade的蓝图，便于对模块内的url进行操控
grade = Blueprint("grade",__name__)

@grade.route('/')
def get_grade():
    return "我是班级"

@grade.route('/createdb/')
def create_db():
    db.create_all() # 在数据库中创建指定的表单
    return "班级表创建成功！！"

@grade.route('/creategrade/')
def create_grade():
    names = {
        'python':'人生苦短，我用python',
        'h5':'我是๑乛◡乛๑',
        'java':'家娃',
        'go':'gogogogogogo'
    }
    grades_list = []
    for key,value in names.items():
        grade = Grade(key,value)  # 创建班级实例
        grades_list.append(grade)
    db.session.add_all(grades_list) # 向数据库中一次性添加、提交多个实例
    db.session.commit()
    return "班级实例创建成功"

@grade.route('/selectstubygrade/<int:id>')
def select_stu_by_grade(id):  # 通过指定班级查找学生
    grade = Grade.query.get(id) # get中只能为主键值，不加相关字段
    stus = grade.students  # OneToMany  Grade--one Student--Many
    return render_template('grade_student.html',grade=grade,stus=stus)
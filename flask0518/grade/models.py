from datetime import datetime
from utils.functions import db

class Grade(db.Model): # 班级模型
    g_id = db.Column(db.Integer,primary_key=True,autoincrement=True) # 班级id  主键  自增
    g_name = db.Column(db.String(10),unique=True)  # 班级名称  独一无二
    g_desc = db.Column(db.String(100),nullable=True)  # 班级描述  可以为空
    g_create_time = db.Column(db.Date,default=datetime.now)  # 创建时间，默认为当前时间
    # Student:关联的模型名称  backref -- (关联模型实例.stu --> 对应的Grade实例)
    # lazy：懒加载  访问时（即 grade.students）才加载两个模型间的关系
    students = db.relationship('Student',backref='stu',lazy=True)
    __tablename__ = "grade"

    def __init__(self,name,desc):
        self.g_name = name
        self.g_desc = desc

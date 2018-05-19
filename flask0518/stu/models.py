from utils.functions import db

class Student(db.Model): # 学生模型
    s_id = db.Column(db.INTEGER,primary_key=True,autoincrement=True) # id 整型  主键  自增
    s_name = db.Column(db.String(20),unique=True) # 姓名  字符串  不重复
    s_age = db.Column(db.INTEGER,default=10) # 年龄 整型 默认10
    # 外键虽然不能像Django中的那样直接使用，但是不可或缺，否则会出现如下错误
    # NoForeignKeysError: Could not determine join condition between parent/child tables on relationship Grade.students
    # - there are no foreign keys linking these tables. Ensure that referencing columns are associated with a ForeignKey
    # or ForeignKeyConstraint, or specify a 'primaryjoin' expression.
    # 加unique=True 即为OneToOne
    s_g = db.Column(db.Integer, db.ForeignKey("grade.g_id"), nullable=True)
    __tablename__ = "student"

    def __init__(self,name,age):  # 初始化函数
        self.s_name = name
        self.s_age = age

sc = db.Table(  # 定义中间表
    'sc',
    # 外键中的内容一定是“关联表名.主键”,如果不是关联表名，则会出现如下错误
    # NoForeignKeysError: Could not determine join condition between parent/child tables on relationship Course.students
    # - there are no foreign keys linking these tables via secondary table 'sc'.
    # Ensure that referencing columns are associated with a ForeignKey or ForeignKeyConstraint,
    # or specify 'primaryjoin' and 'secondaryjoin' expressions.
    db.Column('s_id',db.Integer,db.ForeignKey("student.s_id"),primary_key=True),
    db.Column('c_id',db.Integer,db.ForeignKey('course.c_id'),primary_key=True)
)

class Course(db.Model):
    c_id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    c_name = db.Column(db.String(10),unique=True)
    students = db.relationship('Student', # 关联模块
                               secondary = sc, # 中间表名称
                               backref='cou' # 反向身份引用，学生实例.cou --> 对应的课程信息
                               )
    # 如果不写表名，则自动命名为模块名的小写(不行的！！)
    __tablename__ = 'course'


    def __init__(self,name):
        self.c_name = name
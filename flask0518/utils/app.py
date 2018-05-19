from flask import Flask
from stu.views import stu
from grade.views import grade
from utils.functions import init_ext
from utils.settings import templates_dir, static_dir, SQLALCHEMY_DATABASE_URI

def create_app():
    # template_folder -- 默认访问stu下的templates文件夹
    # static_folder -- 默认访问stu下的static文件夹
    app = Flask(__name__,
                template_folder=templates_dir,
                static_folder=static_dir)
    app.register_blueprint(blueprint=stu,url_prefix='/stu') # 学生应用与stu蓝图绑定起来，并以/stu前缀与其他应用进行区分
    app.register_blueprint(blueprint=grade, url_prefix='/grade') # 班级应用与grade蓝图绑定起来，并以/grade前缀与其他应用进行区分
    # 数据库相关配置信息的设定
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'secret_key'

    app.debug = True # 显示debugtoolbar工具栏
    init_ext(app) # 放置所有的app初始化内容
    return app

from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension
from flask_restful import Api
from flask_marshmallow import Marshmallow

db = SQLAlchemy() # 实例化数据库
debugtoolbar = DebugToolbarExtension() # 实例化debugtoolbar工具栏
api = Api()  # 使用接口输入输出数据
ma = Marshmallow() # 序列化数据

def get_db_url(DATABASE):
    user = DATABASE.get('USER','root')  # USER为空，默认赋值为root
    password = DATABASE.get('PASSWORD')
    host = DATABASE.get('HOST')
    name = DATABASE.get('NAME')
    port = DATABASE.get('PORT')
    db = DATABASE.get('DB')
    driver = DATABASE.get('DRIVER')
    return '{}+{}://{}:{}@{}:{}/{}'.format(db,driver,
                                              user,password,
                                              host,port,name)

def init_ext(app):
    # app的相关初始化工作
    # 初始化app 将其置于SQLAlchemy框架之下，便于进行orm映射
    # 同时加载数据库配置信息，为后续的使用做准备
    # 若少了此句，则会报如下错误：
    # AssertionError: The sqlalchemy extension was not registered to the current application.
    # Please make sure to call init_app() first.
    # 即具体应用一定要被SQLAlchemy框架初始化，置于其下
    # SQLAlchemy(app=app) # 尽量在初始化的过程中把公共的部分(app)提出来，避免重复操作，如下
    db.init_app(app=app)
    debugtoolbar.init_app(app=app)
    api.init_app(app=app)
    ma.init_app(app=app)
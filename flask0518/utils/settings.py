import os
from utils.functions import get_db_url
# 放置所有配置相关的操作，形同Django的setting.py

# 基础路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 页面模板
templates_dir = os.path.join(BASE_DIR,"templates")
# 静态模板
static_dir = os.path.join(BASE_DIR,"static")

# 连接数据库
DATABASE = {
    # 用户
    'USER':'root',
    # 密码
    'PASSWORD':'5201314',
    # 端口
    'PORT':'3306',
    # 地址 127.0.0.1
    'HOST':'127.0.0.1',
    # 数据库
    'DB':'mysql',
    # 驱动
    # pymysql --> 驱动  -- python3没有mysqldb,所以需要以pymysql为媒介，来操纵mysql
    'DRIVER':'pymysql',
    # 数据库名称
    'NAME': 'flask_20180518'
}

# 连接数据库
SQLALCHEMY_DATABASE_URI = get_db_url(DATABASE)
# 序列化
from utils.functions import ma

class StuMarsh(ma.Schema):

    class Meta:
        fields = ('s_name','s_age')

stumarsh = StuMarsh()
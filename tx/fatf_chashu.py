import numpy as np
import pandas as pd
# import  pymysql

# 打开数据库连接
# db = pymysql.connect("localhost", "root", "root", "test2")
#
# # 使用 cursor() 方法创建一个游标对象 cursor
# cursor = db.cursor()
#
# # 使用 execute()  方法执行 SQL 查询
# cursor.execute("SELECT 报告类型,建议,次级指标,国家,评级,评估原文,评价内容,备注 from test2.R1;")
# # 使用 fetchone() 方法获取单条数据.
# data = cursor.fetchall()
#
# print(data[0])
#
# # 关闭数据库连接
# db.close()
import numpy as np
import pandas as pd
data=pd.read_csv(r'/Users/saimatsu/Desktop/fatf618_fatfr2.csv',encoding='utf8')
for x in np.array(data):
    print(x[0],x[1],x[2])
df1 = pd.read_excel(r'/Users/saimatsu/Downloads/FATFReader_miao.xlsx', sheetname='Authors')

pd.read_excel()


    # product_list_to_insert = list()
# for x in np.array(data):
#     product_list_to_insert.append(FatfCx_xu(bglx=x[0], jy=[1], cjzb=[2], gj=[3], pj=[4], pgyw=[5], pjnr=[6],bzh=[7]))
#     FatfCx_xu.objects.bulk_create(product_list_to_insert)
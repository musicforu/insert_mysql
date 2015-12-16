#!/usr/bin/python
import xlrd
import pymysql

pymysql.install_as_MySQLdb()
import MySQLdb

table_time=input("请输入要传入数据库的3G表的时间(YYYYMMDD如20151124):").strip()
data = xlrd.open_workbook('D:/每日网络质量/M2000日报'+table_time+'.xlsx')
table = data.sheet_by_name(u'1X')
nrows = table.nrows

#row_values=[]
#for i in range(1,nrows):
	#row_values.append(table.row_values(i))

row_values=[]
for i in range(1,nrows):
	left=[]
	row_value=table.row_values(i)
	for col_value in row_value:
		if col_value == 'NIL':
			col_value=0
		left.append(col_value)
	row_values.append(left)
#print(row_values)

conn=MySQLdb.connect(
		host='127.0.0.1',
		port=3306,
		user='root',
		passwd='703298',
		db='test1',
		charset='utf8'
	)

cursor=conn.cursor()
cursor.execute("CREATE TABLE 3G_"+table_time+"(开始时间 VARCHAR(30),1X标识 VARCHAR(30),网元名称 VARCHAR(30),小区号 VARCHAR(60),扇区号 VARCHAR(30),载频号 VARCHAR(30),\
	小区号_num INT(10),分公司 VARCHAR(30),镇区 VARCHAR(30),直观基站名 VARCHAR(30),覆盖区域 VARCHAR(30),1X载频数 INT(10),伪导频 VARCHAR(30),扇区呼建失败 INT(10),\
	扇区掉话 INT(10),RSSI是否异常 VARCHAR(30),软切换比例_FCH_百分比 FLOAT(10,3),软切换因子_百分比 FLOAT(10,3),尝试次数_CS INT(10),建立成功次数_CS INT(10),\
	建立失败次数_CS INT(10),建立成功率_CS_百分比 FLOAT(10,3),掉话次数_CS INT(10),掉话率_CS_百分比 FLOAT(10,3),捕获反向业务信道前导失败次数_CS INT(10),\
	分配呼叫资源失败次数_CS INT(10),寻呼响应次数载频 INT(10),业务连接失败次数_CS INT(10),业务信道信令交互失败次数_CS INT(10),A1接口失败次数_CS INT(10),\
	尝试次数_PS INT(10),建立成功次数_PS INT(10),建立失败次数_PS INT(10),掉话次数操作维护干预_CS INT(10),掉话次数定时器超时_CS INT(10),掉话次数其它_CS INT(10),\
	掉话次数设备故障_CS INT(10),掉话次数无线接口失败_CS INT(10),掉话次数收不到反向帧_CS INT(10),掉话次数无线接口消息失败_CS INT(10),掉话次数系统侧_CS INT(10),\
	掉话次数A2接口_CS INT(10),掉话次数Abis接口_CS INT(10),掉话次数Erasure帧多_CS INT(10),掉话次数_PS INT(10),业务信道分配成功次数 INT(10),业务信道分配请求次数 INT(10),\
	业务信道请求失败次数 INT(10),分集RSSIdBm FLOAT(10,3),主集RSSIdBm FLOAT(10,3),载频反向链路平均FER_CS_百分比 FLOAT(10,3),载频前向链路平均FER_CS_百分比 FLOAT(10,3),拥塞次数 INT(10),\
	业务信道拥塞率_百分比 FLOAT(10,3),业务信道分配失败次数前向功率不足_软切换 INT(10),业务信道分配失败次数WALSH不足 INT(10),业务信道分配Abis前向带宽不足 INT(10),\
	业务信道分配Abis反向带宽不足 INT(10),业务信道分配失败次数其它 INT(10),\
	业务信道分配失败次数反向功率不足 INT(10),业务信道分配失败次数前向功率不足 INT(10),业务信道分配失败次数信道不足 INT(10),业务信道分配失败次数A3A7资源不足_软切换 INT(10),\
	业务信道分配失败次数功率不足_前向SCH INT(10),Walsh最大占用数 INT(10),Walsh平均占用数 INT(10),业务信道承载的话务量强度不含切换CS_FCHErl FLOAT(10,3),\
	业务信道承载的话务量强度不含切换PS_FCHErl FLOAT(10,3),业务信道承载的话务量含切换爱尔兰 FLOAT(10,3),WALSH话务量强度_FCHErl FLOAT(10,3))")

sql_insert='insert into 3G_'+table_time+' values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,\
%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
cursor.executemany(sql_insert,row_values)

conn.commit()
cursor.close()
conn.close()

print('传入数据库成功！')
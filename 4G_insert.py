#!/usr/bin/python
import xlrd
import pymysql

pymysql.install_as_MySQLdb()
import MySQLdb

def change_time(time):
	return time.replace('-','')

table_time=input("请输入要传入数据库的4G表的时间(YYYY-MM-DD如2015-12-13):").strip()
insert_time=change_time(table_time)
data = xlrd.open_workbook('D:/4G相关/4G性能指标日报/4G性能指标日报('+table_time+').xlsx')
table = data.sheet_by_name(u'小区详情')
nrows = table.nrows
#row_values=table.row_values(2)
row_values=[]
for i in range(1,nrows):
	#获取第i行数据数组	
	row_value=table.row_values(i)
	#获取该行长度
	row_length=len(row_value)
	#获取前1-8列字符串
	col_char=row_value[0:9]
	#获取第9列并转换为整数
	col_nine=int(row_value[9])
	#获取第10列，不变仍为字符串
	col_ten=row_value[10]
	#获取剩余列数内容（数组）
	col_left=row_value[11:]
	#存储将剩余数组中的空值转换为0的数组
	col_left_sum=[]
	for col_value in col_left:
		if col_value == '':
			col_value=0
		col_left_sum.append(col_value)
	
	col_ten_end=[float(x) for x in col_left_sum]
	#拼接9,10，及之后的列值
	tmp_1=[]
	tmp_1.append(col_nine)	
	tmp_1.append(col_ten)
	tmp_1.extend(col_ten_end)
	#拼接成最终一行的列表值
	col_char.extend(tmp_1)	
	#放入总数组中
	row_values.append(col_char)



conn=MySQLdb.connect(
		host='127.0.0.1',
		port=3306,
		user='root',
		passwd='703298',
		db='test1',
		charset='utf8'
	)

cursor=conn.cursor()
cursor.execute("CREATE TABLE 4G_"+insert_time+"(日期 VARCHAR(30),地市 VARCHAR(30),分公司 VARCHAR(30),行政区 VARCHAR(30),覆盖类型 VARCHAR(30),网络制式 VARCHAR(30),厂家 VARCHAR(30),eNodeBName VARCHAR(30),基站名称 VARCHAR(60),\
	基站编号 INT(10),小区名称 VARCHAR(60),小区编号 INT(5),下行PRB平均利用率_百分比 FLOAT(13,3),上行PRB平均利用率_百分比 FLOAT(13,3),PDCCH信道占用率_百分比 FLOAT(13,3),PRACH信道占用率_百分比 FLOAT(13,3),\
	最大RRC连接用户数 FLOAT(13,3),平均RRC连接用户数 FLOAT(13,3),平均激活用户数 FLOAT(13,3),PDCP层上行流量_MB FLOAT(13,3),PDCP层下行流量_MB FLOAT(13,3),PDCP层总流量_MB FLOAT(13,3),上行PRB资源利用率_业务信息_百分比 FLOAT(13,3),\
	上行PRB资源利用率_控制信息_百分比 FLOAT(13,3),下行PRB资源利用率_业务信息_百分比 FLOAT(13,3),下行PRB资源利用率_控制信息_百分比 FLOAT(13,3),空口下行用户面丢包数 INT(10),空口上行用户面丢包数 INT(10),平均用户数 FLOAT(13,3),\
	用户面下行平均时延_ms FLOAT(13,3),用户面PDCP层上行平均吞吐率_百分比 FLOAT(13,3),用户面PDCP层下行平均吞吐率_百分比 FLOAT(13,3),物理层上行平均吞吐率_Kbps FLOAT(13,3),物理层下行平均吞吐率_Kbps FLOAT(13,3),\
	UE发起的RRC连接建立请求次数 INT(10),UE发起的RRC连接建立成功次数 INT(10),UE发起的RRC连接建立成功率_百分比 FLOAT(13,3),UE发起的RRC连接失败次数 FLOAT(13,3),网络发起的RRC连接建立请求次数 FLOAT(13,3),\
	网络发起的RRC连接建立成功次数 INT(10),网络发起的RRC连接失败次数 FLOAT(13,3),网络发起的RRC建立成功率_百分比 FLOAT(13,3),RRC连接建立成功率_百分比 FLOAT(13,3),RRC连接重建请求次数 INT(10),\
	RRC连接重建成功次数 INT(10),RRC连接重建成功率_百分比 FLOAT(13,3),RRC连接建立失败次数_UE无应答 INT(10),RRC连接建立失败次数_小区Reject INT(10),RRC连接建立失败次数_其它原因 INT(10),\
	E_RAB建立请求次数 INT(10),E_RAB建立成功次数 INT(10),E_RAB建立成功率_百分比 FLOAT(13,3),无线连接成功率_百分比 FLOAT(13,3),E_RAB建立失败次数_UE无响应 INT(10),E_RAB建立失败次数_核心网问题 INT(10),\
	E_RAB建立失败次数_传输层问题 INT(10),E_RAB建立失败次数_无线层问题 INT(10),E_RAB建立失败次数_无线资源不足 INT(10),E_RAB建立失败次数_安全模式配置失败 INT(10),E_RAB建立失败次数_其它原因 INT(10),\
	E_RAB异常释放次数 INT(10),E_RAB正常释放次数 INT(10),E_RAB掉线率_百分比 INT(10),E_RAB异常释放次数_核心网问题 INT(10),E_RAB异常释放次数_传输层问题 INT(10),E_RAB异常释放次数_网络拥塞 INT(10),\
	E_RAB异常释放次数_切换失败 INT(10),S1信令连接建立尝试次数 INT(10),S1信令连接建立成功次数 INT(10),S1信令连接建立成功率_百分比 FLOAT(13,3),eNodeB内切换请求次数 FLOAT(13,3),eNodeB内切换成功次数 FLOAT(13,3),\
	系统内切换成功率_百分比 FLOAT(13,3),eNodeB内切换成功率_百分比 FLOAT(13,3),eNodeB间切换成功率_百分比 FLOAT(13,3),X2接口切换请求次数 FLOAT(13,3),X2接口切换成功次数 FLOAT(13,3),X2接口切换成功率_百分比 FLOAT(13,3),\
	S1接口切换请求次数 INT(10),S1接口切换成功次数 INT(10),S1接口切换成功率_百分比 FLOAT(13,3),UE上下文异常释放次数 INT(10),UE上下文正常释放次数 INT(10),UE上下文掉线率_百分比 FLOAT(13,3),\
	同频切换请求次数 FLOAT(13,3),同频切换成功次数 FLOAT(13,3),同频切换成功率_百分比 FLOAT(13,3),异频切换请求次数 FLOAT(13,3),异频切换成功次数 FLOAT(13,3),异频切换成功率_百分比 FLOAT(13,3),RSSI平均值_dBm FLOAT(13,3),\
	RSSI最大值_dBm FLOAT(13,3),RSSI最小值_dBm FLOAT(13,3),平均每PRB干扰噪声平均值_dBm FLOAT(13,3),信道干扰噪声_dBm FLOAT(13,3),下行双流比_分子 INT(10),下行双流比_不含单发送天线_百分比 FLOAT(13,3),\
	CQI质差比例 FLOAT(10,7),CQI0_4次数 INT(10),LTE重定向到3G的次数 INT(10),4G重定向3G比例 FLOAT(9,7),MR总数 INT(9),第二强邻区MR重叠覆盖数 FLOAT(13,3),精确覆盖率 FLOAT(13,3),经度 FLOAT(10,6),\
	纬度 FLOAT(10,6),参考信号功率 FLOAT(13,2),小区发射功率 FLOAT(13,2))")

sql_insert='insert into 4G_'+insert_time+' values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\
,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
cursor.executemany(sql_insert,row_values)

conn.commit()
cursor.close()
conn.close()

print('传入数据库成功！')
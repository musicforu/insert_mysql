a='日期 VARCHAR(30),地市 VARCHAR(30),分公司 VARCHAR(30),覆盖类型 VARCHAR(30),网络制式 VARCHAR(30),厂家 VARCHAR(30),eNodeBName VARCHAR(30),基站名称 VARCHAR(30),\
	基站编号 int(10),小区名称 VARCHAR(30),小区编号 FLOAT(18,8),下行PRB平均利用率_百分比 FLOAT(18,8),上行PRB平均利用率_百分比 FLOAT(18,8),PDCCH信道占用率_百分比 FLOAT(18,8),\
	PRACH信道占用率_百分比 FLOAT(18,8),最大RRC连接用户数 FLOAT(18,8),平均RRC连接用户数 FLOAT(18,8),平均激活用户数 FLOAT(18,8),PDCP层上行流量_MB FLOAT(18,8),PDCP层下行流量_MB FLOAT(18,8),\
	PDCP层总流量_MB FLOAT(18,8),上行PRB资源利用率_业务信息_百分比 FLOAT(18,8),上行PRB资源利用率_控制信息_百分比 FLOAT(18,8),下行PRB资源利用率_业务信息_百分比 FLOAT(18,8),\
	下行PRB资源利用率_控制信息_百分比 FLOAT(18,8),空口下行用户面丢包数 FLOAT(18,8),空口上行用户面丢包数 FLOAT(18,8),平均用户数 FLOAT(18,8),用户面下行平均时延_ms FLOAT(18,8),\
	用户面PDCP层上行平均吞吐率_百分比 FLOAT(18,8),用户面PDCP层下行平均吞吐率_百分比 FLOAT(18,8),物理层上行平均吞吐率_Kbps FLOAT(18,8),物理层下行平均吞吐率_Kbps FLOAT(18,8),\
	UE发起的RRC连接建立请求次数 FLOAT(18,8),UE发起的RRC连接建立成功次数 FLOAT(18,8),UE发起的RRC连接建立成功率_百分比 FLOAT(18,8),UE发起的RRC连接失败次数 FLOAT(18,8),\
	网络发起的RRC连接建立请求次数 FLOAT(18,8),网络发起的RRC连接建立成功次数 FLOAT(18,8),网络发起的RRC连接失败次数 FLOAT(18,8),网络发起的RRC建立成功率_百分比 FLOAT(18,8),\
	RRC连接建立成功率_百分比 FLOAT(18,8),RRC连接重建请求次数 FLOAT(18,8),RRC连接重建成功次数 FLOAT(18,8),RRC连接重建成功率_百分比 FLOAT(18,8),RRC连接建立失败次数_UE无应答 FLOAT(18,8),\
	RRC连接建立失败次数_小区Reject FLOAT(18,8),RRC连接建立失败次数_其它原因 FLOAT(18,8),E_RAB建立请求次数 FLOAT(18,8),E_RAB建立成功次数 FLOAT(18,8),E_RAB建立成功率_百分比 FLOAT(18,8),\
	无线连接成功率_百分比 FLOAT(18,8),E_RAB建立失败次数_UE无响应 FLOAT(18,8),E_RAB建立失败次数_核心网问题 FLOAT(18,8),E_RAB建立失败次数_传输层问题 FLOAT(18,8),E_RAB建立失败次数_无线层问题 FLOAT(18,8),\
	E_RAB建立失败次数_无线资源不足 FLOAT(18,8),E_RAB建立失败次数_安全模式配置失败 FLOAT(18,8),E_RAB建立失败次数_其它原因 FLOAT(18,8),E_RAB异常释放次数 FLOAT(18,8),E_RAB正常释放次数 FLOAT(18,8),\
	E_RAB掉线率_百分比 FLOAT(18,8),E_RAB异常释放次数_核心网问题 FLOAT(18,8),E_RAB异常释放次数_传输层问题 FLOAT(18,8),E_RAB异常释放次数_网络拥塞 FLOAT(18,8),E_RAB异常释放次数_切换失败 FLOAT(18,8),\
	S1信令连接建立尝试次数 FLOAT(18,8),S1信令连接建立成功次数 FLOAT(18,8),S1信令连接建立成功率_百分比 FLOAT(18,8),eNodeB内切换请求次数 FLOAT(18,8),eNodeB内切换成功次数 FLOAT(18,8),\
	系统内切换成功率_百分比 FLOAT(18,8),eNodeB内切换成功率_百分比 FLOAT(18,8),eNodeB间切换成功率_百分比 FLOAT(18,8),X2接口切换请求次数 FLOAT(18,8),X2接口切换成功次数 FLOAT(18,8),\
	X2接口切换成功率_百分比 FLOAT(18,8),S1接口切换请求次数 FLOAT(18,8),S1接口切换成功次数 FLOAT(18,8),S1接口切换成功率_百分比 FLOAT(18,8),UE上下文异常释放次数 FLOAT(18,8),\
	UE上下文正常释放次数 FLOAT(18,8),UE上下文掉线率_百分比 FLOAT(18,8),同频切换请求次数 FLOAT(18,8),同频切换成功次数 FLOAT(18,8),同频切换成功率_百分比 FLOAT(18,8),\
	异频切换请求次数 FLOAT(18,8),异频切换成功次数 FLOAT(18,8),异频切换成功率_百分比 FLOAT(18,8),RSSI平均值_dBm FLOAT(18,8),RSSI最大值_dBm FLOAT(18,8),RSSI最小值_dBm FLOAT(18,8),\
	平均每PRB干扰噪声平均值_dBm FLOAT(18,8),信道干扰噪声_dBm FLOAT(18,8),下行双流比_分子 FLOAT(18,8),下行双流比_不含单发送天线_百分比 FLOAT(18,8),CQI质差比例 FLOAT(18,8),\
	CQI0_4次数 FLOAT(18,8),LTE重定向到3G的次数 FLOAT(18,8),4G重定向3G比例 FLOAT(18,8),MR总数 FLOAT(18,8),第二强邻区MR重叠覆盖数 FLOAT(18,8),精确覆盖率 FLOAT(18,8),经度 FLOAT(18,8),\
	纬度 FLOAT(18,8),参考信号功率 FLOAT(18,8),小区发射功率 FLOAT(18,8)'
b=a.split(',')
print(len(b))
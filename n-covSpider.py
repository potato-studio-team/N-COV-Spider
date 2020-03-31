import requests
import json
import types
from bs4 import BeautifulSoup

def getInformationChina():
	url = "https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5"
	try:
		r = requests.get(url)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text
	except:
		print("!中国疫情数据抓取错误!")

def getInformationForeign():
	url = "https://api.inews.qq.com/newsqa/v1/automation/foreign/country/ranklist"
	try:
		r = requests.get(url)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text
	except:
		print("!国际疫情数据抓取错误!")

def dataMake(dataJs,dataLs):
	dataLs[0] = json.loads(dataJs[0])
	dataLs[1] = json.loads(dataJs[1])
	return dataLs

# 获取字典中的objkey对应的值，适用于字典嵌套
# dict:字典
# objkey:目标key
# default:找不到时返回的默认值
def MoreDictGet(dict,objkey,default):
	tmp = dict
	for k,v in tmp.items():
		if k == objkey:
			return v
		elif type(v) == dict:
			rel = MoreDictGet(v,objkey,default)
			return rel

	return default			

# 疫情总览处理
def MainVirous(dataLs):
	ls = []

	# 中国疫情总览处理+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

	data = dataLs[0]
	# 修补腾讯API格式错误
	data = eval(data["data"].replace("true","True").replace("false","False"))
	
	# 搜索日期数据
	ls.append("数据更新时间：" + MoreDictGet(data,"lastUpdateTime","none"))
	
	ls.append("中国疫情总览------------------------------------------------------")
	dic1 = MoreDictGet(data,"chinaTotal","none")
	dic2 = MoreDictGet(data,"chinaAdd","none")

	# 确诊
	ls.append("确诊:" + "       累计:" + str(dic1["confirm"]) + 
		"例(新增:" + str(dic2["confirm"]) + ")" + 
		"     现有:" + str(dic1["nowConfirm"]) + 
		"例(新增:" + str(dic2["nowConfirm"]) + ")")

	# 治愈
	ls.append("治愈:" + "       累计:" + str(dic1["heal"]) + 
		"例(新增:" + str(dic2["heal"]) + ")")

	# 死亡
	ls.append("死亡:" + "       累计:" + str(dic1["dead"]) + 
		"例(新增:" + str(dic2["dead"]) + ")")

	# 疑似
	ls.append("疑似:" + "       现有:" + str(dic1["suspect"]) + 
		"例(新增:" + str(dic2["suspect"]) + ")")

	# 境外输入
	ls.append("境外输入:" + "   累计:" + str(dic1["importedCase"]) + 
		"例(新增:" + str(dic2["importedCase"]) + ")")
	
	# 重症
	ls.append("重症:" + "       现有:" + str(dic1["nowSevere"]) + 
		"例(新增:" + str(dic2["nowSevere"]) + ")")

	# 国际疫情总览处理+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

	data = dataLs[1]
	dic = MoreDictGet(data,"data","none")

	wdConfirmAdd = 0
	wdNowConfirm = 0
	wdConfirm = 0
	wdDead = 0
	wdHeal = 0
	wdNowConfirmCompare = 0
	wdHealCompare = 0
	wdDeadCompare = 0

	for di in dic:
		# 全部数据计算
		wdConfirmAdd = MoreDictGet(di,"confirmAdd","none") + wdConfirmAdd
		wdNowConfirm = MoreDictGet(di,"nowConfirm","none") + wdNowConfirm
		wdConfirm = MoreDictGet(di,"confirm","none") + wdConfirm
		wdDead = MoreDictGet(di,"dead","none") + wdDead
		wdHeal = MoreDictGet(di,"heal","none") + wdHeal
		wdNowConfirmCompare = MoreDictGet(di,"nowConfirmCompare","none") + wdNowConfirmCompare
		wdHealCompare = MoreDictGet(di,"healCompare","none") + wdHealCompare
		wdDeadCompare = MoreDictGet(di,"deadCompare","none") + wdDeadCompare


	ls.append("\n世界疫情总览-------------------------------------------------------")

	# 确诊
	ls.append("确诊:" + "       累计:" + str(wdConfirm) + 
		"例(新增:" + str(wdConfirmAdd) + ")" + 
		"     现有:" + str(wdNowConfirm) + 
		"例(新增:" + str(wdNowConfirmCompare) + ")")

	# 治愈
	ls.append("治愈:" + "       累计:" + str(wdHeal) + 
		"例(新增:" + str(wdHealCompare) + ")")

	# 死亡
	ls.append("死亡:" + "       累计:" + str(wdDead) + 
		"例(新增:" + str(wdDeadCompare) + ")")

	return ls

# 中国疫情处理
def chinsVirous(data):
	ls = []
	# 修补腾讯API格式错误
	data = eval(data["data"].replace("true","True").replace("false","False"))
	
	# 搜索日期数据
	ls.append("数据更新时间：" + MoreDictGet(data,"lastUpdateTime","none"))
	
	ls.append("中国疫情总览------------------------------------------------")
	dic1 = MoreDictGet(data,"chinaTotal","none")
	dic2 = MoreDictGet(data,"chinaAdd","none")

	# 确诊
	ls.append("确诊:" + "       累计:" + str(dic1["confirm"]) + 
		"例(新增:" + str(dic2["confirm"]) + ")" + 
		"     现有:" + str(dic1["nowConfirm"]) + 
		"例(新增:" + str(dic2["nowConfirm"]) + ")")

	# 治愈
	ls.append("治愈:" + "       累计:" + str(dic1["heal"]) + 
		"例(新增:" + str(dic2["heal"]) + ")")

	# 死亡
	ls.append("死亡:" + "       累计:" + str(dic1["dead"]) + 
		"例(新增:" + str(dic2["dead"]) + ")")

	# 疑似
	ls.append("疑似:" + "       现有:" + str(dic1["suspect"]) + 
		"例(新增:" + str(dic2["suspect"]) + ")")

	# 境外输入
	ls.append("境外输入:" + "   累计:" + str(dic1["importedCase"]) + 
		"例(新增:" + str(dic2["importedCase"]) + ")")
	
	# 重症
	ls.append("重症:" + "       现有:" + str(dic1["nowSevere"]) + 
		"例(新增:" + str(dic2["nowSevere"]) + ")")

	ls.append("中国各省疫情------------------------------------------------")

	dic = MoreDictGet(data,"areaTree","none")
	dic = MoreDictGet(dic[0],"children","none")# 解决列表问题

	ls.append("编号 省份  现有确诊  现有疑似  累计确诊  治愈  死亡")
	num = 0

	for di in dic:
		# 获取信息并存入变量

		diIn = MoreDictGet(di,"total","none")
		name = MoreDictGet(di,"name","none")# 省
		nowConfirm = MoreDictGet(diIn,"nowConfirm","none")# 现有确诊
		confirm = MoreDictGet(diIn,"confirm","none")# 累计确诊
		suspect = MoreDictGet(diIn,"suspect","none")# 疑似
		dead = MoreDictGet(diIn,"dead","none")# 死亡
		heal = MoreDictGet(diIn,"heal","none")# 治愈

		num = num + 1

		ls.append(str(num) + ".  " + str(name) + "     " + str(nowConfirm) + "     " + str(suspect) + 
			"     " + str(confirm) + "     " + str(heal) + "     " + str(dead))

	return ls

# 国际疫情处理
def foreignVirous(data):
	dic = MoreDictGet(data,"data","none")

	wdConfirmAdd = 0
	wdNowConfirm = 0
	wdConfirm = 0
	wdDead = 0
	wdHeal = 0
	wdNowConfirmCompare = 0
	wdHealCompare = 0
	wdDeadCompare = 0

	for di in dic:
		# 全部数据计算
		wdConfirmAdd = MoreDictGet(di,"confirmAdd","none") + wdConfirmAdd
		wdNowConfirm = MoreDictGet(di,"nowConfirm","none") + wdNowConfirm
		wdConfirm = MoreDictGet(di,"confirm","none") + wdConfirm
		wdDead = MoreDictGet(di,"dead","none") + wdDead
		wdHeal = MoreDictGet(di,"heal","none") + wdHeal
		wdNowConfirmCompare = MoreDictGet(di,"nowConfirmCompare","none") + wdNowConfirmCompare
		wdHealCompare = MoreDictGet(di,"healCompare","none") + wdHealCompare
		wdDeadCompare = MoreDictGet(di,"deadCompare","none") + wdDeadCompare


def writeFile(place,data):
    data = str(data)
    file = open(place,'w', encoding="utf-8")
    file.write(data)
    file.close()

def main():
	# 疫情分类，分为国内：0，国外：1
	dataJs = ["none"]*2
	dataLs = ["none"]*2

	print("#正在获取数据...\n")
	dataJs[0] = getInformationChina()
	dataJs[1] = getInformationForeign()

	if dataJs[0] == "none" or dataJs[1] == "none":
		print("!抓取错误！\n")

	else:
		print("#获取成功\n") 

		dataLs = dataMake(dataJs,dataLs)

		result = MainVirous(dataLs)

		print("以下是疫情的总览数据")
		for i in result:
			print(i + "\n")

		check = input("请输入你要查看的数据类型：\n\n总览：M\n\n中国疫情：C\n\n国际疫情：F\n>>>")
		if check == "M" or check == "m":
			result = MainVirous(dataLs)

		elif check == "C" or check == "c":
			result = chinsVirous(dataLs[0])

		elif check == "F" or check == "f":
			result = foreignVirous(dataLs[1])


		for i in result:
			print(i + "\n")

		# writeFile("test.txt",result[0])
	input("回车退出")

main()
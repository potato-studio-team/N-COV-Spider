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
	中这

	ls.append("中国疫情分省------------------------------------------------")

	return ls

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

		chinaRuselt = chinsVirous(dataLs[0])

		for i in chinaRuselt:
			print(i + "\n")

		# writeFile("test.txt",result[0])
	input("回车退出")

main()
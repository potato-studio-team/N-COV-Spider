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


# def dict_get(dict, objkey, default):
# 	tmp = dict
# 	for k,v in tmp.items():
# 		if k == objkey:
# 			return v
# 		else:
# 			if type(v) == "Dictionary":
# 				ret = dict_get(v, objkey, default)
# 				if ret is not default:
# 					return ret
# 			else:
# 				noDict = v
# 				while(1):
# 					for k,v in noDict.items():
# 						if k == objkey:
# 							return v
# 						elif
# 						else:
# 							bleak

# 获取字典中的objkey对应的值，适用于字典嵌套
# dict:字典
# objkey:目标key
# default:找不到时返回的默认值
def MoreDictGet(dict,objkey,default):
	tmp = dict
	for k,v in tmp.items():
		if k == objkey:
			return v
		print(v)
		print(type(v))
		if type(v) == dict:
			rel = MoreDictGet(v,objkey,default)
			return rel

	return default			

def chinsVirous(data):
	ls = []
	ls.append(MoreDictGet(data,"lastUpdateTime","none"))
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

		print(chinaRuselt)
		# writeFile("test.txt",result[0])
	input("回车退出")

main()
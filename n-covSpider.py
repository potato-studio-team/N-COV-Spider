import requests
import json
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

def writeFile(place,data):
    data = str(data)
    filehandle = open(place,'w', encoding="utf-8")
    filehandle.write(data)
    filehandle.close()

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
		getType = input("#请输入你需要的数据代码\n>>>")
		result = dataMake(dataJs,dataLs)
		print(result)
		writeFile("test.txt",result[0])
	input("回车退出")

main()
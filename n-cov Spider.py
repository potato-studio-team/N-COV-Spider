import requests
from bs4 import BeautifulSoup

def getInformation():
	url = "https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5"
	try:
        send_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
        "Connection": "keep-alive",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8"
        }#伪装成浏览器

        r = requests.get(url,send_headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "Error"

def dataMake(data, getType):


def main():
	data = getInformation()
	result = dataMake(data, getType)
	if data == "Error":
		print("!抓取错误！\n")

	else:


main()
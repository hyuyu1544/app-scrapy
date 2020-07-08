# app-scrapy
用scrapy爬取app資訊及回應

## setup
```
git clone https://github.com/hyuyu1544/app-scrapy.git
cd app-scrapy/app_scrapy
pipenv install
```
進入pipenv shell: ```pipenv shell```
<br>
## Execution<br>
### google play<br>
指令: ```scrapy crawl googleplay```
<br>
參數: <br>
```-a fids=```(輸入多個由```,```隔開)<br>
```-a date=```(只爬取日期之後的回應，格式：YYYYMMDD)<br>
```-a comment=```(True/False)<br>
舉例一:爬取netflix app 資訊及2020年7月9日之後的回應<br>
```
scrapy crawl googleplay \
-a fids=com.netflix.mediaclient \
-a date=20200709 \
-a comment=True
```
舉例二:爬取twitter及telegram資訊和2020年7月1日之後的回應<br>
```
scrapy crawl googleplay \
-a fids=com.twitter.android,org.telegram.messenger \
-a date=20200701 \
-a comment=True
```

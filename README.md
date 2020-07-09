# app-scrapy
用scrapy爬取app資訊及回應

## setup
```
git clone https://github.com/hyuyu1544/app-scrapy.git
cd app-scrapy
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
舉例三:用scrapy內建參數```-o```生成文件<br>
```
scrapy crawl googleplay \
-a fids=com.twitter.android,org.telegram.messenger \
-a date=20200701 \
-a comment=True \
-o result.csv
```
結果:<br>
```
{'app_link': 'https://play.google.com/store/apps/details?id=com.netflix.mediaclient&hl=zh-TW',
 'app_name': 'Netflix',
 'article_type': 'app',
 'author': 'Netflix, Inc.',
 'content': '想找來自全世界，大家都在聊的節目與電影嗎？所有精彩內容全在 Netflix。 我們擁有獲獎肯定的影集、電影、紀錄片和脫口秀特輯。 '
            'Netflix 會讓您愛不釋手的原因如下： • '
            '我們持續推出新的節目與電影。您可以瀏覽新片或搜尋您最喜歡的影片，並且直接在您的裝置上串流視訊。 • '
            '隨著您觀賞的內容越多，Netflix 越能根據您的喜好，推薦節目與電影給您。 • '
            '每個帳戶可建立多達五名使用者。使用者可讓不同的家庭成員擁有個人化的 Netflix。 • '
            '享有兒童專屬的安全觀影體驗，提供老少咸宜的娛樂內容。 • 可預覽我們的影集與電影的短片，並在新集數與新片上線時收到通知。 • '
            '節省流量。將影片下載到您的行動裝置，隨時隨地，離線觀賞。 欲知完整條款與條件詳情，請前往 '
            'http://www.netflix.com/termsofuse 欲知隱私權聲明詳情，請前往 '
            'http://www.netflix.com/privacy 【最新異動】您會擔心接著要看什麼，我們正努力讓這項體驗變得更好。',
 'created_time': datetime.datetime(2020, 7, 6, 0, 0)}
```
```
{'app_link': 'https://play.google.com/store/apps/details?id=com.netflix.mediaclient&reviewId=gp:AOqpTOHADVgkiWOX9MyR15LD9dCm6mQaMZ8vqSj3E8afn0myKsQAQDdj1fMpkGk9TU8TRiAIzQkC3MOaEaU6O_4',
 'app_name': 'Netflix',
 'article_type': 'response',
 'author': '莊秋明',
 'content': '方便簡單快速',
 'created_time': datetime.datetime(2020, 7, 10, 3, 12)}
```

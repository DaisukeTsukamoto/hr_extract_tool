from libs.soup_util import RequestsUtil as req
from libs.db_util import HrInfo, Database


BASE_URL = 'https://www.nikkei.com'  # ベースURLの定義

class ScraperNikkei():
    def execute(self):
        self.session = Database.setup()

        # 1.記事ページのURLリストを取得する
        #info_urls1 = self.get_urls1(BASE_URL + '/news/jinji/hatsurei/')
        
        #追加step4
        #info_urls2 = self.get_urls2(BASE_URL + '/news/jinji/hatsurei/?page=2')
        #info_urls3 = self.get_urls3(BASE_URL + '/news/jinji/hatsurei/?page=3')
        #info_urls4 = self.get_urls4(BASE_URL + '/news/jinji/hatsurei/?page=4')
        info_urls5 = self.get_urls5(BASE_URL + '/news/jinji/hatsurei/?page=5')

        # 2.記事ページからタイトル、日付、内容をDBに保存する
        #for url1 in info_urls1:
        #    self.get_content1(url1)
        
        #追加step4
        #for url2 in info_urls2:
        #    self.get_content2(url2)
        #for url3 in info_urls3:
        #    self.get_content3(url3)
        #for url4 in info_urls4:
        #    self.get_content4(url4)
        for url5 in info_urls5:
            self.get_content5(url5)

        self.session.close()

#    def get_urls1(self, url1):
#        print(f"URL {url1} をスクレイピング中...")
#        soup = req.fetch(url1)
#        if not soup:
#           return []    
#
#        # 記事ページのURLを取得する処理
#        # soupから抜き出そう
#        info_urls1 = soup.find_all('a', class_='fauxBlockLink_f1dg9afs')
#        info_urls1 = [BASE_URL + info_url1['href'] for info_url1 in info_urls1]
#        return info_urls1
    
    #追加step4
    #def get_urls2(self, url2):
#        print(f"URL {url2} をスクレイピング中...")
#        soup = req.fetch(url2)
#        if not soup:
#            return []
#        info_urls2 = soup.find_all('a', class_='fauxBlockLink_f1dg9afs')
#        info_urls2 = [BASE_URL + info_url2['href'] for info_url2 in info_urls2]
#        return info_urls2
    #def get_urls3(self, url3):
#        print(f"URL {url3} をスクレイピング中...")
#        soup = req.fetch(url3)
#        if not soup:
#            return []
#        info_urls3 = soup.find_all('a', class_='fauxBlockLink_f1dg9afs')
#        info_urls3 = [BASE_URL + info_url3['href'] for info_url3 in info_urls3]
#        return info_urls3
    #def get_urls4(self, url4):
#        print(f"URL {url4} をスクレイピング中...")
#        soup = req.fetch(url4)
#        if not soup:
#            return []
#        info_urls4 = soup.find_all('a', class_='fauxBlockLink_f1dg9afs')
#        info_urls4 = [BASE_URL + info_url4['href'] for info_url4 in info_urls4]
#        return info_urls4
    def get_urls5(self, url5):
        print(f"URL {url5} をスクレイピング中...")
        soup = req.fetch(url5)
        if not soup:
            return []
        info_urls5 = soup.find_all('a', class_='fauxBlockLink_f1dg9afs')
        info_urls5 = [BASE_URL + info_url5['href'] for info_url5 in info_urls5]
        return info_urls5

#    def get_content1(self, url1):
        soup = req.fetch(url1)
        print(f"URL {url1} をスクレイピング中...")
        if not soup:
            return

        # 記事ページからタイトル、日時、内容を取得する処理
        # Step1 標準出力しよう
        # Step2 SQLAlchemyでデータベースのhr_infoテーブルに格納しよう
        title=soup.find('h1', class_='title_t1xgcrem').get_text()
        date=soup.find('time').get_text()
        body=soup.find('p', class_='paragraph_p18mfke4').get_text()

        new_record = HrInfo(
            title=title,
            date=date,
            body=body
        )

        self.session.add(new_record)
        self.session.commit()

    #追加step4
#    def get_content2(self, url2):
        soup = req.fetch(url2)
        print(f"URL {url2} をスクレイピング中...")
        if not soup:
            return

        title=soup.find('h1', class_='title_t1xgcrem').get_text()
        date=soup.find('time').get_text()
        body=soup.find('p', class_='paragraph_p18mfke4').get_text()

        new_record = HrInfo(
            title=title,
            date=date,
            body=body
        )

        self.session.add(new_record)
        self.session.commit()
    
#    def get_content3(self, url3):
        soup = req.fetch(url3)
        print(f"URL {url3} をスクレイピング中...")
        if not soup:
            return

        title=soup.find('h1', class_='title_t1xgcrem').get_text()
        date=soup.find('time').get_text()
        body=soup.find('p', class_='paragraph_p18mfke4').get_text()

        new_record = HrInfo(
            title=title,
            date=date,
            body=body
        )

        self.session.add(new_record)
        self.session.commit()

#    def get_content4(self, url4):
        soup = req.fetch(url4)
        print(f"URL {url4} をスクレイピング中...")
        if not soup:
            return

        title=soup.find('h1', class_='title_t1xgcrem').get_text()
        date=soup.find('time').get_text()
        body=soup.find('p', class_='paragraph_p18mfke4').get_text()

        new_record = HrInfo(
            title=title,
            date=date,
            body=body
        )

        self.session.add(new_record)
        self.session.commit()
    
    def get_content5(self, url5):
        soup = req.fetch(url5)
        print(f"URL {url5} をスクレイピング中...")
        if not soup:
            return

        title=soup.find('h1', class_='title_t1xgcrem').get_text()
        date=soup.find('time').get_text()
        body=soup.find('p', class_='paragraph_p18mfke4').get_text()

        new_record = HrInfo(
            title=title,
            date=date,
            body=body
        )

        self.session.add(new_record)
        self.session.commit()
from libs.soup_util import RequestsUtil as req
from libs.db_util import HrInfo, Database


BASE_URL = 'https://www.nikkei.com'  # ベースURLの定義

class ScraperNikkei():
    def execute(self):
        self.session = Database.setup()

        # 1.記事ページのURLリストを取得する
        info_urls = self.get_urls(BASE_URL + '/news/jinji/hatsurei/')

        # 2.記事ページからタイトル、日付、内容をDBに保存する
        for url in info_urls:
            self.get_content(url)

        self.session.close()

    def get_urls(self, url):
        print(f"URL {url} をスクレイピング中...")
        soup = req.fetch(url)
        if not soup:
            return []

        # 記事ページのURLを取得する処理
        # soupから抜き出そう
        info_urls = soup.find_all('a', class_='fauxBlockLink_f1dg9afs')
        info_urls = [BASE_URL + info_url['href'] for info_url in info_urls]
        return info_urls

    def get_content(self, url):
        soup = req.fetch(url)
        print(f"URL {url} をスクレイピング中...")
        if not soup:
            return

        # 記事ページからタイトル、日時、内容を取得する処理
        # Step1 標準出力しよう
        # Step2 SQLAlchemyでデータベースのhr_infoテーブルに格納しよう
        title=soup.find('h1', class_='title_t1xgcrem').get_text()
        date=soup.find('time').get_text()
        content=soup.find('p', class_='paragraph_p18mfke4').get_text()
        print(f"タイトル: {title}")
        print(f"日付: {date}")
        print(f"内容: {content}")

        self.session.commit()

from libs.soup_util import RequestsUtil as req
from libs.db_util import HrInfo, Database
from datetime import datetime, timedelta

BASE_URL = 'https://www.nikkei.com'  # ベースURLの定義
today = datetime.now()
yesterday = today - timedelta(days=1)
formatted_yesterday = yesterday.strftime("%Y年%m月%d日")

class ScraperNikkei():
    def execute(self):
        self.session = Database.setup()

        # 1.記事ページのURLリストを取得する
        all_urls = []
        for page in range(1, 6):
            page_urls = self.get_urls(f"{BASE_URL}/news/jinji/hatsurei/?page={page}")
            all_urls.extend(page_urls)

        # 2.記事ページからタイトル、日付、内容をDBに保存する
        for url in all_urls:
            self.get_content(url)

        self.session.close()

    def get_urls(self, url):
        print(f"URL {url} をスクレイピング中...")
        soup = req.fetch(url)
        if not soup:
            return []   

        # 記事ページのURLを取得する処理
        info_urls = soup.find_all('a', class_='fauxBlockLink_f1dg9afs')
        info_urls = [BASE_URL + info_url['href'] for info_url in info_urls]
        return info_urls

    def get_content(self, url):
        soup = req.fetch(url)
        print(f"URL {url} をスクレイピング中...")
        if not soup:
            return

        # 記事ページからタイトル、日時、内容を取得する処理
        title = soup.find('h1', class_='title_t1xgcrem').get_text()
        date = soup.find('time').get_text()
        body = soup.find('p', class_='paragraph_p18mfke4').get_text()

        article_date = datetime.strptime(date.split()[0], "%Y年%m月%d日")

        if article_date.date() == yesterday.date():
            new_record = HrInfo(
                title=title,
                date=date,
                body=body
            )
            self.session.add(new_record)
            self.session.commit()
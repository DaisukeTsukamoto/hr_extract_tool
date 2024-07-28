from libs.soup_util import RequestsUtil as req
from libs.db_util import HrInfo, Database

BASE_URL = 'https://www.nikkei.com'  # ベースURLの定義
MAX_PAGE = 5

class ScraperNikkei():

    def execute(self):
        self.session = Database.setup()

        for page in range(MAX_PAGE):
            # 1.記事ページのURLリストを取得する
            for url in self.get_urls(f'{BASE_URL}/news/jinji/hatsurei/?page={page+1}'):
                # 2.記事ページからタイトル、日付、内容をDBに保存する
                self.get_content(url)

        self.session.close()

    def get_urls(self, url):
        print(f"URL {url} をスクレイピング中...")
        soup = req.fetch(url)
        if not soup:
            return []

        # 記事ページのURLを取得する処理
        # soupから抜き出そう
        elements = soup.find_all('a', class_="fauxBlockLink_f1dg9afs")

        # hrefの部分をリスト変数に格納
        return [BASE_URL + element.get('href') for element in elements]

    def get_content(self, url):
        soup = req.fetch(url)
        print(f"URL {url} をスクレイピング中...")
        if not soup:
            return

        # 記事ページからタイトル、日時、内容を取得する処理
        # Step1 標準出力しよう
        title = self.extract_text(soup, 'h1', class_="title_t1xgcrem")
        date = self.extract_text(soup, 'div', class_="timeStampOverride_tclhxc0", child_tag='time')
        body = self.extract_text(soup, 'p', class_="paragraph_p18mfke4")


        # 日付が昨日の日付であるかを確認
        if date and self.is_yesterday(date):
            hr_info = HrInfo(title=title, date=date, body=body)
            self.session.add(hr_info)
            self.session.commit()
        else:
            print(f"スキップ: URL {url} の記事は昨日の日付ではありません。")

    def extract_text(self, soup, tag, class_, child_tag=None):
        element = soup.find(tag, class_=class_)
        if element:
            if child_tag:
                element = element.find(child_tag)
            return element.text.strip() if element else None
        return None

    def is_yesterday(self, date_str):
        from datetime import datetime, timedelta
        # 現在の日付を取得し、昨日の日付を計算
        today = datetime.now()
        yesterday = today - timedelta(days=1)

        # 日付文字列をパースして datetime オブジェクトに変換して比較
        try:
            date = datetime.strptime(date_str, '%Y年%m月%d日 %H:%M')
            return date.date() == yesterday.date()
        except ValueError:
            return False

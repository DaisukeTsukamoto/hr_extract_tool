from libs.soup_util import RequestsUtil as req
from libs.db_util import HrInfo, Database


BASE_URL = 'https://www.nikkei.com'  # ベースURLの定義
MAX_PAGE = 5  # 読み込むページ数を決められます

class ScraperNikkei():
    def execute(self):
        self.session = Database.setup()

        # 1.記事ページのURLリストを取得する
        # 2.記事ページからタイトル、日付、内容をDBに保存する
        for page in range(MAX_PAGE):
            for url in self.get_urls(f'{BASE_URL}/news/jinji/hatsurei/?page={page+1}'):
                self.get_content(url)
        self.session.close()

    def get_urls(self, url):
        print(f"URL {url} 内の記事一覧をスクレイピング中...")
        soup = req.fetch(url)
        if not soup:
            return []

        # 記事ページのURLを取得する処理
        # soupから抜き出そう
        info_urls = soup.find_all('a', class_="fauxBlockLink_f1dg9afs")
        return [BASE_URL + info_url.get('href') for info_url in info_urls]

    def get_content(self, url):
        soup = req.fetch(url)
        print(f"URL {url} をスクレイピング中...")
        if not soup:
            return

        # 記事ページからタイトル、日時、内容を取得する処理
        title = self.extract_text(soup, 'h1', class_="title_t1xgcrem")
        date = self.extract_text(soup, 'div', class_="timeStampOverride_tclhxc0", child_tag='time')
        body = self.extract_text(soup, 'p', class_="paragraph_p18mfke4")

        if date and self.is_yesterday(date):
            hr_info = HrInfo(title=title, date=date, body=body)
            self.session.add(hr_info)
            self.session.commit()
        else:
            print(f"スキップ: URL {url} の記事は昨日の日付ではありません。")

    def extract_text(self, soup, tag, class_, child_tag=None):
        info_url = soup.find(tag, class_=class_)
        if info_url:
            if child_tag:
                info_url = info_url.find(child_tag)
            return info_url.text.strip() if info_url else None
        return None

    def is_yesterday(self, date_str):
        from datetime import datetime, timedelta
        # 現在の日付を取得し、指定した日付を計算
        today = datetime.now()
        yesterday = today - timedelta(days=1)

        # 日付文字列をパースして datetime オブジェクトに変換して比較
        try:
            date = datetime.strptime(date_str, '%Y年%m月%d日 %H:%M')
            return date.date() == yesterday.date()
        except ValueError:
            return False
        
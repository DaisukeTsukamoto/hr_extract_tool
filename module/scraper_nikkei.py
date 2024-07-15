from libs.soup_util import RequestsUtil as req
from libs.db_util import HrInfo, Database

BASE_URL = ''  # ベースURLの定義

class ScraperNikkei():
    def execute(self):
        self.session = Database.setup()

        # 1.記事ページのURLリストを取得する
        info_urls = self.get_urls()

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
        info_urls = []

        return info_urls

    def get_content(self, url):
        soup = req.fetch(url)
        print(f"URL {url} をスクレイピング中...")
        if not soup:
            return

        # 記事ページからタイトル、日時、内容を取得する処理
        # Step1 標準出力しよう
        # Step2 SQLAlchemyでデータベースのhr_infoテーブルに格納しよう

        self.session.commit()

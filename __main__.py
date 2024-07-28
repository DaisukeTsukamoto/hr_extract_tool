from module.scraper_nikkei import ScraperNikkei
from service.writer import Writer
from libs.db_util import Database

if __name__ == "__main__":
    ScraperNikkei().execute()
    Writer().execute()
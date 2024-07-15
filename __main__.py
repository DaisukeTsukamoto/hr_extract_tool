from module.scraper_nikkei import ScraperNikkei
from service.writer import Writer

if __name__ == "__main__":
    ScraperNikkei().execute()
    # Writer().execute()
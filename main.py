import os
import sys

from scrapy.cmdline import execute


def main():
    # sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    # execute(["scrapy", "crawl", "EnglishSpider"])
    # execute(["scrapy", "crawl", "ChineseSpider"])
    # execute(["scrapy", "crawl", "MathSpider"])
    # execute(["scrapy", "crawl", "PhysicsSpider"])
    # execute(["scrapy", "crawl", "ChemistrySpider"])
    # execute(["scrapy", "crawl", "BiologySpider"])
    # execute(["scrapy", "crawl", "GeographySpider"])
    # execute(["scrapy", "crawl", "HistorySpider"])
    execute(["scrapy", "crawl", "PoliticsSpider"])
    pass


if __name__ == '__main__':
    main()
    pass

from multiprocessing.dummy import Pool as ThreadPool
from calendar import monthrange
from urllib import request
import re


class ArchiveGetter:
    def __init__(self, years):
        self.months = ArchiveGetter.get_months()
        self.years = years
        self.base_url = 'http://volcano.febras.net/archive/'

    @staticmethod
    def get_months():
        return [i for i in range(1, 13)]

    @staticmethod
    def get_days(month, year):
        return [i for i in range(1, monthrange(year, month)[1] + 1)]

    @staticmethod
    def form_calendar_number_format(num):
        if num < 10:
            return '0' + str(num)
        else:
            return str(num)

    def form_urls(self):
        result = []
        for year in self.years:
            for month in self.months:
                for day in ArchiveGetter.get_days(month, year):
                    result.append(self.base_url + str(year) + '/' +
                                  ArchiveGetter.form_calendar_number_format(month) + '/' +
                                  ArchiveGetter.form_calendar_number_format(day) + '/' + 'SHV1'
                                  )
        return result



    def get_url_from_page(url):
        try:
            f = request.urlopen(url)
            return [url + '/' + s for s in re.findall(r'href=[\'"]?([^\'" >]+)', str(f.read()))[1:]]
        except:
            print(url, '404')
            return ""

    def load_pages(self):
        urls = self.form_urls()
        pool = ThreadPool(13)
        results = pool.map(ArchiveGetter.get_url_from_page, urls)
        pool.close()
        pool.join()
        with open('files/urls.txt', 'w') as file:
            for res in results:
                for el in res:
                    if el != "":
                        file.write(el + '\n')
            file.close()






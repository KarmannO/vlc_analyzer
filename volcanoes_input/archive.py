from calendar import monthrange

class AcrhiveGetter:
    def __init__(self):
        self.root_path = 'http://volcano.febras.net/archive/'
        self.cam_name = 'SHV1'
        self.years = ['2015', '2016']


    @staticmethod
    def form_months(self):
        return [i for i in range(1, 13)]


    @staticmethod
    def form_days(self, year, month):
        return [i for i in range(1, monthrange(year, month)[1] + 1)]


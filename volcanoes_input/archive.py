from calendar import monthrange


class ArchiveGetter:
    def __init__(self):
        self.root_path = 'http://volcano.febras.net/archive/'
        self.cam_name = 'SHV1'
        self.paths = []
        self.years = [2015, 2016]
        for year in self.years:
            path = self.root_path + str(year)
            months = ArchiveGetter.form_months()
            for month in months:
                path_local_month = path + '/' + ArchiveGetter.stringify_date_element(month)
                days = ArchiveGetter.form_days(year, month)
                for day in days:
                    path_local_days = path_local_month + '/' + ArchiveGetter.stringify_date_element(day)
                    self.paths.append(path_local_days + '/' + self.cam_name)

    def get_paths(self):
        return self.paths

    @staticmethod
    def form_months():
        return [i for i in range(1, 13)]

    @staticmethod
    def form_days(year, month):
        return [i for i in range(1, monthrange(year, month)[1] + 1)]

    @staticmethod
    def stringify_date_element(el):
        if el < 10:
            return '0' + str(el)
        else:
            return str(el)


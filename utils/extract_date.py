import datetime
import dateparser


class DateExtractor(object):

    @staticmethod
    def get_date(text):
        if text.lower() == 'next day':
            text = 'tomorrow'
        return dateparser.parse(text) if dateparser.parse(text) else ""


if __name__ == '__main__':
    date1 = DateExtractor.get_date('next day')
    print(date1)

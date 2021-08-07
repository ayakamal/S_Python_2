import datetime
import dateutil.parser
# str=dateutil.parser.parse("15/12/2016")
# str = datetime.datetime.strptime('15/12/2016', '%d/%m/%Y').strftime('%Y%m%d')
# str = parse("11-15-2012")
# print(str)
# print(parse(str).strftime('%Y%m%d'))
from dateutil.parser import parse
def change_date_format(*args):
    list_dates = []
    for s in args:
        str = parse(s).strftime('%Y%m%d')
        list_dates.append(str)

    print("The Date List in YYYYMMDD: ")
    print(list_dates)

change_date_format("2010/03/30","15/12/2016", "11-20-2018", "20130720")

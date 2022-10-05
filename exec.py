import datetime


def week_number_of_month(date_value):
    return (date_value.isocalendar()[1] - date_value.replace(day=1).isocalendar()[1] + 1)


if __name__ == '__main__':
    today = datetime.datetime.now()
    print(today)
    # print(round(datetime.datetime.now().timestamp()))
    print(today.strftime("%B")) # month name
    # print(datetime.date.isocalendar())
    print(week_number_of_month(today))


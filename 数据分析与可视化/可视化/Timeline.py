import datetime

import pyecharts.options as opts
from pyecharts.charts import *
import time
import pandas as pd

begin = datetime.date(2019, 1, 1)
end = datetime.date(2022, 3, 4)

# data = [日期，次数]
dic = {}

cur = datetime.date.today()

read_file = pd.read_csv('../time_dist/result.csv')
times = read_file['通知时间']  # 时间戳
i = 0
for time in times:
    if '昨天' in time:
        times[i] = cur - datetime.timedelta(days=1)
        i += 1
    elif len(time) == 5:
        times[i] = cur
        i += 1
    else:
        break
# print(times)
times.tolist()
print(times)


def get_number_in_list(date_list, number) -> int:
    appear_time = 0
    for date in date_list:
        if number == date:
            appear_time += 1
    return appear_time


data = [(str(begin + datetime.timedelta(days=i)), get_number_in_list(times, str(begin + datetime.timedelta(days=i))))
        for i in range((end - begin).days + 1)]

print(data)


def create_cal(year, title=''):
    return (
        Calendar()
            .add("", data, calendar_opts=opts.CalendarOpts(range_=year))
            .set_global_opts(
                title_opts=opts.TitleOpts(title=title),
                visualmap_opts=opts.VisualMapOpts(
                    max_=100,
                    is_piecewise=True,
                    pieces=[
                        {"max": 10, "label": "10以下", "color": "#daf7a6"},
                        {"min": 10, "max": 20, "label": "10-20", "color": "#ffc300"},
                        {"min": 20, "max": 30, "label": "20-30", "color": "#ff5733"},
                        {"min": 30, "max": 40, "label": "30-40", "color": "#c70039"},
                        {"min": 40, "label": "40以上", "color": "#900c3f"}, ]
                ),
                legend_opts=opts.LegendOpts(is_show=False),
            )
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))

    )


def make_page():
    page = Page(page_title="2019-2022公告发布时间分布")
    page.add(create_cal('2019', '2019-2022公告发布时间分布'), create_cal('2020'), create_cal('2021'), create_cal('2022'))

    # page.render("page6.html")
    return page


make_page()

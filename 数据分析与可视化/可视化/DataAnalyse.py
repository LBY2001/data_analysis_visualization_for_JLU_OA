import datetime
import pandas as pd
import numpy as np
import pyecharts.options as opts
from pyecharts.charts import *
import time

cur = datetime.date.today()

read_file = pd.read_csv('../time_dist/result.csv')
times = read_file['通知时间']
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
print(times)


# calendar = Calendar(init_opts=opts.InitOpts(width='1200px', height='600px'))\
#     .add("", yaxis_data=times, )\
#     .render("cal.html")


calendar = (
    Calendar()
    .add("", times, calendar_opts=opts.CalendarOpts(range_="2022", pos_left='20%'))
    .set_global_opts(visualmap_opts=opts.VisualMapOpts(
        max_=12000,
        is_piecewise=True,
        pieces=[
            {"max": 10, "label": "10以下", "color": "#daf7a6"},
            {"min": 10, "max": 100, "label": "100以下", "color": "#ffc300"},
            {"min": 100, "max": 500, "label": "500以下", "color": "#ff5733"},
            {"min": 500, "max": 1000, "label": "1000以下", "color": "#c70039"},
            {"min": 1000, "label": "1000以上", "color": "#900c3f"},
        ]
    ))

)#.render("cal.html")

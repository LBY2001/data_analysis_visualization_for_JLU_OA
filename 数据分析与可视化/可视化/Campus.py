
import pyecharts.options as opts
from pyecharts.charts import *
import pandas as pd

read_csv = pd.read_csv('../time_dist/校区.csv')
x_data = []
y_data = []
for i in range(len(read_csv)):
    x_data.append((read_csv['Campus'][i]))
    y_data.append(int(read_csv['Number'][i]))
s = sum(int(i) for i in y_data)

x_with_per = []
for x in range(len(x_data)):
    x_data[x] = x_data[x] + str(y_data[x]*100//s) + '%'

bar = Bar().add_xaxis(xaxis_data=x_data).add_yaxis("", y_axis=y_data)#.render("校区.html")


def make_pie() -> Pie:
    pie = Pie()\
        .add("", [list(z) for z in zip(x_data, y_data)], center=["50%", "50%"], radius=["30%", "50%"])\
        .set_global_opts(title_opts=opts.TitleOpts(title="校区分布"),
                         legend_opts=opts.LegendOpts(pos_bottom='20%', pos_left='5%', orient='vertical', item_gap=20))\
        # .render("校区1.html")
    return pie


make_pie()

print("OK")


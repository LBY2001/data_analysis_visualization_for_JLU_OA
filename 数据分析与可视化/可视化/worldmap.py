import pyecharts.options as opts
from pyecharts.charts import *
import pandas as pd
 # import translators as ts


def world_map() -> Map:
    read_csv = pd.read_csv('../time_dist/国家(2).csv')

    Data = []

    for i in range(0, len(read_csv["number"])):
        Data.append((read_csv['en_name'][i], int(read_csv['number'][i])))
    print(Data)
    geo = Map() \
        .add("", data_pair=Data, maptype="world", is_map_symbol_show=False) \
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False)) \
        .set_global_opts(title_opts=opts.TitleOpts(title='公告中提及的国家次数'),
                         visualmap_opts=opts.VisualMapOpts(
                             max_=2000, min_=1, is_piecewise=True,
                             pieces=[{"max": 9, "min": 1, "label": "1-9", "color": "#f9c929"},
                    {"max": 99, "min": 10, "label": "10-99", "color": "#e6a032"},
                    {"max": 499, "min": 100, "label": "100-499", "color": "#c14e4a"},
                    {"max": 999, "min": 500, "label": "500-999", "color": "#a20b5d"},
                    {"max": 2000, "min": 1000, "label": "1000-2000", "color": "#9f025e"}, ]),
                         )\

    # geo.render("wm.html")
    # grid = Grid().add(geo, grid_opts=opts.GridOpts(pos_left="5%", pos_right="5%", pos_top="5%", pos_bottom="5%"))
    # grid.render("grid.html")
    print("over")
    return geo


world_map()

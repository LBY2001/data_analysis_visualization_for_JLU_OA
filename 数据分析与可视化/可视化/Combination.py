import pyecharts.options as opts
from pyecharts.charts import *
import worldmap
import Campus
import Timeline

geo = worldmap.world_map()
page = Timeline.make_page()
pie = Campus.make_pie()
t2019 = Timeline.create_cal(2019, '2019-2022年公告发布频数')
t2020 = Timeline.create_cal(2020, '')
t2021 = Timeline.create_cal(2021, '')
t2022 = Timeline.create_cal(2022, '')

pie.render('../成果图/各校区饼图.html')
geo.render('../成果图/通知相关世界地图.html')
page.render('../成果图/发布时间热力图.html')

Page = Page(layout = Page.DraggablePageLayout)
Page.add(pie, geo, t2019, t2020, t2021, t2022)
# Page.render('../time_dist/temp.html')

Page.save_resize_html('../time_dist/temp.html', cfg_file="../time_dist/chart_config.json", dest="../成果图/可视化大屏.html")

print('done')

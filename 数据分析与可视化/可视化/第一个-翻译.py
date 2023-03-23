import pandas as pd
import numpy as np
import translators as ts

read_csv = pd.read_csv('../time_dist/国家(1).csv', encoding='utf-8')

country_list = read_csv['country']
number = read_csv['number']
en_names = []
'''
name_replace = {
    "America": 'United States',
    "Britain": 'United Kingdom',
    "South Korea": 'Korea',
    "The French": 'France',
    "\"In the Netherlands\",": 'Netherlands',
    "North Korea": 'Dem. Rep. Korea',
    "The Swedish": 'Sweden',
    "The Danish": 'Denmark',
    "The Swiss": 'Switzerland',
    "The Norwegian": 'Norway',
    "The Irish": 'Ireland',
    "The Czech Republic": 'Czech Rep.',
    "The Greek": 'Greece',
    "\"In Hungry\",": 'Hungary',
    "\"In Cambodia\",": 'Cambodia',
    "\"In Zambia\",": 'Zambia',
    "The Philippines": 'Philippines',
    "yemen": 'Yemen',

}
'''
nameMap = { "阿富汗":"Afghanistan", "安哥拉":"Angola", "阿尔巴尼亚":"Albania", "阿尔及利亚":"Algeria", "阿根廷":"Argentina", "亚美尼亚":"Armenia", "澳大利亚" :"Australia", "奥地利":"Austria", "阿塞拜疆":"Azerbaijan", "巴哈马":" Bahamas ", "孟加拉国":"Bangladesh", "比利时":" Belgium ", "贝宁" :"Benin", "布基纳法索":"Burkina Faso", "布隆迪":" Burundi", "保加利亚":"Bulgaria", "波斯尼亚和黑塞哥维那":"Bosnia and Herz", "白俄罗斯" :"Belarus", "伯利兹" :"Belize", "百慕大群岛":"Bermuda", "玻利维亚":"Bolivia", "巴西":"Brazil", "文莱":"Brunei ", "不丹":"Bhutan", "博茨瓦纳":"Botswana", "柬埔寨":"Cambodia", "喀麦隆":"Cameroon", "加拿大":"Canada", "中非共和国":"Central African Rep.", "乍得" :"Chad", "智利" :"Chile", "中国" :"China", "哥伦比亚":"Colombia", "刚果（金）":"Congo", "哥斯达黎加":"Costa Rica", "科特迪瓦":"Côte d'Ivoire", "克罗地亚" :"Croatia ", "古巴" :"Cuba", "塞浦路斯" :"Cyprus", "捷克共和国":"CzechRep", "韩国" :"Dem.Rep.Korea", "刚果（布）":"Dem. Rep. Congo", "丹麦" :"Denmark", "吉布提":"Djibouti", "多米尼加":"Dominican Rep.", "厄瓜多尔":"Ecuador", "埃及" :"Egypt", "萨尔瓦多" :"ElSalvador", "赤道几内亚":"Eq.Guinea", "厄立特里亚":"Eritrea", "爱沙尼亚":"Estonia", "埃塞俄比亚":"Ethiopia", "福克兰群岛":"FalklandIs", "斐济" :"Fiji", "芬兰" :"Finland", "法国" :"France", "法属圭亚那":"FrenchGuiana", "法属南部领地":"Fr.S.AntarcticLands", "加蓬" :"Gabon", "冈比亚":"Gambia", "德国" :"Germany", "佐治亚州":"Georgia ", "加纳":"Ghana", "希腊":"Greece", "格陵兰":"Greenland", "危地马拉":"Guatemala", "几内亚":"Guinea", "几内亚比绍":"Guinea-Bissau", "圭亚那":"Guyana", "海地":"Haiti", "赫德岛和麦克唐纳群岛":"HeardI.andMcDonaldIs", "洪都拉斯":"Honduras", "匈牙利":"Hungary", "冰岛":"Iceland", "印度":"India", "印度尼西亚":"Indonesia", "伊朗":"Iran", "伊拉克":"Iraq", "爱尔兰":"Ireland", "以色列":"Israel", "意大利":"Italy", "象牙海岸":"IvoryCoast", "牙买加":"Jamaica", "日本" :"Japan", "乔丹":"Jordan", "克什米尔":"Kashmir", "哈萨克斯坦":"Kazakhstan", "肯尼亚":"Kenya", "科索沃":"Kosovo", "科威特":"Kuwait", "吉尔吉斯斯坦":"Kyrgyzstan", "老挝" :"Laos", "老挝":"Lao PDR", "拉脱维亚":"Latvia", "黎巴嫩":"Lebanon", "莱索托":"Lesotho", "利比里亚":"Liberia", "利比亚":"Libya", "立陶宛":"Lithuania", "卢森堡":"Luxembourg", "马达加斯加":"Madagascar", "马其顿":"Macedonia", "马拉维":"Malawi", "马来西亚":"Malaysia", "马里":"Mali", "毛里塔尼亚":"Mauritania", "墨西哥":"Mexico", "摩尔多瓦":"Moldova", "蒙古" :"Mongolia", "黑山" :"Montenegro", "摩洛哥":"Morocco", "莫桑比克":"Mozambique", "缅甸":"Myanmar", "纳米比亚":"Namibia", "荷兰" :"Netherlands", "新喀里多尼亚":"New Caledonia", "新西兰":"New Zealand", "尼泊尔":"Nepal", "尼加拉瓜":"Nicaragua", "尼日尔":"Niger", "尼日利亚":"Nigeria", "朝鲜":"Korea", "北塞浦路斯":"NorthernCyprus", "挪威":"Norway", "阿曼":"Oman", "巴基斯坦":"Pakistan", "巴拿马":"Panama", "巴布亚新几内亚":"Papua New Guinea", "巴拉圭":"Paraguay", "秘鲁":"Peru", "刚果":"Republi cofthe Congo", "菲律宾":"Philippines", "波兰":"Poland", "葡萄牙":"Portugal", "波多黎各":"Puerto Rico", "卡塔尔":"Qatar", "塞尔维亚共和国":"RepublicofSerbia", "罗马尼亚":"Romania", "俄罗斯":"Russia", "卢旺达":"Rwanda", "萨摩亚":"Samoa", "沙特阿拉伯":"Saudi Arabia", "塞内加尔":"Senegal", "塞尔维亚" :"Serbia", "塞拉利昂" :"Sierra Leone", "斯洛伐克":"Slovakia", "斯洛文尼亚":"Slovenia", "所罗门群岛":"SolomonIs", "索马里兰":"Somaliland", "索马里":"Somalia", "南非":"South Africa", "南乔治亚和南桑德威奇群岛":"S.Geo.andS.Sandw.Is", "南苏丹":"S.Sudan", "西班牙":"Spain", "斯里兰卡":"Sri Lanka", "苏丹" :"Sudan", "苏里南":"Suriname", "斯威士兰":"Swaziland", "瑞典" :"Sweden", "瑞士":"Switzerland", "叙利亚":"Syria", "塔吉克斯坦":"Tajikistan", "坦桑尼亚":"Tanzania", "泰国" :"Thailand", "东帝汶":"Timor-Leste", "多哥" :"Togo", "特立尼达和多巴哥":"TrinidadandTobago", "突尼斯":"Tunisia", "土耳其":"Turkey", "土库曼斯坦":"Turkmenistan", "乌干达":"Uganda", "乌克兰":"Ukraine",
            "英国": "United Kingdom", "坦桑尼亚联合共和国": "UnitedRepublicofTanzania", "美国" : "United States", "美利坚合众国": "UnitedStatesofAmerica", "乌拉圭": "Uruguay", "乌兹别克斯坦": "Uzbekistan", "瓦努阿图": "Vanuatu", "委内瑞拉": "Venezuela", "越南": "Vietnam", "西岸" : "WestBank", "西撒哈拉": "W.Sahara", "也门共和国": "Yemen", "赞比亚共和国": "Zambia", "津巴布韦": "Zimbabwe",'新加坡':'Singapore Rep.','蒙古国':'Mongolia','捷克':'Czech Rep.','赞比亚':'Zambia','也门':'Yemen','约旦':'Jordan'}
print(1)
for i in range(0, len(country_list)):
    '''
    en_name = ts.google(read_csv['country'][i], sleep_seconds=5, timeout=None, proxies=None)
    if en_name in name_replace:
        en_name = name_replace[en_name]
    '''
    en_name=nameMap[country_list[i]]
    en_names.append(en_name)
    print(en_name)

print(en_names)

read_csv['en_name'] = en_names
read_csv.to_csv('../time_dist/国家(2).csv', encoding='utf-8', index=False)

print("导出完成")
import json
import pygal
from Ex_csv_and_worldMap.countrie_codes import get_country_code
from pygal.style import RotateStyle as RS, LightColorizedStyle as LCS


# 将数据加载到一个列表中
filename = "population_data.json"
with open(filename) as f:
    pop_data = json.load(f)
# print(type(pop_data))
cc_populations = {}
# 打印每个国家2010年的人口数据
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict["Value"]))
        print(country_name + " : " + str(population))
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population

# 按人口数据进行分组
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop
# 查看每组有多少个国家
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))

wm_style = RS("#336699", base_style=LCS)
wm = pygal.maps.world.World(style= wm_style)
wm.title = "World Population in 2010, by Country"
wm.add("0-10m", cc_pops_1)
wm.add("10m-1bn", cc_pops_2)
wm.add(">1bn", cc_pops_3)
wm.render_to_file("world_populations.svg")










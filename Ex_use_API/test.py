import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


# 执行API调用并存储响应
API = "https://api.github.com/search/repositories?q=language:python&sort=stars"
def get_Json(url):
    try:
        r = requests.get(url=url, timeout=10)
        r.raise_for_status()
        # r.encoding = r.apparent_encoding
        # 将API存储到字典中
        response_dict = r.json()
        return response_dict
    except:
        print("失败了")

response_dict = get_Json(API)
print("Total repositories", response_dict["total_count"])
repo_dicts = response_dict["items"]
print("Repositories returned:", len(repo_dicts))
# 研究第一个仓库
# repo_dict = repo_dicts[0]
# print("\nKeys:", len(repo_dict))
# for key in sorted(repo_dict.keys()):
#     print(key)
# names, stars = [], []
# print("\nSelect infomation about each repositories:")
# for repo_dict in repo_dicts:
#     print("\nSelected information about first repository:")
#     print("\nName:", repo_dict["name"])
#     print("full_name:", repo_dict["full_name"])
#     print("Owner:", repo_dict["owner"]["login"])
#     print("Stars:", repo_dict["stargazers_count"])
#     print("Repository:", repo_dict["html_url"])
#     print("Created:", repo_dict["created_at"])
#     print("Updated:", repo_dict["updated_at"])
#     print("Description:", repo_dict["description"])
#     print("---------------------------------------------------------------------")
stars = []
names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict["name"])
    stars.append(repo_dict["stargazers_count"])
    # plot_dict = {
    #     "value": repo_dict["stargazers_count"],
    #     "label": repo_dict["description"],
    #     'xlink': repo_dict['html_url'], # 给图表中添加可单机的链接
    # }
    # plot_dicts.append(plot_dict)
# 可视化处理
my_style = LS("#333366", base_style=LCS)
# 改进pygal图表
my_config = pygal.Config()
my_config.x_labels_rotation = 45
my_config.show_legend = True    # 是否显示一个代表标记按钮
my_config.title_font_size = 24  # 标题大小
my_config.label_font_size = 14  # 副标签标题大小， 即x轴上的项目名和y轴上的大部分数字
my_config.major_label_font_size = 18    # 主标签标题大小 即y轴上为5000整数倍的刻度
my_config.truncate_label = 15   # 将较长项目名缩短为15个字符
my_config.show_y_guides = False  # 是否有y轴刻度线
my_config.width = 1000
chart = pygal.Bar(my_config, style=my_style)
chart.title = "Most_Starred Python Project on GitHub"
chart.x_labels = names
chart.add("", stars)
chart.render_to_file("python_repos111.svg")
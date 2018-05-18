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
print(repo_dicts[15]["description"], repo_dicts[15]["name"])
# for i, dic in enumerate(repo_dicts):
#     print(i, dic["description"])

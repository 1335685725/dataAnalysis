from pygal_maps_world.i18n import COUNTRIES


def get_country_code(country_name):
    '''
    根据指定国家返回国别码
    :param country_name:
    :return:
    '''
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    return None
    # 没有找到就i返回None

# print(get_country_code("Andorra"))
# print(get_country_code("United Arab Emirates"))
# print(get_country_code("Afghanistan"))

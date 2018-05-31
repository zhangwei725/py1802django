from django import template

# 1|过滤器的名称:参数
# 名字格式都是固定的,不能修改
register = template.Library()


# add  +
@register.filter
def test_filter(value, param):
    return value + param


def test_filter1(value, p1, p2):
    return value * p1 * p2


@register.simple_tag
def test_tag(value, p1, p2, p3):
    return value + p1 + p2 + p3

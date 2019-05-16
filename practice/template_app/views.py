from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        "city": "深圳",
        "district": "宝安",
        "my_list": ['dota2', 'auto_chess', 'PUBG'],
        "my_dict": {"graphics_card": "GTX1080TI"},
        "my_html": "<h1>LGD是不可战胜的</h1>",
    }
    return render(request, 'index.html', context=context)

def index_child(request):
    context = {
        "city": "深圳",
        "district": "宝安",
        "my_list": ['dota2', 'auto_chess', 'PUBG'],
        "my_dict": {"graphics_card": "GTX1080TI"},
        "my_html": "<h1>LGD是不可战胜的</h1>",
    }
    return render(request, 'index_child.html', context=context)


def jinja2(request):
    context = {'my_list': [1, 2, 3, 4, 5]}
    return render(request, 'jinja2.html', context=context)
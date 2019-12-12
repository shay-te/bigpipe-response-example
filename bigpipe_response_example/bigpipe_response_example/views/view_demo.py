import random
from time import sleep

from bigpipe_response.bigpipe_response import BigpipeResponse
from bigpipe_response.pagelet import Pagelet

from data.demo_dao import DemoDAO

demo_dao = DemoDAO()


def demo(request):
    wait_from, wait_to = 1,12
    context = {
        'data': {
            'pagelet_news_feed_time': random.randrange(wait_from, wait_to),
            'pagelet_navigation_menu_time': random.randrange(wait_from, wait_to),
            'pagelet_information_boxes_time': random.randrange(wait_from, wait_to)
        }
    }

    pagelets = [
        Pagelet(request, 'pagelet_top_blue_bar', top_blue_bar, {}),
        Pagelet(request, 'pagelet_news_feed', news_feed, {'param_1': 0, 'sleep_time': context['data']['pagelet_news_feed_time']}),
        Pagelet(request, 'pagelet_navigation_menu', navigation_menu, {'sleep_time': context['data']['pagelet_navigation_menu_time']}),
        Pagelet(request, 'pagelet_information_boxes', information_boxes, {'sleep_time': context['data']['pagelet_information_boxes_time']}),
        Pagelet(request, 'pagelet_chat', chat, {})
    ]
    return BigpipeResponse(request,
                           render_type=BigpipeResponse.RenderType.TEMPLATE,
                           render_source='demo.html',
                           render_context=context,
                           pagelets=pagelets,
                           js_dependencies=['demo_pagelet_timer'],
                           scss_dependencies=['@demo_main'])


# Server side rendering
def top_blue_bar(request):
    return BigpipeResponse(request,
                           render_type=BigpipeResponse.RenderType.JAVASCRIPT_RENDER,
                           render_source='TopBlueBar')


def news_feed(request, param_1, sleep_time):
    sleep(sleep_time)
    return BigpipeResponse(request,
                           render_type=BigpipeResponse.RenderType.JAVASCRIPT,
                           render_source='NewsFeed',
                           render_context=demo_dao.get_news_feed())


def navigation_menu(request, sleep_time):
    sleep(sleep_time)
    return BigpipeResponse(request,
                           render_type=BigpipeResponse.RenderType.JAVASCRIPT,
                           render_source='NavigationMenuList',
                           render_context=demo_dao.get_navigation_items())


def information_boxes(request, sleep_time):
    sleep(sleep_time)
    return BigpipeResponse(request,
                           render_type=BigpipeResponse.RenderType.JAVASCRIPT,
                           render_source='ListInformationGenerator',
                           render_context=demo_dao.get_custom_information())


def chat(request):
    return BigpipeResponse(request,
                           render_type=BigpipeResponse.RenderType.JAVASCRIPT,
                           render_source='Chat')


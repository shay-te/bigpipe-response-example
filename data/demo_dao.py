import os
import random

from django.utils.translation import gettext

words = """
It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal 
distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum
 as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).
"""

# all images are from https://www.freeimages.com/
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
images_dir = os.path.join(parent_dir, 'public', 'images')
images_prefix = 'public/images'

images = ['{}/{}'.format(images_prefix, f) for f in os.listdir(images_dir)]


def random_words(min_words_count, max_word_count: int = None):
    if not max_word_count:
        max_word_count = len(words) - 1
    words_copy = words.split(" ")
    random.shuffle(words_copy)
    return ' '.join(words_copy[0:random.randrange(min_words_count, max_word_count)])


custom_info_components = ['ListingInformationGrid', 'ComponentPost']


def get_component_context(component_name, title_minimum_words, content_minimum_words):
    if component_name == 'ListingInformationGrid':
        images_copy = images.copy()
        random.shuffle(images_copy)
        return {'title': random_words(3), 'size': 2, 'images': images_copy[0:4]};
    if component_name == 'ComponentPost':
        return {
            'title': random_words(title_minimum_words),
            'content': random_words(content_minimum_words)
        }
    return {}


class DemoDAO(object):

    def __init__(self, config):
        self.conf = config

    @property
    def config(self):
        return self.conf

    def get_news_feed(self):
        locale_post = [
            {
                'title': gettext('post_title_1'),
                'content': random_words(15),
                'image': images[random.randint(0, len(images) - 1)] if bool(random.getrandbits(1)) else None
            },
            {
                'title': 'post_title_2',
                'content': random_words(15),
                'image': images[random.randint(0, len(images) - 1)] if bool(random.getrandbits(1)) else None
            }
        ]
        return {'feed': locale_post + [{
                'title': 'I am post title {}'.format(i),
                'content': random_words(15),
                'image': images[random.randint(0, len(images)-1)] if bool(random.getrandbits(1)) else None
            } for i in range(1, 25)]
        }

    def get_navigation_items(self):
        navigation_main = {
            'title': 'Favorites',
            'menu_items':[
                {'icon': 'fa-user', 'label': 'my name'},
                {'icon': 'fa-newspaper', 'label': gettext('News Feed')},
                {'icon': 'fa-video', 'label': gettext('Videos on Watch')},
                {'icon': 'fa-store', 'label': gettext('Marketplace')}
            ]
        }

        navigation_shortcuts = {
            'title': gettext('Shortcuts'),
            'menu_items': [
                {'icon': 'fa-ellipsis-h', 'label': random_words(3, 4)},
                {'icon': 'fa-ellipsis-h', 'label': random_words(3, 4)},
                {'icon': 'fa-ellipsis-h', 'label': random_words(3, 4)},
                {'icon': 'fa-ellipsis-h', 'label': random_words(3, 4)}
            ]
        }

        return {'menus': [navigation_main, navigation_shortcuts]}

    def get_custom_information(self):
        custom_info = []
        for i in range(3, random.randint(6, 10)):
            component = custom_info_components[random.randrange(0, len(custom_info_components))]
            custom_info.append({'component': component, 'context': get_component_context(component, self.conf.title_minimum_word_count, self.conf.content_minimum_word_count)})
        return {'renderComponents': custom_info}

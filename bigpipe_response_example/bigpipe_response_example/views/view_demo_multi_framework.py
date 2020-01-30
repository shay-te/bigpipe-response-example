from bigpipe_response.bigpipe import Bigpipe
from bigpipe_response.bigpipe_render_options import BigpipeRenderOptions
from bigpipe_response.helpers import to_include

from bigpipe_response.bigpipe_response import BigpipeResponse
from bigpipe_response.pagelet import Pagelet

from bigpipe_response_example.bigpipe_processors.VueDOMBind import VueDOMBind
from data.app_instance import AppInstance

demo_dao = AppInstance.get()

js_dependencies = to_include(['React=react', 'ReactDOM=react-dom', 'createReactClass=create-react-class', 'Vue=vue.default'],
                             is_link=True,
                             processor_name=Bigpipe.get().config.processors.js_modules.params.processor_name)


def demo(request):

    pagelets = [
        Pagelet(request, 'vue-container', vue_view, {}),
        Pagelet(request, 'markdown-container', markdown_view, {}),
    ]
    return BigpipeResponse(request,
                           render_type=BigpipeResponse.RenderType.TEMPLATE,
                           render_source='demoMultipleFrameworks.html',
                           pagelets=pagelets,
                           js_dependencies=js_dependencies,
                           scss_dependencies=['@demo_main'])


def vue_view(request):
    return BigpipeResponse(request,
                           render_type=BigpipeResponse.RenderType.JAVASCRIPT,
                           render_source='DynamicList',
                           render_options=BigpipeRenderOptions(js_processor_name='vue', js_dom_bind=VueDOMBind()))


def markdown_view(request):
    return BigpipeResponse(request,
                           render_type=BigpipeResponse.RenderType.JAVASCRIPT_RENDER,
                           render_source='markdown_demo',
                           render_options=BigpipeRenderOptions(js_processor_name='markdown'))

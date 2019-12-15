from bigpipe_response.bigpipe_response import BigpipeResponse


def demo(request):
    return BigpipeResponse(request,
                           render_type=BigpipeResponse.RenderType.JAVASCRIPT_RENDER,
                           render_source='LandingPage')


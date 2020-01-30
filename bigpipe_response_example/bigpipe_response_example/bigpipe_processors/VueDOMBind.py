import json

from bigpipe_response.javascript_dom_bind.javascript_dom_bind import JavascriptDOMBind


class VueDOMBind(JavascriptDOMBind):
    def generate_bind_command(self, render_source: str, render_context: dict, target_element: str):
        return """
        new Vue({{
                runtimeCompiler: true,
                render: {component},
                props: {context},
            }}).$mount("#{element}")
        """.format(component=render_source, context=json.dumps(render_context), element=target_element)

from pathlib import Path

from bigpipe_response.processors.base_file_processor import BaseFileProcessor
import markdown2


class MarkdownProcessor(BaseFileProcessor):

    def process_resource(self, input_file: str, output_file: str, include_dependencies: list, exclude_dependencies: list, options: dict = {}):
        fp = open(output_file, "w", encoding='utf-8')
        fp.write(self.__from_input(input_file))
        fp.close()

    def render_resource(self, input_file: str, context: dict, i18n: dict):
        return self.__from_input(input_file)

    def __from_input(self, input_file):
        return markdown2.markdown(Path(input_file).read_text(), extras=[])

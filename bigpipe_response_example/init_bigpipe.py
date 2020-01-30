import os

import hydra
from bigpipe_response.processors.remote_js_file_processor import RemoteJsFileProcessor
from omegaconf import OmegaConf
from bigpipe_response.bigpipe import Bigpipe

project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def create_processors():
    vue_processor = RemoteJsFileProcessor('vue',
                                          'bigpipe_response_example.bigpipe_processors.VueProcessor.js',
                                          [os.path.join(project_path, 'client', 'vue')],
                                          source_ext=['js', 'vue'],
                                          target_ext='js')
    return [vue_processor]


def init_bigpie(bigpipe_config):
    OmegaConf.register_resolver('full_path', lambda sub_path: os.path.join(project_path, sub_path.replace("\\", "/")))
    Bigpipe.init(bigpipe_config, create_processors())  # Setup bigpipe


@hydra.main(config_path="../config/app_config.yaml")
def main(cfg):
    init_bigpie(cfg.bigpipe)
    Bigpipe.get().shutdown()

if __name__ == '__main__':
    main()
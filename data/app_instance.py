from data.demo_dao import DemoDAO


class AppInstance(object):
    _app_instance = None

    @staticmethod
    def init(cfg):
        if not AppInstance._app_instance:
            AppInstance._app_instance = DemoDAO(cfg)

    @staticmethod
    def get():
        return AppInstance._app_instance

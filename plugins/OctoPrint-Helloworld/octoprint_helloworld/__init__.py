
import logging
import logging.handlers
import octoprint.plugin

# https://docs.octoprint.org/en/master/plugins/mixins.html#sec-plugins-mixins
# https://docs.octoprint.org/en/master/plugins/mixins.html#sec-plugins-mixins-injectedproperties


#  https://docs.octoprint.org/en/master/plugins/mixins.html#startupplugin
class HelloWorldPlugin(octoprint.plugin.StartupPlugin,
                       octoprint.plugin.TemplatePlugin,
                       octoprint.plugin.SettingsPlugin):
    
    def __init__(self):
        self._console_logger = None

    def initialize(self):
        self._console_logger = logging.getLogger("octoprint.plugins.helloworld")

    def on_startup(self, host, port):
        console_logging_handler = logging.handlers.RotatingFileHandler(
            self._settings.get_plugin_logfile_path(postfix="helloworld"), maxBytes=2 * 1024 * 1024)
        console_logging_handler.setFormatter(logging.Formatter("%(asctime)s %(message)s"))
        console_logging_handler.setLevel(logging.INFO)

        self._console_logger.addHandler(console_logging_handler)
        self._console_logger.setLevel(logging.INFO)
        self._console_logger.propagate = False

    def on_after_startup(self):
        self._console_logger.info("Console Logger Hello World!")
        self._logger.info("Logger Hello World!")

    def get_settings_defaults(self):
        return dict(url="https://en.wikipedia.org/wiki/Hello_world")
        
    def get_template_configs(self):
        return [
            dict(type="navbar", custom_bindings=False),
            dict(type="settings", custom_bindings=False)
        ]

__plugin_pythoncompat__ = ">=3.7,<4"
__plugin_implementation__ = HelloWorldPlugin()
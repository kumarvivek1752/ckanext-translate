import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

from ckan.lib.plugins import DefaultTranslation


# ckanext_multilingual/ckanext_multilingual/plugin.py
# from ckanext.scheming import plugin as scheming_plugin


from ckan.plugins import implements, interfaces
from ckan.plugins import SingletonPlugin

# import ckanext.fluent.plugin as fluent_plugin


class TranslatePlugin(plugins.SingletonPlugin, DefaultTranslation):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(interfaces.IConfigurable, inherit=True)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, "templates")
        toolkit.add_public_directory(config_, "public")
        toolkit.add_resource("fanstatic", "translate")

        config_[
            "scheming.dataset_schemas"
        ] = "ckanext.translate:schemas/translate_dataset.json"
        # config_[
        #     "scheming.dataset_schemas"
        # ] = "ckanext.translate:schemas/ckan_dataset.yaml"
        config_[
            "scheming.presets"
        ] = """
        ckanext.scheming:presets.json
        ckanext.fluent:presets.json
        """

    def configure(self, config):
        # Register your custom schema file(s)
        # scheming_plugin.register_scheming_datasets('schemas/translate_dataset.json')
        pass

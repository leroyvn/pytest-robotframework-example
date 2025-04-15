def check_plugin(config, name):
    items = dict(config.pluginmanager.list_name_plugin())
    if name in items:
        if items[name] is not None:
            return True
    return False

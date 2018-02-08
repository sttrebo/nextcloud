from subprocess import check_output
from syncloud_app import logger


class OCConsole:
    def __init__(self, occ_runner_path):
        self.occ_runner_path = occ_runner_path
        self.log = logger.get_logger('nextcloud_occ')

    def run(self, args):
        
        output = check_output('{0} {1}'.format(self.occ_runner_path, args), shell=True).strip()
        if output:
            self.log.info(output)
        return output


class OCConfig:
    def __init__(self, oc_config_path):
        self.oc_config_path = oc_config_path
        self.log = logger.get_logger('nextcloud_config')
        
    def set_value(self, key, value):
        self.log.info('setting value: {0} = {1}'.format(key, value))
        output = check_output('{0} {1} {2}'.format(
            self.oc_config_path,
            key,
            "'{0}'".format(value)), shell=True).strip()
        if output:
            self.log.info(output)
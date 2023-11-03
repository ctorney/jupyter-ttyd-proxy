"""
Return config on servers to start for jupyter-ttyd-proxy

"""
import os


def setup_ttyd():

    def _get_command(port):
        return ['ttyd', '-W', '-p', '{}'.format(port), 'bash']

    return {
        'command': _get_command,
        'absolute_url': False,
        'environment': {},
        'launcher_entry': {
            'title': 'jupyter-ttyd-proxy',
            'icon_path': os.path.join(os.path.dirname(os.path.abspath(__file__)), 'icons', 'jupyter-ttyd-proxy.svg')
        }
    }

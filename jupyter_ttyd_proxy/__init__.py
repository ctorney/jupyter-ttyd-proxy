"""
Return config on servers to start for jupyter-ttyd-proxy

"""
import os
import shutil


def setup_ttyd():

    def _get_command(port):
        
        executable = shutil.which('ttyd')
        if executable is None:
            raise FileNotFoundError('Cannot find ttyd executable')

        executable = shutil.which('zellij')
        if executable is None:
            return ['ttyd', '-W', '-p', '{}'.format(port), "-t", "fontSize=14", "-t", "enableSixel=true", "-t", "fontFamily=HackNerdFontMono", "-t", "titleFixed=jupyterhub",  '-t', 'enableSixel=true', '-t', 'disableReconnect=true', 'bash']
        else:
            return ['ttyd', '-W', '-p', '{}'.format(port), "-t", "fontSize=14", "-t", "enableSixel=true", "-t", "fontFamily=HackNerdFontMono", "-t", "titleFixed=Zellij",  '-t', 'enableSixel=true', '-t', 'disableReconnect=true', "zellij", "attach", "-c", "'jupyterhub'"]

    return {
        'command': _get_command,
        'absolute_url': False,
        'environment': {},
        'launcher_entry': {
            'title': 'Zellij (ttyd)',
            'icon_path': os.path.join(os.path.dirname(os.path.abspath(__file__)), 'icons', 'jupyter-ttyd-proxy.png')
        }
    }

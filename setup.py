import setuptools

setuptools.setup(
    name="jupyter-ttyd-proxy",
    version='1.0dev',
    url="https://github.com/ctorney/jupyter-ttyd-proxy",
    author="Colin Torney",
    description="colin.j.torney@gmail.com",
    packages=setuptools.find_packages(),
	keywords=['Jupyter'],
	classifiers=['Framework :: Jupyter'],
    install_requires=[
        'jupyter-server-proxy'
    ],
    entry_points={
        'jupyter_serverproxy_servers': [
            'ttyd = jupyter_ttyd_proxy:setup_ttyd',
        ]
    },
    package_data={
        'jupyter_ttyd_proxy': ['icons/*'],
    },
)

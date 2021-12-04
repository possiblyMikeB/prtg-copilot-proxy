from setuptools import setup, find_packages, findall

setup(
    name='prtg-copilot-proxy',
    version='0.1',
    description='Proxy allowing PRTG\'s "HTTP Data Advanced" to retrieve metrics from PCP (https://pcp.io) via `pmproxy`',
    author="Michael Blackmon",
    author_email="differentiablef@gmail.com",
    url='https://github.com/possiblyMikeB/prtg-copiloy-proxy/',
    packages=find_packages(),
    entry_points = {
        'console_scripts': [
            'prtg-copilot-proxy=prtg_copilot_proxy.__main__:main'
        ]
    },
    install_requires=[
        'tornado>=6.1',
        'requests>=2.25.1'
    ]
)   
      
      

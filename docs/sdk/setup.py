from distutils.core import setup

setup(
    name='opssdk',
    version='0.0.1',
    packages=['opssdk', 'opssdk.logs', 'opssdk.operate', 'opssdk.install', 'opssdk.get_info', 'opssdk.utils', 'websdk'],
    url='https://github.com/ss1917/ops_sdk/',
    license='',
    install_requires=['fire',
                      'shortuuid',
                      'pymysql==0.9.3',
                      'python3-pika==0.9.14',
                      'PyJWT',
                      'requests',
                      'redis==2.10.6',
                      'tornado==5.0',
                      'python-dateutil==2.7.5',
                      'ldap3==2.6',
                      'django==2.2.13',
                      'pycryptodome'
                      ],
    author='actanble',
    author_email='actanble@gmail.com',
    description='SDK of the operation and maintenance script' 'logs' 'operate'
)
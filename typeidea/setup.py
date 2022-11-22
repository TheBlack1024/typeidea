
from setuptools import setup,find_packages

packages = find_packages('typeidea')
print(packages)

setup(
    name = 'typeidea',
    version = '${version}',
    description = 'Blog System base on Django',
    author = 'TheBlack',
    author_email = '912182005@qq.com',
    url = 'https://www.the5fire.com',
    license='MIT',
    packages = packages,
    package_dir = {'': 'typeidea'},
    #package_data = {'': [  #方法一：打包数据文件
        #'themes/*/*/*/*',  #需要按目录层级匹配
    #]},
    include_package_data=True, #方法二：配合MANIFEST.in文件
    install_requires=[
        'django~=2.0',
        'gunicorn==19.9.0',
        'supervisor==4.0.3',
        'xadmin==2.0.1',
        'mysqlclient==1.4.2.post1',
        'django-ckeditor==5.4.0',
        'django-rest-framework==0.1.0',
        'django-redis==4.10.0',
        'django-autocomplete-light==3.2.10',
        'mistune==0.8.4',
        'Pillow==9.3.0',
        'coreapi==2.3.3',
        # debug
        'django-debug-toolbar==1.11',
        'django-silk==3.0.2',
    ],
    extras_require = {
        'ipython': ['ipython==7.5.0']
    },
    scripts = [
        'typeidea/manage.py',
    ],
    entry_points={
        'console_scripts':[
            'typeidea_manage = manage:main',
        ]
    },
    classifiers = [ #Optional
        # 软件成熟度如何？一般有下面几种选项
        # 3-Alpha
        # 4-Beta
        # 5-Production/Stable
        'Development Status :: 3 - Alpha',

        #指明项目的受众
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',


        #选择项目的许可证（Licenes)
        'License :: OSI Approved :: MIT License',

        #指定项目需要使用的Python版本
        'Programming Language :: Python :: 3.7',

    ],
)
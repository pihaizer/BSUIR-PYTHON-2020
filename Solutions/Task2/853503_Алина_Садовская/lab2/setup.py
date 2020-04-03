from distutils.core import setup

setup(
    name='lab2',
    version='',
    package_dir={'lab2': '../lab2'},
    packages=['lab2', 'lab2.code', 'lab2.code.catched', 'lab2.code.json_conv', 'lab2.code.singleton',
              'lab2.code.sort_in_memory', 'lab2.code.vector', 'lab2.tests', 'lab2.tests.catched',
              'lab2.tests.vector', 'lab2.tests.json_test', 'lab2.tests.sort', 'lab2.tests.singleton'],
    url='',
    license='',
    author='AlinaSadovskaya',
    author_email='alinasadovsckaya@yandex.ru',
    description='my lab 2', requires=['numpy', 'numpy']
)
#  Copyright 2019 Universidade Estadual de Santa Cruz
#
#  Author: Prof. Mathias Santos de Brito <msbrito@uesc.br>
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from setuptools import setup, find_packages


setup(
    name='cet-tools',
    version='0.1a1',
    description='Ferramenta CLI para o auxílio de gerenciamento de '
                'disciplinas e aulas para a UESC.',
    long_description='Este software consiste em um conjunto de ferrametas '
                     'para auxiliar no gerecimaneto de disciplinas e aulas. '
                     'Elas foram desenvolvidas com base nas especificidades da'
                     'Universidade Estadual de Santa Cruz. O sistema visa ser'
                     'um facilitador para os professores que preferem utilizar'
                     'terminais ao invés de ambientes gráficos.',
    long_description_content_type='text/markdown',
    author='Mathias Santos de Brito',
    author_email='msbrito@uesc.br',
    url='https://github.com/mathiasbrito/CET-Tools',
    include_package_data=True,
    packages=find_packages(),
    setup_requires=['pytest-runner'],
    install_requires=['click', 'tabulate', 'scrapy'],
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'cet-tools=scripts.cet_tools:main',
        ]
    },
    python_requires='>=3.6',
    license="APACHE 2.0",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Operating System :: OS Independent"
    ],
)


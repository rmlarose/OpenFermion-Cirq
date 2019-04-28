# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import io
from setuptools import find_packages, setup

# This reads the __version__ variable from openfermioncirq/_version.py
__version__ = None
exec(open('openfermioncirq/_version.py').read())

# Readme file as long_description:
long_description = ('================\n' +
                    'OpenFermion-Cirq\n' +
                    '================\n')
stream = io.open('README.rst', encoding='utf-8')
stream.readline()
long_description += stream.read()
description = ('Quantum circuits for simulations ' +
               'of quantum chemistry and materials.')

# Read in runtime-requirements.txt
requirements = open('requirements.txt').readlines()
requirements = [r.strip() for r in requirements]

openfermioncirq_packages = ['openfermioncirq'] + [
    'openfermioncirq.' + package
    for package in find_packages(where='openfermioncirq')
]

setup(
    name='openfermioncirq',
    version=__version__,
    url='https://github.com/quantumlib/OpenFermion-Cirq',
    author='The OpenFermion Developers',
    author_email='openfermioncirq@googlegroups.com',

    # CAUTION: the semantics of python_requires and how it interacts with PYPI
    # are extremely inconvenient, so read this before changing it.
    #
    # One would assume that, because each wheel within a package specifies a
    # python_requires line, PYPI would consider the python_requires of the
    # package to be the union of each of its wheels. This is not the case. What
    # PYPI actually does is assert that the python_requires of the package is
    # the python_requires of the *first wheel uploaded to the package*. So if
    # you have a wheel targeting python 2, and set "python_requires='2.7.*'"
    # for that wheel, then it doesn't matter how many python 3 wheels you add to
    # the package; python 3 users will not be able to pip install them.
    #
    # The workaround for this problem is to set the actual python_requires of
    # all wheels in a package to the union of the desired python_requires of all
    # the wheels in the package (or to not set it at all). Then, when uploading
    # wheels, ensure that their names encode the version they are targeting. For
    # example, a wheel named 'cirq-#.#.#-py27-none-any.whl' will only be
    # installed in python 2.7.
    python_requires='>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*,!=3.6.4',

    install_requires=requirements,
    license='Apache 2',
    description=description,
    long_description=long_description,
    packages=openfermioncirq_packages)

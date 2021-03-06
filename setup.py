from setuptools import setup, find_packages

setup(
    name='django-file-picker',
    version='0.6.0',
    author='Caktus Consulting Group',
    author_email='solutions@caktusgroup.com',
    packages=find_packages(exclude=['sample_project']),
    include_package_data=True,
    #url='https://github.com/caktus/django-file-picker/',
    url='http://django-file-picker.readthedocs.org/',
    license='BSD',
    description='Pluggable file picker',
    classifiers=[
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
    ],
    long_description=open('README.rst').read(),
    install_requires=['sorl-thumbnail==12.3',],
    zip_safe=False, # because we're including media that Django needs
)


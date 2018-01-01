from setuptools import setup

setup(
    name='gvcci',
    version='0.0.1',
    description='color extraction to turn images into 16 color palettes',
    url='https://github.com/FabriceCastel/gvcci',
    author='Fabrice Castel',
    author_email='fabrice.castel@hotmail.com',
    license='MIT',
    packages=['gvcci'],
    scripts=['bin/gvcci'],
    include_package_data=True,
    install_requires=[
        "numpy",
        "scikit-learn",
        "scikit-image",
        "pystache",
        "hasel>=1.0.1"
    ],
    dependency_links=[
        "https://github.com/sumartoyo/hasel.git"
        "tarball/master#egg=package-1.0.1"
    ]
)

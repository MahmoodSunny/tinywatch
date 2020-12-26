from setuptools import setup

OPTIONS = {
    'iconfile': 'stopwatch.png'
    }
setup(
    app=["tinywatch.py"],
    options={'py2app': OPTIONS},
setup_requires=["py2app"]
)
from setuptools import setup, find_packages

def readme():
    try:
        with open('README.md') as f:
            return f.read()
    except:
        pass

setup(name='instagram-download',
	version='1.1.0',
	description='Download pictures from instagram',
	author='Subhrajit Prusty',
	url='https://github.com/SubhrajitPrusty/instagram-download/',
	author_email='subhrajit1997@gmail.com',

	long_description=readme(),  
	long_description_content_type='text/markdown', 
	license='MIT',

	setup_requires=['setuptools>=40.0.0'],
      
	install_requires=['splinter', 'bs4', 'click'],
      	packages=find_packages(),
	entry_points="""
	[console_scripts]
		instagram-dl=instagram:insta
	"""
)

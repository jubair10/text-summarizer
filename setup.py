import setuptools

with open('Readme.md', 'r') as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = 'End-to_end-Text-Sumarization'
AUTHOR_USER_NAME = 'jubair10'
SRC_REPO = 'text-summarizer'
AUTHOR_EMAIL = 'mdnahiyan4000@gmail.com'

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description='End-to-end text summarization using BERT and Hugging Face Transformers',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=f'https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}',
    project_url={
        "Bug Tracker": f'https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues'
        },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where='src'),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Text Processing :: Natural Language Processing',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Linguistic',
        'Topic :: Text Processing :: Natural Language Generation',
        'Topic :: Text Processing :: Filters',
        'Topic :: Text Processing :: Translation',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Natural Language Processing',
        'Topic :: Text Processing :: Linguistic',
        'Topic :: Text Processing :: Natural Language Generation',
        'Topic :: Text Processing :: Filters',
        'Topic :: Text Processing :: Translation',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Natural Language Processing',
        'Topic :: Text Processing :: Linguistic',
        'Topic :: Text Processing :: Natural Language Generation',],
    python_requires='>=3.6',
)



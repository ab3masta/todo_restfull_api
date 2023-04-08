from setuptools import setup, find_packages

setup(
    name='todo-restfull-api',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'fastapi',
        'uvicorn',
        'pymongo',
        'psycopg2-binary',
        'firebase-admin'
    ],
    entry_points={
        'console_scripts': [
            'todo-restfull-api=todo-restfull-api.cli:app.main'
        ]
    },
    author='Abdou Abarchi Aboubacar',
    author_email='aboubacarabdouabarchidev@gmail.com',
    description='📝🔗 Todo RESTful API: A fast and modern API built with FastAPI and Python for managing tasks, using Firebase, MongoDB, and PostgreSQL as data storage.',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)

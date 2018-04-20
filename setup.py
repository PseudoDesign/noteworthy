from setuptools import find_packages, setup

with open("README.md") as f:
    long_description = f.read()

setup(
    name="noteworthy",
    long_description=long_description,
    long_description_content_type="text/markdown",
    version="0.0.1.dev0",
    author="Pseudo Design <info@pseudo.design>",
    install_requires=['pylast', 'wget'],
    tests_require=[],
    description="A Python application for retrieving a user's currently streaming last.fm song.",
    author_email="info@pseudo.design",
    url="https://github.com/PseudoDesign/noteworthy",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: MIT License",
        "Topic :: Internet",
        "Topic :: Multimedia :: Sound/Audio",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    python_requires='>=3.6.*',
    keywords=["Last.fm", "music", "scrobble", "scrobbling", "OBS", "Streamlabs"],
    packages=find_packages(exclude=('tests*',)),
    license="MIT",
    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
        'console_scripts': [
            'noteworthy=noteworthy:main',
        ],
    },
)

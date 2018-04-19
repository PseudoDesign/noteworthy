from setuptools import find_packages, setup

with open("README.md") as f:
    long_description = f.read()

setup(
    name="now_playing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    version="0.0.1.dev0",
    author="Pseudo Design <info@pseudo.design>",
    install_requires=['pylast'],
    tests_require=['mock', 'pytest', 'coverage', 'pycodestyle', 'pyyaml',
                   'pyflakes', 'flaky'],
    description="A Python interface to Last.fm and Libre.fm",
    author_email="info@pseudo.design",
    url="https://github.com/PseudoDesign/now_playing",
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
    license="MIT"
)

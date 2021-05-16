import setuptools

with open("README.md" , "r") as f:
    long_description = f.read()

setuptools.setup(
      name="pyculas",
      version="2.0",
      author="Yash Indane",
      author_email="yashindane46@gmail.com",
      description="calculas python library",
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/YashIndane/pyculas",
      packages=setuptools.find_packages(),
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
      ],
      python_requires='>=3.6',
)

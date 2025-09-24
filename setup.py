from setuptools import setup, find_packages

setup(
    name="product-sales-analysis",
    version="1.0.0",
    description="A Python project for analyzing product sales data with pandas, matplotlib, and seaborn.",
    author="Prem Chavan",
    author_email="premchavanzoub@gmail.com",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy",
        "matplotlib",
        "seaborn",
        "jupyter",
        "openpyxl"
    ],
    python_requires=">=3.7",
)

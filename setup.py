from setuptools import setup, find_packages

setup(
    name="mlflow_e2e_project",
    version="0.1.0",
    author="Pranav Suryawanshi",
    author_email="your.email@example.com",
    description="End-to-End ML pipeline with Flask and MLflow integration.",
    packages=find_packages(),
    install_requires=[
        "flask>=2.0",
        "numpy>=1.21",
        "pandas>=1.3",
        "scikit-learn>=1.0",
    ],
    include_package_data=True,
    python_requires=">=3.7",
)

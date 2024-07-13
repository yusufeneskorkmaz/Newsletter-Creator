from setuptools import setup, find_packages

setup(
    name="NewsletterCreator",
    version="0.1.0",
    author="yusufeneskorkmaz",
    author_email="yusufeneskorkmaz@outlook.com",
    description="A tool for summarizing multiple URLs and translating the summaries",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "langchain",
        "langchain_community",
        "beautifulsoup4",
        "gradio",
        "requests",
    ],
    entry_points={
        "console_scripts": [
            "multi-url-summarizer=MultiURLSummarizer.main:main",
        ],
    },
)
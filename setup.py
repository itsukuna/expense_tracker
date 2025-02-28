from setuptools import setup

setup(
    name="expense_tracker",
    version="0.1",
    entry_points={
        "console_scripts": [
            "expense_tracker=expense_tracker:main",
        ],
    },
    python_requires=">=3.10",
    author="Ayush Singh Arya",
    description="A CLI tool to track and manage expenses.",
    url="https://github.com/itsukuna/expense_tracker.git",
)

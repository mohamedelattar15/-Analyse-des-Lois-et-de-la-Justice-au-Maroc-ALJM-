import os

directories = [
    "data",
    "notebooks",
    "src/scraper",
    "src/processing",
    "src/rag",
    "src/models",
    "src/utils",
    "app",
    "docs"
]

for directory in directories:
    os.makedirs(directory, exist_ok=True)
    print(f"Directory created: {directory}")

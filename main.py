import os
os.environ['USER_AGENT'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'

import logging
from MultiURLSummarizer.pipeline.summarize_pipeline import SummarizePipeline
from MultiURLSummarizer.config.configuration import get_config

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')
logger = logging.getLogger(__name__)


def main():
    config = get_config()
    logger.info("Initializing Summarize Pipeline")
    pipeline = SummarizePipeline()

    print("Multi-URL Summarizer and Translator")
    print("Enter URLs (one per line, press Enter twice when done):")
    urls = []
    while True:
        line = input()
        if line:
            urls.append(line)
        else:
            break
    urls_input = "\n".join(urls)

    print("\nSelect target language:")
    print("1. Original")
    print("2. English")
    print("3. Turkish")
    language_choice = input("Enter your choice (1-3): ")
    language_map = {"1": "Original", "2": "English", "3": "Turkish"}
    target_language = language_map.get(language_choice, "Original")

    logger.info("Processing URLs")
    result = pipeline.run(urls_input, target_language)

    print("\nSummaries:")
    print(result)


if __name__ == "__main__":
    main()
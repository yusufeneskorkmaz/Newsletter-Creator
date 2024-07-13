import logging
from typing import List
from MultiURLSummarizer.components.summarizer import summarize_url
from MultiURLSummarizer.components.translator import translate_text
from MultiURLSummarizer.utils.common import is_valid_url, clean_text
from MultiURLSummarizer.config.configuration import get_config

logger = logging.getLogger(__name__)

class SummarizePipeline:
    def __init__(self):
        self.config = get_config()

    def process_urls(self, urls: str, target_language: str) -> List[str]:
        summaries = []
        for url in urls.split('\n'):
            url = url.strip()
            if is_valid_url(url):
                try:
                    summary = summarize_url(url)
                    if target_language != "Original":
                        summary = translate_text(summary, target_language)
                    summaries.append(clean_text(summary))
                except Exception as e:
                    # Handle connection errors specifically
                    if "ConnectionError" in str(e):
                        logger.error(f"Connection error while summarizing URL {url}: {str(e)}")
                        summaries.append("Summarization service unavailable")
                    else:
                        logger.error(f"Error processing URL {url}: {str(e)}")
                        summaries.append(f"Error processing URL: {url}")
            else:
                summaries.append(f"Invalid URL: {url}")
        return summaries

    def run(self, urls: str, target_language: str) -> str:
        summaries = self.process_urls(urls, target_language)
        return "\n\n".join(summaries)

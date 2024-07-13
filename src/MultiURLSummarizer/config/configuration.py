from dataclasses import dataclass, field
from typing import List

@dataclass
class SummarizerConfig:
    model: str = "llama3:instruct"
    base_url: str = "http://127.0.0.1:11434"

@dataclass
class TranslatorConfig:
    model: str = "llama3:instruct"
    base_url: str = "http://127.0.0.1:11434"

@dataclass
class Config:
    summarizer: SummarizerConfig = field(default_factory=SummarizerConfig)
    translator: TranslatorConfig = field(default_factory=TranslatorConfig)
    supported_languages: List[str] = field(default_factory=lambda: ["Original", "English", "Turkish"])

def get_config() -> Config:
    return Config()
# Newsletter Creator

This project aims to simplify the process of monitoring news and internet content by leveraging advanced AI technology to summarize and translate articles from around the whole internet.

## Features

- **Aggregation and Summarization**: Users can fetch news articles from specified URLs and summarize them using the Llama 3 model.
- **Gradio Interface**: The user-friendly Gradio interface simplifies interaction, allowing users to input URLs and view summarized text effortlessly.
- **Translation Feature**: The app includes a translation functionality, enabling users to translate summarized texts into their desired languages.

## Project Structure

```
Newsletter-Creator/
│
├── src/
│   └── MultiURLSummarizer/
│       ├── components/
│       │   ├── summarizer.py
│       │   └── translator.py
│       ├── config/
│       │   └── configuration.py
│       ├── pipeline/
│       │   └── summarize_pipeline.py
│       └── utils/
│
├── tests/
│   ├── test_summarizer/
│   └── test_translator/
├── main.py
├── app.py
├── setup.py
├── requirements.txt
└── README.md
```
## Screenshot from Gradio App

To use the Newsletter Creator in you web browser via gradio app.

```
python app.py
```


[![capture-20240714005101209.png](https://i.postimg.cc/q7pvj114/capture-20240714005101209.png)](https://postimg.cc/sM0z24FN)

## Requirements

ollama must be installed and served:
   ```
   ollama run llama3:instruct
   ```

Install the required packages:
   ```
   pip install -e .
   ```

## Usage

To use the Newsletter Creator, run the script from the command line, providing the URL of the document you wish to summarize::

```
python summarizer.py -u "http://example.com/article" "http://anotherexample.com/research" "http://example.org/news"

```

This script will:
- Scrapes data from the URL you provide
- Transform the data
- Summaries according to instructions
- Provides translation according to your preference


## File Descriptions

- `main.py`: Script for running the full training pipeline
- `app.py`: Gradio application for the web interface
- `src/MultiURLSummarizer/components/`: Contains modules for summarization and translation.
- `src/MultiURLSummarizer/config/`: Contains configuration settings
- `src/MultiURLSummarizer/pipeline/`: Contains summarization pipeline scripts
- `src/MultiURLSummarizer/utils/`: Contains utility functions


## Dependencies

Main dependencies include:
- langchain
- langchain_community
- beautifulsoup4
- gradio
- requests

See `requirements.txt` for a full list of dependencies.

## Contributing

Contributions to improve the model, extend the functionality, or improve documentation are welcome. Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).
import gradio as gr
from MultiURLSummarizer.components.summarizer import summarize_url
from MultiURLSummarizer.components.translator import translate_text
from MultiURLSummarizer.utils.common import is_valid_url, clean_text

def process_urls(urls, target_language):
    summaries = []
    for url in urls.split('\n'):
        url = url.strip()
        if is_valid_url(url):
            summary = summarize_url(url)
            if target_language != "Original":
                summary = translate_text(summary, target_language)
            summaries.append(clean_text(summary))
        else:
            summaries.append(f"Invalid URL: {url}")
    return "\n\n".join(summaries)

def gradio_interface(urls, target_language):
    return process_urls(urls, target_language)

iface = gr.Interface(
    fn=gradio_interface,
    inputs=[
        gr.Textbox(lines=5, label="URLs (one per line)"),
        gr.Dropdown(["Original", "English", "Turkish"], label="Target Language", value="Original")
    ],
    outputs=gr.Textbox(label="In a Nutshell..."),
    title="Newsletter Creator",
    description="Enter multiple URLs to get summarized content with optional translation."
)

if __name__ == "__main__":
    iface.launch(share=True)

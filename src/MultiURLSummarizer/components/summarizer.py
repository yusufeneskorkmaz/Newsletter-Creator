from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.chat_models import ChatOllama
from langchain_community.document_loaders import WebBaseLoader

def load_document(url):
    """Load document from the specified URL."""
    loader = WebBaseLoader(url)
    return loader.load()

def setup_summarization_chain():
    """Setup the summarization chain with a prompt template and ChatOllama."""
    prompt_template = PromptTemplate(
        template="""As a professional summarizer, create a concise summary of the provided text, adhering to these guidelines:
            1. Craft a summary that is detailed yet concise, focusing on the main points.
            2. Incorporate key ideas and essential information, eliminating unnecessary details.
            3. Rely strictly on the provided text, without including external information.
            4. Format the summary as a short paragraph with a title.
            5. Keep the summary to about 2-3 sentences.
        "{text}"
        CONCISE SUMMARY:""",
        input_variables=["text"],
    )
    llm = ChatOllama(model="llama3:instruct", base_url="http://127.0.0.1:11434")
    llm_chain = LLMChain(llm=llm, prompt=prompt_template)
    return llm_chain

def summarize_url(url):
    """Summarize the content of a given URL."""
    docs = load_document(url)
    llm_chain = setup_summarization_chain()
    summary = llm_chain.run(docs)
    return summary
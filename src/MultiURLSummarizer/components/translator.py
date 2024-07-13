from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.chat_models import ChatOllama

def setup_translator_chain(target_language):
    """Setup the translation chain with a prompt template and ChatOllama."""
    prompt_template = PromptTemplate(
        template="""As a professional translator, provide an accurate and coherent translation of the provided text into {language}, ensuring that the translation is faithful to the original text.
        "{text}"
        TRANSLATION:""",
        input_variables=["text", "language"],
    )
    llm = ChatOllama(model="llama3:instruct", base_url="http://127.0.0.1:11434")
    llm_chain = LLMChain(llm=llm, prompt=prompt_template)
    return llm_chain

def translate_text(text, target_language):
    """Translate the given text to the target language."""
    llm_chain = setup_translator_chain(target_language)
    translated_text = llm_chain.run({"text": text, "language": target_language})
    return translated_text
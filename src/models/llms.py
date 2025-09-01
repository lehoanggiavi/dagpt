from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq

def load_llm(model_name):
    """
    Load Large Language Model
    """
    if model_name == 'gpt-3.5-turbo':
        return ChatOpenAI(
            model=model_name,
            temperature=0.0,
            max_tokens=1000
        )
    elif model_name=='gpt-4':
        return ChatOpenAI(
            model=model_name,
            temperature=0.0,
            max_tokens=1000
        )
    elif model_name=='llama-3.3-70b-versatile':
        return ChatGroq(
            model=model_name,
            temperature=0.0,
            max_tokens=1000
        )
    else:
        raise ValueError(
            "Unkown model.\
                Please choose from ['gpt-3.5-turbo', 'gpt-4', 'llama-3.3-70b-versatile' ...]"
        )
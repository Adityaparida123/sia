from llm.chatbot import ask_chatbot


def generate_insight(data):
    prompt = f"""
    Analyze this supply chain data and give smart business insight:

    {data}

    Keep answer short and useful.
    """

    return ask_chatbot(prompt)

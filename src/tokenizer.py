import tiktoken


def tiktoken_length(text: str) -> int:
    """Get the tokenizer corresponding to a specific model in the OpenAI API."""

    _tiktoken: tiktoken = tiktoken.get_encoding("cl100k_base")
    tokens: int = len(_tiktoken.encode(text=text, disallowed_special=()))

    return tokens

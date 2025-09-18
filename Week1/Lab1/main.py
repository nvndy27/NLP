
from src.core.dataset_loaders import load_raw_text_data
from src.preprocessing.simple_tokenizer import SimpleTokenizer
from src.preprocessing.regex_tokenizer import RegexTokenizer

if __name__ == "__main__":
    # Tạo tokenizer
    simple_tokenizer = SimpleTokenizer()
    regex_tokenizer = RegexTokenizer()


    dataset_path = "C:\\Users\\Admin\\Documents\\NLP\\UD_English-EWT\\UD_English-EWT\\en_ewt-ud-dev.txt"
    raw_text = load_raw_text_data(dataset_path)

    sample_text = raw_text[:500]

    print("\n--- Tokenizing Sample Text from UD_English-EWT ---")
    print(f"Original Sample: {sample_text[:100]}...")  # chỉ in 100 ký tự đầu tiên


    simple_tokens = simple_tokenizer.tokenize(sample_text)
    print(f"SimpleTokenizer Output (first 20 tokens): {simple_tokens[:20]}")


    regex_tokens = regex_tokenizer.tokenize(sample_text)
    print(f"RegexTokenizer Output (first 20 tokens): {regex_tokens[:20]}")

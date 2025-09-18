import re 
from src.core.interfaces import Tokenizer
from typing import List

class SimpleTokenizer(Tokenizer):
 def tokenize(self, text: str) -> List[str]:
  tokens = re.findall(r"\w+|[.,?!]", text)
        
  return tokens
 
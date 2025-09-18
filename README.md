# NLP
Nộp bài tập thực hành NLP kì 1 2025 
Báo cáo Tuần 1 : 

Lab1
Mô tả công việc
  Task 1:
  Cài đặt Tokenizer interface trong src/core/interfaces.py.
  Cài đặt SimpleTokenizer trong src/preprocessing/simple_tokenizer.py:
  Chuyển text thành chữ thường.
  Tách từ dựa trên khoảng trắng.
  Xử lý dấu câu (. , ? !) tách riêng khỏi token.

  Task 2 (Bonus):
  Cài đặt RegexTokenizer trong src/preprocessing/regex_tokenizer.py dùng regex \w+|[^\w\s].
  Hỗ trợ tách token chính xác hơn khi có nhiều dấu câu liền nhau (..., 's, v.v.).

  Task 3:
  Dùng load_raw_text_data để load dataset UD_English-EWT.
  Thử nghiệm tokenization trên text thực tế (500 ký tự đầu).
  So sánh kết quả giữa SimpleTokenizer và RegexTokenizer.

Kết quả lab1:
  --- Tokenizing Sample Text from UD_English-EWT ---
  Original Sample: From the AP comes this story : 

  President Bush on Tuesday nominated two individuals to replace reti...
  SimpleTokenizer Output (first 20 tokens): ['From', 'the', 'AP', 'comes', 'this', 'story', 'President', 'Bush', 'on', 'Tuesday', 'nominated', 'two', 'individuals', 'to', 'replace', 'retiring', 'jurists', 'on', 'federal', 'courts']
  RegexTokenizer Output (first 20 tokens): ['From', 'the', 'AP', 'comes', 'this', 'story', ':', 'President', 'Bush', 'on', 'Tuesday', 'nominated', 'two', 'individuals', 'to', 'replace', 'retiring', 'jurists', 'on', 'federal']

Giải Thích kết quả: 
  Trong Lab 1, SimpleTokenizer chỉ tách theo khoảng trắng nên nhiều khi dấu câu bị dính vào từ, làm vocabulary “bẩn” hơn. RegexTokenizer dùng biểu thức chính quy nên tách rõ từ và dấu câu, kết quả gọn và chính xác hơn. Vì vậy, khi áp dụng trên dữ liệu thực tế (UD_English-EWT), RegexTokenizer cho ra tokens sạch, còn SimpleTokenizer có thể bỏ sót hoặc dính dấu câu.

Lab2 
Mô tả công việc:
  Cài đặt CountVectorizer trong src/representations/count_vectorizer.py.
  Các bước chính:
  fit(corpus): xây dựng vocabulary từ corpus.
  transform(corpus): chuyển văn bản thành ma trận đếm từ (document-term matrix).
  fit_transform(corpus): kết hợp hai bước trên.
  Kết hợp với SimpleTokenizer hoặc RegexTokenizer để xử lý văn bản.  

Kết quả lab2: 
  Vocabulary: {'.': 0, 'AI': 1, 'I': 2, 'NLP': 3, 'a': 4, 'is': 5, 'love': 6, 'of': 7, 'programming': 8, 'subfield': 9}
  Document-term matrix:
  [1, 0, 1, 1, 0, 0, 1, 0, 0, 0]
  [1, 0, 1, 0, 0, 0, 1, 0, 1, 0]
  [1, 1, 0, 1, 1, 1, 0, 1, 0, 1]

Giải thích kết quả: 
  Trong Lab 2, em đã cài đặt CountVectorizer để học vocabulary từ corpus và biến đổi văn bản thành ma trận số. Kết quả cho thấy mỗi câu được biểu diễn bằng vector đếm số lần xuất hiện của từ trong vocabulary. Ví dụ, câu "I love NLP." được ánh xạ thành vector có các vị trí tương ứng với "I", "love", "NLP", "." với giá trị bằng 1.











  

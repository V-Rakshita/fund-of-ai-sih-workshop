import PyPDF2
from collections import Counter
import re

def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""

    for page in reader.pages:
        text += page.extract_text()

    return text


def summarize_text(text):

    sentences = text.split(".")
    summary = sentences[:5]

    return ".".join(summary)


def extract_keywords(text):

    words = re.findall(r'\w+', text.lower())

    stopwords = ["the","is","in","and","to","of","a"]

    words = [w for w in words if w not in stopwords]

    freq = Counter(words)

    return [word for word, count in freq.most_common(10)]
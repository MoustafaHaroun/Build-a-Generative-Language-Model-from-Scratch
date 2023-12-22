from string import punctuation
from collections import Counter
from collections import defaultdict
import json

userInput = input("Enter a sentence: ")

json_file_path = "CommentsTestData.json"
with open(json_file_path, 'r') as file:
    post_comments_with_labels = json.load(file)


class NaiveBayesClassifier:
    def __init__(self, samples):
        self.mapping = {"pos": [], "neg": []}
        self.neg_mapping = defaultdict(lambda: 0)
        self.sample_count = len(samples)
        for text, label in samples:
            self.mapping[label] += self.tokenize(text)
        self.pos_counter = Counter(self.mapping["pos"])
        self.neg_counter = Counter(self.mapping["neg"])

    @staticmethod
    def tokenize(text):
        return (
            text.lower().translate(str.maketrans("", "", punctuation + "1234567890"))
            .replace("\n", " ")
            .split(" ")
        )

    def classify(self, text):
        tokens = self.tokenize(text)
        pos = []
        neg = []

        for token in tokens:
            pos.append(self.pos_counter[token] / self.sample_count)
            neg.append(self.neg_counter[token] / self.sample_count)

        # rerturn "neg", "pos" or "nutral"
        total_Negative = sum(neg)
        total_Positive = sum(pos)

        if total_Negative == total_Positive:
            return "neutral"
        elif total_Negative > total_Positive:
            return "neg"
        else:
            return "pos"


cl = NaiveBayesClassifier(post_comments_with_labels)


def get_sentiment(text):
    cl = NaiveBayesClassifier(post_comments_with_labels)
    return cl.classify(text)

result = get_sentiment(userInput)
print(result)

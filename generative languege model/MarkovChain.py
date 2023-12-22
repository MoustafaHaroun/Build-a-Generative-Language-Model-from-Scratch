import random
from string import punctuation
from collections import defaultdict
class MarkovChain:
    def __init__(self):
        self.graph = defaultdict(list)

    def _tokenize(self, text):
        return (
            text.translate(str.maketrans('', '', punctuation + "1234567890")),
            text.translate(str.maketrans('', ''))
            .replace("\n", " ")
            .split(" ")
        )

    def train(self, text):
        tokens = self._tokenize(text)
        for i, token in enumerate(tokens[1]):
            if (len(tokens[1]) - 1) == i:
                break
            self.graph[tokens[1][i]].append(tokens[1][i + 1])

    def generate(self, prompt, length=10):
        current = list(self._tokenize(prompt)[1])[-1]
        output = prompt
        for i in range(length):
            options = self.graph.get(current, [])
            if not options:
                continue
            current_option = random.choice(options)
            output += " " + current_option
            current = current_option
        return output

# Example usage:
file = open("SongData.txt", "r")
text_data = file.read()
file.close()

markov_chain = MarkovChain()
markov_chain.train(text_data)
generated_text = markov_chain.generate("He was", length=20)
print(generated_text)

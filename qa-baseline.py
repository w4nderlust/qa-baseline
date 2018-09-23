import argparse
import math
from pws import Bing

parser = argparse.ArgumentParser()
parser.add_argument("-q", "--question", help="the question you want to ask", required=True)
parser.add_argument("-a", "--answers", help="the candidate answers", nargs="+", required=True)
parser.add_argument("-r", "--results", help="The number of search engine results to consider", type=int, default=30)
parser.add_argument("-l", "--lang", help="The language of the question", default="en")
args = parser.parse_args()

#print(args)
search_results = Bing.search(args.question.lower(), args.results, 0, country_code=args.lang)
#print(search_results)

result_strings = [" ".join([result['link_text'], result["link_info"]]).lower() for result in search_results['results']]

scores = []
for answer in args.answers:
    answer = answer.lower()
    score = 0
    for rank, result_string in enumerate(result_strings):
        if result_string:
            count = result_string.count(answer)
            score += count / (rank + 1)
    scores.append(score)

_scores = [math.exp(s) for s in scores]
sum__scores = sum(_scores)
probabilities = [_score / sum__scores for _score in _scores]

suggestions = {}
for i, answer in enumerate(args.answers):
    suggestions[answer] = {"probablity": probabilities[i], "raw_score": scores[i]}
    print("{} - probablity: {:.4f}  raw score: {:.4f}".format(answer, probabilities[i], scores[i]))


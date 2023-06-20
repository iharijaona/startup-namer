from typing import Union
import time
import random
from .fixes import featurize
from .normalizer import normalize
from .validation import vilidate_availabilty
from .scorer import score

def namer(keywords: Union[str, list[str]], seed=random.random()):
  
  random.seed(seed)

  if isinstance(keywords, str):
    keywords = keywords.split()

  candidates = featurize(keywords)

  candidates = map(lambda name: dict(name=normalize(name), score=score(name)), candidates)

  candidates = vilidate_availabilty(list(candidates))

  # Sort by score
  candidates = sorted(candidates, key=lambda n: -1 * n['score'])

  candidates = filter(lambda candidate: candidate['available'] , candidates)

  # Reduce to just words
  candidates = map(lambda item: item['name'], candidates)

  return list(candidates)

  

if __name__ == '__main__':
  names = namer("software development engineering cloud web application information technology digital reliable mature")

  with open("startup_names.csv", "w") as out:
    out.writelines("\n".join(names))

  for n in names:
    print(n)
    time.sleep(1)
from random import random
from .fixes import ACTUAL_SUFFIXES
from .normalizer import normalize
import syllables 

def score(word: str):
  mark = 0
  mark += syllables_score(word)
  mark += suffix_score(word)
  mark += length_score(word)
  mark += random() * 0.4
  return mark


def syllables_score(word: str): 
  """Scores a word based on syllables"""
  syllables_count = syllables.estimate(word)
  if syllables_count == 2: return 6.1
  elif syllables_count == 3: return 6
  elif syllables_count > 4: return 2
  return 4

def suffix_score(word: str):
  """Scores a word based on suffixes"""
  is_actual = any([word[-len(suffix):] == suffix for suffix in ACTUAL_SUFFIXES])
  return  -1.5 if is_actual else 0

def length_score(word: str):
  """Scores a word based on length"""
  if (len(normalize(word)) < 9): return 0.1
  return 0


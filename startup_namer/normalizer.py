import re

def normalize (name: str) -> str:
  name = re.sub(r'e i', 'i', name) # time ible -> timible
  name = re.sub(r'y i', 'i', name) # technology ible -> technologible
  name = re.sub(r'th t', 'i', name) # health tion -> healthion
  name = re.sub(r'(.) (.)', '\\1\\2', name) # live event -> livevent
  name = name.capitalize()
  return name


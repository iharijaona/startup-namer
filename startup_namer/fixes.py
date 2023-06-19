# https://dailyblogtips.com/200-prefixes-and-suffixes-for-domain-names/

PREFIXES = [
  '1st',
  'active',
  'arc',
  'auto',
  'app',
  'avi', # aviato
  'at', # atsky
  'base', # basecamp
  'big', 
  'co',
  'con',
  'core',
  'clear', # clearleft
  'daily',
  'e',
  'en', # envato
  'echo', # echoplex
  'even',
  'ever', # note
  'extra',
  'fair', # fairlight
  'first', # first info
  'fast',
  'go', # gopro
  'high', # highrise
  'hyper',
  'in',
  'inter',
  'iso',
  'info',
  'ideo',
  'jump',
  'live', # livejournal
  'light',
  'make',
  'mass', # massdrop
  'meta', # metalab
  'matter', # mattermost
  'multi',
  'new',
  'neo',
  'novo', # renew
  'nova', # new
  'omni', # omniture
  'on',
  'one', # onenote
  'open',
  'over', # overwatch
  'out',
  're',
  'real',
  'peak',
  'pure',
  'plury',
  'plural',
  'shift',
  'silver', # silverstripe
  'solid',
  'super',
  'hyper',
  'spark',
  'start',
  'smart', # smart compil
  'true', # truecrypt
  'the',
  'tech',
  'quick',
  'great',
  'up', # upwork
  'ultra',
  'vivo' # alive
  'vibe', # vibewrite
  'we', #wedoit
  'world',
  # Professional/Mastery
  'expert',
  'pro',
  'prime',
  'intelli'
  # Technology/Cyber
  'tech',
  'digital',
  # Sleek/Swift
  'swift',
  'quick'
]

WORD_SUFFIXES = [
  'arc', # luminarc
  'atlas',
  'base', # crunchbase
  'bay', # ebay
  'boost',
  'capsule', # time capsule
  'case',
  'center',
  'cast', # shoutcast
  'click',
  'dash',
  'deck',
  'dock', # flowdock, stardock, apidock
  'dot', # slashdot
  'drop', # massdrop
  'engine',
  'engineering',
  'flow', # eventflow
  'glow', # afterglow
  'grid', # sendgrid
  'gram', # instagram
  'graph',
  'hub', # github
  'focus',
  'factory',
  'insight',
  'info'
  'kit',
  'lab', # gitlab
  'link',
  'level',
  'layer', # softlayer
  'light', # fairlight
  'line',
  'logic', # authlogic
  'load',
  'loop',
  'ment',
  'method',
  'mode',
  'mark', # zipmark
  'mind',
  'mindz',
  'ness',
  'now',
  'pass',
  'port',
  'post',
  'press', # wordpress
  'prime', # pushprime
  'push',
  'rise', # highrise
  'response',
  'scape', # netscape
  'scale',
  'scan', # skyscanner
  'scout',
  'sense',
  'set',
  'shift', # redshift, infoshift
  'ship', # codeship
  'sight',
  'side',
  'signal', # appsignal
  'snap',
  'scope', # periscope
  'space', # squarespace
  'span',
  'spark',
  'spot', # blogspot
  'start',
  'soft',
  'storm', # packetstorm
  'stripe', # silverstripe
  'sync',
  'tap', # healthtap
  'tilt',
  'ture', # omniture
  'type',
  'view',
  'verge', # converge
  'vibe',
  'ware',
  'yard', # engineyard
  'up', # squareup
  'tools',
  'system',
  'systemz',
  'tech',
  'techz',
  'focus',
  'zone',
  'world'
]

# Actual suffixes (not just words); ranks lower
ACTUAL_SUFFIXES = [
  'ary', # apiary
  'able', # mashable
  'ance',
  'er',
  'eon', # vaporeon :p
  'ent',
  'ery', # machinery, digitalery
  'ible',
  'ice',
  'ite', # graphite
  'ful',
  'gent',
  'tion',
  'sion',
  'ric',
  'tic'
]

SUFFIXES = set(WORD_SUFFIXES + ACTUAL_SUFFIXES + PREFIXES)

PREFIXES = set(PREFIXES + WORD_SUFFIXES)

def featurize(keywords: list[str]):
  if len(keywords):
    return permutate_fixes(PREFIXES, keywords) + permutate_fixes(keywords, SUFFIXES)
  else:
    return permutate_fixes(PREFIXES, SUFFIXES)

def permutate_fixes(prefixes: list[str], suffixes: list[str]):
  return sum([[f'{pf} {sf}' for pf in prefixes if pf != sf] for sf in suffixes], [])


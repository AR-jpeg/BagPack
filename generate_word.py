"""Get random words."""

from requests import get
import json

content = get("https://raw.githubusercontent.com/sindresorhus/mnemonic-words/master/words.json").content

words = json.loads(content)
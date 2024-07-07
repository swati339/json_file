import json

info = {
  "name": "Aesha",
  "is_dog": False,
  "hobbies": ["reading", "dancing", "hiking",],
  "age": 45,
  "address": {
    "work": None,
    "home": ("Kathmandu", "Nepal",),
  },
  "friends": [
    {
      "name": "abc",
      "hobbies": ["eating", "hiking", "reading",],
    },
    {
      "name": "def",
      "hobbies": ["running", "reading",],
    },
  ],
}

with open("hello.json", mode="w", encoding="utf-8") as write_file:
    json.dump(info, write_file, indent =4)
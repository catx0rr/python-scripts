#!/usr/bin/python3

import json

string_of_jason_data = {"name": "Zophie", "isCat": true, "miceCaught": 0, "felineIQ": null}


json_as_python_value = json.loads(string_of_jason_data)

print(json_as_python_value)

pythonValue = json.dumps(string_of_jason_data)

print(pythonValue)

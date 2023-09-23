import re

text = """
 Hello my Name is Max and my phone number is +41 79 204 51 69. It used to be +41 79 204 51 68 but now it is +41 79 204 51 69.
"""

phone_number = "+41 79 204 51 69"
pattern = r"\+[\d\' ']+"

compiled_regex = re.compile(pattern)

match_iter = compiled_regex.finditer(text, re.IGNORECASE)

for m in match_iter:
	print(f'Found match "{m.group(0)}" ranging from index {m.start()} - {m.end()}')
import re

text = """
Foo Mustermann
Phone Number: +41 81 410 08 49
foo.mustermann@gmail.com

Bar Mustermann
+41 81 410 08 21
bar.mustermann@gmail.com

Baz Mustermann
Phone Number is +41 81 410 08 42
baz.mustermann@gmail.com
"""


pattern = r"\+[\d\' ']+"

compiled_regex = re.compile(pattern)

match_iter = compiled_regex.finditer(text, re.IGNORECASE)

for m in match_iter:
	print(f'Found match "{m.group(0)}" ranging from index {m.start()} - {m.end()}')

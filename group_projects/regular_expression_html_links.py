import re

html_content = """
<!DOCTYPE html>
<html>
    <head>
        <title>Example</title>
    </head>
    <body>
    	<a href="http://www.google.ch">google.ch</a>
    	<a target="_blank" href="http://www.google.ch">google.de</a>
        <p>This is an example of a simple HTML page with one paragraph.</p>
    </body>
</html>
"""

link_pattern = r"href=\"[\w+]+"

match_iter = re.finditer(link_pattern, html_content, re.IGNORECASE)

for m in match_iter:
	print(f'Found match "{m.group(0)}" ranging from index {m.start()} - {m.end()}')
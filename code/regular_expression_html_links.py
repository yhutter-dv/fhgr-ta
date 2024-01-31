import re

html_content = """
<!DOCTYPE html>
<html>
    <head>
        <title>HTML with Links</title>
    </head>
    <body>
    	<a href="http://www.google.ch">google.ch</a>
    	<a target="_blank" href="http://www.realpython.org">realpython.org</a>
        <p>This is a paragraph with a <a href="http://www.python.org">Python Link</a></p>
    </body>
</html>
"""

# Capture the actual link inside a group.
link_pattern = r"href=\"([A-Za-z:\/\.]+)"

match_iter = re.finditer(link_pattern, html_content, re.IGNORECASE)

for m in match_iter:
	print(f'Found match "{m.group(1)}" ranging from index {m.start()} - {m.end()}')

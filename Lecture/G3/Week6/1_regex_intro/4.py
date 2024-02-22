# meta characters
# * + . ? ^ $ { } [ ] ( ) |
# | - either or

import re

word = "roses are red, violets are blue"

print(re.findall("roses|violets", word))

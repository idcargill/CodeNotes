import sys
from mod1 import do_stuff
from textwrap import dedent

print(sys.version)

# printdir(pd))

do_stuff()

multi_line = '''
Big long text
with more stuff
and junk.
'''

new_multi_line = dedent(multi_line)


print(multi_line)
print(new_multi_line)
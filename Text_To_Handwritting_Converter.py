# $ pip install pywhatkit

import pywhatkit as pwk

txt = """~~~~~~~~~~~~Python~~~~~~~~~~~\n
Python is a popular programming language. It was created by Guido van Rossum, and released in 1991.

It is used for:

web development (server-side),
software development,
mathematics,
system scripting."""

pwk.text_to_handwriting(txt, "demo.png", [0, 0, 138])
print("Program End!")
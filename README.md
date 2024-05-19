# PyKozo

PyKozo is a Python library that allows for complete web development using Python scripts. Currently, it only includes the complete HTML module, but other modules will be added in the future.

Version 0.0.21

Documentation coming soon...

# Getting started

**Installation:**

Run the following command in your command prompt / shell:

```
pip install -U PyKozo
```
**Your first compilation**

You need to instantiate `pykozo.html()` into a variable and preferably within a function.

```python
from pykozo import html

def my_page():
    page = html()  # Instantiate the class
    # Now, to create HTML with an h1, we'll do the following
    page.h1('Hello World')  # The first argument is the content inside the h1
    # And now, to compile our HTML, we'll do
    return page.compile()

# Now if we print the function...
print(my_page())
```

We'll get this:
```
<h1>Hello World</h1>
```


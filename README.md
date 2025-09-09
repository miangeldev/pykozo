# PyKozo
<img src="https://github.com/miangeldev/pykozo/assets/170264335/e9a08425-93b6-4020-9dc4-d7526b62b151" width="200" height="200" />

PyKozo is a Python library that allows for complete web development using Python scripts. Currently, it only includes the complete HTML module, but other modules will be added in the future.

Version 0.0.4

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

**Attributes**

You can add all kinds of attributes, such as style or class. Here's an example:

```python
pykozo.html.p('Hi', style='color: #000080;', className='container')
# After the first attribute, you can pass parameters that go into the HTML
```

**About self-closing tags**

In HTML, there are tags that only close once, like `<input>`. In this case, for these tags, the first argument is no longer the content but starts as the first attribute. An example is:

```python
pykozo.html.input(type="submit", value="Submit")
```

**Components and sections**

PyKozo recommends and even "forces" you to work with components and sections. How do you create a component? Here's how:

```python
from pykozo import html

def my_button_component(text):
    button = html()
    button.button(text, type="button")
    return button.compile()

def main_page():
    page = html()
    buttons = ""
    for i in range(5):
        button = my_button_component(f"Button {i}")
        buttons += button
    page.div(buttons)
    return page.compile()

print(main_page())
```
and we will receive this:
```
<div><button type="button">Button 0</button><button type="button">Button 1</button><button type="button">Button 2</button><button type="button">Button 3</button><button type="button">Button 4</button></div>
```
And an example for a section:
```python
from pykozo import html

def python_frameworks_list():
    frameworks = ["Flask", "FastAPI", "Django", "etc"]
    section = html()
    for framework in frameworks:
        section.li(framework)
    return section.compile()

def main_page():
    page = html()
    page.ul(python_frameworks_list())
    return page.compile()

print(main_page())
```
and it prints this:
```
<ul><li>Flask</li><li>FastAPI</li><li>Django</li><li>etc</li></ul>
```

**Implementation with Flask**

PyKozo can integrate with most Python frameworks, one of which is Flask. Here is a very basic example of how to implement it:

```python
from pykozo import html
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    page = html()
    page.h1("Hi everyone")
    page.h2("My first Page with PyKozo and Flask")
    page.img(src='https://source.unsplash.com/random', style="width:400px;")
    return page.compile()

if __name__ == "__main__":
    app.run()
```

You can add backend logic, and the code will also display a random image from an API.

![Captura de pantalla_20240519_192004](https://github.com/miangeldev/pykozo/assets/170264335/e96a1618-5458-4b43-b81e-5fd63da763c4)

# CSS Support!
```python
from pykozo import CSS

class Styles1(CSS):
    @CSS.style(name="red-text", type="class")
    def red_text():
        color = "red"
        font_size = "20px"

    @CSS.style(name="blue-bg", type="id")
    def blue_bg():
        background_color = "blue"
        padding = "10px"
    
    @CSS.style(name="p", type="tag")
    def paragraph_style():
        line_height = "1.5"
        text_align = "justify"

class Styles2(CSS):
    @CSS.style(name="green-border", type="class")
    def green_border():
        border = "2px solid green"
        margin = "5px"

    @CSS.style(name="yellow-text", type="id")
    def yellow_text():
        color = "yellow"
        font_weight = "bold"

print("Compiled Styles1 CSS:")
print(Styles1.compile())
print("Compiled Styles2 CSS:")
print(Styles2.compile())
```
We'll get this:
```css
Compiled Styles1 CSS:
.red-text {
  color: red;
  font-size: 20px;
}
#blue-bg {
  background-color: blue;
  padding: 10px;
}
p {
  line-height: 1.5;
  text-align: justify;
}

Compiled Styles2 CSS:
.green-border {
  border: 2px solid green;
  margin: 5px;
}
#yellow-text {
  color: yellow;
  font-weight: bold;
}
```

# Extra Functions

**Add custom tags**

If you want to add a tag that is not registered, you can use the following function:

```python
pykozo.html.add_tag(_tag='tag name', _content='only if the tag is not a self closing tag', _closing_tag=True/False)
```

An example of usage would be for PyScript.

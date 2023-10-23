def build_xml_element(tag, content, **attributes):
    # Start building the opening tag with attributes
    element = f"<{tag}"

    for key, value in attributes.items():
        element += f' {key}="{value}"'

    element += ">"

    element += content

    element += f"</{tag}>"

    return element

xml_element = build_xml_element("a", "Hello there", href="http://python.org", _class="my-link", id="someid")
print(xml_element)
# <a href="http://python.org" _class="my-link" id="someid">Hello there</a>
class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    def to_html(self):
        raise NotImplementedError
    def props_to_html(self):
        html = ""
        if self.props is None:
            return html
        for k ,v in self.props.items():
            html += f" {k}={v}"
        return html
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props_to_html()})"
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__()
        self.tag = tag
        self.value = value
        self.props = props
    def to_html(self):
        if self.value is None:
            raise ValueError("No value string argument was listed")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.props_to_html()})"
    

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__()
        self.tag = tag
        self.children = children
        self.props = props
    def to_html(self):
        if not self.tag:
            raise ValueError("HTML tag was not provided")
        if not self.children:
            raise ValueError("No children argument was provided")
        children_str = ""
        for child in self.children:
            children_str += child.to_html()
        return f"<{self.tag}>{self.props_to_html()}{children_str}</{self.tag}>"
    
from pykozo.self_closing_tags import self_closing_tags_list

class Tag:
    def __init__(self, name, **attrs):
        self.name = name
        self.attrs = attrs
        self.children = []
        self.content = []
        self.parent = None

    def compile(self):
        # Procesa atributos especiales
        processed_attrs = {}
        for k, v in self.attrs.items():
            if k == "class_":
                processed_attrs["class"] = v
            elif k == "id_":
                processed_attrs["id"] = v
            elif not k.startswith("_"):
                processed_attrs[k] = v
        
        attrs_str = " ".join([f'{k}="{v}"' for k, v in processed_attrs.items()])
        html = f"<{self.name}{' ' + attrs_str if attrs_str else ''}>"
        
        if self.name in self_closing_tags_list:
            return html + ">"
        
        html += "".join(self.content + [child.compile() for child in self.children])
        html += f"</{self.name}>"
        return html

class Html:
    """Generador de HTML con gestión automática de contexto."""
    def __init__(self):
        self.root = None
        self.current_parent = None
        self.parent_stack = []

    def __getattr__(self, name):
        """Crea dinámicamente etiquetas."""
        def tag_creator(**attrs):
            tag = Tag(name, **attrs)
            if self.current_parent:
                self.current_parent << tag  # Añade al padre actual
            elif not self.root and name == "html":
                self.root = tag  # Establece la raíz
            return tag
        return tag_creator

    def __enter__(self):
        """Inicia el contexto para una etiqueta."""
        return self

    def __exit__(self, *args):
        """Finaliza el contexto."""
        if self.parent_stack:
            self.current_parent = self.parent_stack.pop()

    def __lshift__(self, other):
        """Añade etiquetas al documento."""
        if isinstance(other, Tag):
            if not self.root:
                self.root = other
            else:
                self.root << other
        return self

    def compile(self):
        """Genera el HTML completo."""
        if not self.root:
            raise ValueError("No hay contenido para compilar")
        return f"<!DOCTYPE html>{self.root.compile()}"
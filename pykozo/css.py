import inspect
import textwrap

class CSS:
    @staticmethod
    def style(name: str, type: str = "class"):
        def decorator(func):
            def wrapper(cls):
                # Extraer el código fuente de la función
                source = inspect.getsource(func)
                
                # Obtener las líneas del código fuente
                lines = source.splitlines()
                
                # Encontrar el inicio del cuerpo de la función
                # Buscar la línea que contiene "def"
                def_index = -1
                for i, line in enumerate(lines):
                    if line.strip().startswith("def "):
                        def_index = i
                        break
                
                if def_index == -1:
                    return func
                
                # Obtener solo las líneas del cuerpo de la función
                # (excluyendo la línea "def" y cualquier decorador)
                body_lines = []
                for i in range(def_index + 1, len(lines)):
                    # Quitar la indentación del cuerpo
                    body_lines.append(lines[i])
                
                # Unir las líneas y quitar la indentación común
                body = "\n".join(body_lines)
                body = textwrap.dedent(body)
                
                # Ejecutar SOLO el cuerpo para obtener las variables
                local_vars = {}
                exec(body, {}, local_vars)
                
                # Filtrar __builtins__ y cosas raras
                clean_vars = {
                    k: v for k, v in local_vars.items()
                    if not k.startswith("__")
                }
                # Volver _ a -
                clean_vars = {
                    k.replace("_", "-"): v for k, v in clean_vars.items()
                }
                
                if not hasattr(cls, "__styles__"):
                    cls.__styles__ = []
                    
                cls.__styles__.append({
                    "name": name,
                    "type": type,
                    "vars": clean_vars,
                })
                return func
            
            func._style_wrapper = wrapper
            return func
        
        return decorator
    
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        for _, attr_value in list(cls.__dict__.items()):
            if hasattr(attr_value, "_style_wrapper"):
                attr_value._style_wrapper(cls)
    
    @classmethod
    def compile(cls):
        if not hasattr(cls, "__styles__"):
            return ""
        css = ""
        for style in cls.__styles__:
            match style["type"]:
                case "class":
                    selector = f".{style['name']}"
                case "id":
                    selector = f"#{style['name']}"
                case "tag":
                    selector = style['name']
                case _:
                    raise ValueError(f"Type of css: {style['type']}")
            css += selector + " {\n"
            for var, value in style["vars"].items():
                css += f"  {var}: {value};\n"
            css += "}\n"
        return css

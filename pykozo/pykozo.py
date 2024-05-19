class html:
    def __init__(self) -> None:
        self.pre_compiled = []
        return None
    def add_tag(self,**kwargs) -> None:
        if "_tag" in kwargs:
            self.pre_compiled.append(kwargs)
        else:
            raise Exception("Not a valid tag")
        return None
    
    def html_tag(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="html"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def head(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="head"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def title(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="title"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)
    
    def base(self,**kwargs):
        kwargs["_content"]=""
        kwargs["_tag"]="base"
        kwargs["_closing_tag"]=True
        self.add_tag(**kwargs)

    def link(self,**kwargs):
        kwargs["_content"]=""
        kwargs["_tag"]="link"
        kwargs["_closing_tag"]=True
        self.add_tag(**kwargs)

    def meta(self,**kwargs):
        kwargs["_content"]=""
        kwargs["_tag"]="meta"
        kwargs["_closing_tag"]=True
        self.add_tag(**kwargs)
    
    def style(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="style"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def script(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="script"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)
    
    def noscript(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="noscript"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def body(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="body"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def article(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="article"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def section(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="section"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def nav(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="nav"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def aside(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="aside"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def h1(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="h1"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def h2(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="h2"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def h3(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="h3"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def h4(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="h4"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def h5(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="h5"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def h6(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="h6"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)
    
    def header(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="header"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def footer(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="footer"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def addres(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="addres"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def main(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="main"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def p(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="p"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def hr(self,**kwargs):
        kwargs["_content"]=""
        kwargs["_tag"]="hr"
        kwargs["_closing_tag"]=True
        self.add_tag(**kwargs)

    def pre(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="pre"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def blockquote(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="blockquote"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def ol(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="ol"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def ul(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="ul"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def li(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="li"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def dl(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="dl"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)
    
    def dt(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="dt"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def dd(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="dd"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def figure(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="figure"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def figcaption(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="figcaption"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def div(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="div"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def a(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="a"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def em(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="em"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def strong(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="strong"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)
        
    def small(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="small"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def s(self,**kwargs):
        kwargs["_content"]=""
        kwargs["_tag"]="s"
        kwargs["_closing_tag"]=True
        self.add_tag(**kwargs)

    def cite(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="cite"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def q(self,**kwargs):
        kwargs["_content"]=""
        kwargs["_tag"]="q"
        kwargs["_closing_tag"]=True
        self.add_tag(**kwargs)

    def dfn(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="dfn"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def abbr(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="abbr"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def data(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="data"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def time(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="time"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def code(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="code"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def var(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="var"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def samp(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="samp"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def kbd(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="kbd"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def sub(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="sub"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def sup(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="sup"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def i(self,**kwargs):
        kwargs["_content"]=""
        kwargs["_tag"]="i"
        kwargs["_closing_tag"]=True
        self.add_tag(**kwargs)

    def b(self,**kwargs):
        kwargs["_content"]=""
        kwargs["_tag"]="b"
        kwargs["_closing_tag"]=True
        self.add_tag(**kwargs)

    def u(self,**kwargs):
        kwargs["_content"]=""
        kwargs["_tag"]="u"
        kwargs["_closing_tag"]=True
        self.add_tag(**kwargs)

    def mark(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="mark"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def ruby(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="ruby"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def rt(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="rt"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def rp(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="rp"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def bdi(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="bdi"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def bdo(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="bdo"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def span(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="span"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def br(self,**kwargs):
        kwargs["_content"]=""
        kwargs["_tag"]="br"
        kwargs["_closing_tag"]=True
        self.add_tag(**kwargs)

    def wbr(self,**kwargs):
        kwargs["_content"]=""
        kwargs["_tag"]="wbr"
        kwargs["_closing_tag"]=True
        self.add_tag(**kwargs)

    def ins(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="ins"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def del_tag(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="del"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def picture(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="picture"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def source(self,**kwargs):
        kwargs["_content"]=""
        kwargs["_tag"]="source"
        kwargs["_closing_tag"]=True
        self.add_tag(**kwargs)

    def img(self,**kwargs):
        kwargs["_content"]=""
        kwargs["_tag"]="img"
        kwargs["_closing_tag"]=True
        self.add_tag(**kwargs)

    def iframe(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="iframe"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def embed(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="embed"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def object(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="object"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def param(self,**kwargs):
        kwargs["_content"]=""
        kwargs["_tag"]="param"
        kwargs["_closing_tag"]=True
        self.add_tag(**kwargs)

    def video(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="video"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def audio(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="audio"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def track(self,**kwargs):
        kwargs["_content"]=""
        kwargs["_tag"]="track"
        kwargs["_closing_tag"]=True
        self.add_tag(**kwargs)

    def map(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="map"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def area(self,**kwargs):
        kwargs["_content"]=""
        kwargs["_tag"]="area"
        kwargs["_closing_tag"]=True
        self.add_tag(**kwargs)

    def table(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="table"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def caption(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="caption"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def colgroup(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="colgroup"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def col(self,**kwargs):
        kwargs["_content"]=""
        kwargs["_tag"]="col"
        kwargs["_closing_tag"]=True
        self.add_tag(**kwargs)

    def tbody(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="tbody"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def thead(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="thead"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def tfoot(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="tfoot"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def tr(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="tr"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def td(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="td"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def th(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="th"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def form(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="form"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def fieldset(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="fieldset"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def legend(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="legend"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def label(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="label"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def input(self,**kwargs):
        kwargs["_content"]=""
        kwargs["_tag"]="input"
        kwargs["_closing_tag"]=True
        self.add_tag(**kwargs)

    def button(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="button"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def select(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="select"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def datalist(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="datalist"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def optgroup(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="optgroup"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def option(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="option"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def textarea(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="textarea"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def output(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="output"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def progress(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="progress"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def meter(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="meter"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def details(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="details"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def summary(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="summary"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def menu(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="menu"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def menuitem(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="menuitem"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def dialog(self,_content,**kwargs):
        kwargs["_content"]=_content
        kwargs["_tag"]="dialog"
        kwargs["_closing_tag"]=False
        self.add_tag(**kwargs)

    def compile(self):
        compiled=""
        for data in self.pre_compiled:
            private_arguments={}
            for key in list(data.keys()):
                if key.startswith('_'):
                    private_arguments[key]=data.pop(key)
            if "_closing_tag" not in private_arguments:
                private_arguments["_closing_tag"]=False

            compiled= compiled + f"<{private_arguments["_tag"]}"
            for key,value in data.items():
                compiled= compiled + f' {key}="{value}" '
            if private_arguments["_closing_tag"] == True:
                compiled=compiled + ">"
            else:
                compiled= compiled + f">{private_arguments["_content"]}</{private_arguments['_tag']}>"
        
        return compiled
    

from .base.base_adapter import BaseAdapter
from .controller import {{cookiecutter.class_prefix}}Controller, {{cookiecutter.class_prefix}}Error


class {{cookiecutter.class_prefix}}Adapter(BaseAdapter):
    """{{cookiecutter.class_prefix.upper()}} Adapter class inheriting base adapter functionality."""

    controller_cls = {{cookiecutter.class_prefix}}Controller
    error_cls = {{cookiecutter.class_prefix}}Error
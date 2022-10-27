from os import listdir, makedirs
from os.path import basename, dirname, exists, isfile, join
from importlib.machinery import SourceFileLoader

from abc import ABC, abstractmethod

class DaoSystem(ABC):
    """Derivative - abstract base class and registry for reading digital object data from a number of sources.
    Since this is likely to require implementation-specific logic, these are designed as customizable plugins
    This class serves two purposes.  Firstly, it serves as an abstract base class, defining
    common methods and properties required to read digital object data into the description model.
    Secondly, it serves as a registry of such formats, with the goal of allowing new formats to
    be implemented in a "plug-in" fashion.  Any class subclassing this one, with the expected
    properties and a class variable "dao_system_name" will be registered on this class and thus usable
    by the software."""

    # Registry of dao systems, key = cls.dao_system_name, value = cls
    registry = {}

    def __init_subclass__(cls, **kwargs):
        """Enforce dao_system descriptive attributes on subclasses, register them"""
        dao_system_attrs = ["dao_system_name"]
        for attr in dao_system_attrs:
            if not hasattr(cls, attr):
                raise RuntimeError("DaoSystem subclass must have `" + attr + "` attribute")

        super().__init_subclass__(**kwargs)
        __class__.registry[cls.dao_system_name] = cls



    @abstractmethod
    def read_data(self, href):
        # parses digital object data from system managing digital objects and dao-level metadata
        pass


def import_dao_plugins(additional_dirs=None):
    if not additional_dirs:
        additional_dirs = []

    dirs = [join(dirname(__file__), "dao_plugins"), *additional_dirs]


    for plugin_dir in dirs:
        if not exists(plugin_dir):
            continue
        for filename in listdir(plugin_dir):
            module = basename(filename)[:-3]
            full_path = join(plugin_dir, filename)
            # skip if not a normal, non underscored file ending in .py
            if module.startswith("_") or not isfile(full_path) or filename[-3:] != ".py":
                continue
            SourceFileLoader(module, full_path).load_module()

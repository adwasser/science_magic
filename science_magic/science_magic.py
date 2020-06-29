# from pkg_resources import resource_string
import os, inspect
from IPython.core.magic import (Magics, magics_class, line_magic)

@magics_class
class ScienceMagic(Magics):

    @line_magic
    def science(self, line):
        """Import statements"""
        from . import science_imports
        with open(inspect.getfile(science_imports)) as f:
            s = f.read()
        ns = self.shell.user_ns
        print(s)
        exec(s, ns)
        # self.astro(line)
        self.stats(line)
        self.plotting(line)

    @line_magic
    def stats(self, line):
        from . import stats_imports
        with open(inspect.getfile(stats_imports)) as f:
            s = f.read()
        ns = self.shell.user_ns
        print(s)
        exec(s, ns)
        
    @line_magic
    def astro(self, line):
        """Import statements"""
        from . import astro_imports
        with open(inspect.getfile(astro_imports)) as f:
            s = f.read()
        ns = self.shell.user_ns
        print(s)
        exec(s, ns)

    @line_magic
    def plotting(self, line):
        """Import statements"""
        from . import plotting_imports
        with open(inspect.getfile(plotting_imports)) as f:
            s = f.read()
        ns = self.shell.user_ns
        print(s)
        exec(s, ns)

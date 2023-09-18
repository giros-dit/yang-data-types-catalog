'''
pyang plugin -- YANG data types discoverer.

Given a YANG module, it searches for its typedefs, generates their translations to
primite YANG types and outputs the result in JSON format.
This plugin is meant to be used with the data types catalog available at https://github.com/giros-dit/yang-data-types-catalog.

Version: 0.0.3.

Author: Networking and Virtualization Research Group (GIROS DIT-UPM) -- https://dit.upm.es/~giros.
'''

import optparse
import pdb
import re
import sys
import json

from pyang import plugin
from pyang import statements

def pyang_plugin_init():
    plugin.register_plugin(DataTypesDiscovererPlugin())

class DataTypesDiscovererPlugin(plugin.PyangPlugin):
    def __init__(self):
        plugin.PyangPlugin.__init__(self, 'data-types-discoverer')
    
    def add_output_format(self, fmts):
        self.multiple_modules = True
        fmts['data-types-discoverer'] = self
    
    def add_opts(self, optparser):
        optlist = [
            optparse.make_option('--data-types-discoverer-help', dest='print_data_types_discoverer_help', action='store_true', help='Prints help and usage.')
        ]
        g = optparser.add_option_group('YANG data types discoverer - Execution options')
        g.add_options(optlist)
    
    def setup_ctx(self, ctx):
        if ctx.opts.print_data_types_discoverer_help:
            print_data_types_discoverer_help()
            sys.exit(0)
    
    def setup_fmt(self, ctx):
        ctx.implicit_errors = False
    
    def emit(self, ctx, modules, fd):
        generate_output(ctx, modules, fd)

def print_data_types_discoverer_help():
    '''
    Prints help and usage information.
    '''
    print('''
Pyang plugin - YANG data types discoverer (data-types-discoverer).
Given a YANG module, it searches for its typedefs, generates their translations to
primite YANG types and outputs the result to a JSON file.
Output file name format is the following: <module_name>@<module_latest_revision>.json.
This plugin is meant to be used with the data types catalog available at https://github.com/giros-dit/yang-data-types-catalog.

Usage:
pyang -f data-types-discoverer <module.yang>
    ''')

def generate_output(ctx, modules, fd):
    '''
    Processes the YANG module and generates the corresponding output.
    '''

    # Use PDB to debug the code with pdb.set_trace().

    # CONSTANTS:

    YANG_PRIMITIVE_TYPES = [
        "int8", "int16", "int32", "int64",
        "uint8", "uint16", "uint32", "uint64",
        "decimal64", "string", "boolean", "enumeration",
        "bits", "binary", "empty", "union"
    ]

    for module in modules:
        data = {}

        module_name = str(module.i_modulename)
        data["module_name"] = module_name

        module_prefix = str(module.i_prefix)
        data["module_prefix"] = module_prefix

        module_namespace = str(module.search_one("namespace").arg)
        data["module_namespace"] = module_namespace

        module_latest_revision = str(module.i_latest_revision)
        data["module_revision"] = module_latest_revision

        data["module_typedefs"] = {}

        typedefs = module.search("typedef")

        typedefs_dict = {}

        if typedefs is not None:
            for typedef in typedefs:
                if typedef is not None:
                    typedef_name = str(typedef.arg)
                    typedef_type = str(typedef.search_one("type").arg)
                    typedefs_dict[typedef_name] = typedef_type

            for typedef in typedefs:
                if typedef is not None:
                    typedef_name = str(typedef.arg)
                    data["module_typedefs"][typedef_name] = {}
                    
                    typedef_type = str(typedef.search_one("type").arg)
                    data["module_typedefs"][typedef_name]["defined_type"] = typedef_type

                    typedef_primitive_type = ""
                    if typedef_type not in YANG_PRIMITIVE_TYPES:
                        typedef_primitive_type = typedefs_dict[typedef_type.replace(module_prefix + ":", "")]
                    else:
                        typedef_primitive_type = typedef_type
                    data["module_typedefs"][typedef_name]["primitive_type"] = typedef_primitive_type
        
        filename = module_name + "@" + module_latest_revision + ".json"
        file = open(filename, 'w')
        file.write(json.dumps(data, indent=4) + '\n')
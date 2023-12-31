# YANG data types catalog
YANG modules data types catalog with conversions to base/primitive YANG types.

This repository provides a registry or catalog of data types defined in YANG modules with the corresponding conversion to base or primitive YANG types.
The catalog consists of a set of JSON files with information about the YANG module and all the `typedefs` that are defined within it. These `typedefs` are identified
by their names and feature their "defined" type and the corresponding conversion to the base or primitive type. You can see the general structure of the JSON file below:

```
{
    "name": "<module_name>",
    "prefix": "<module_prefix>",
    "namespace": "<module_namespace_urn>",
    "latest_revision": "<module_latest_revision_date>",
    "description": "<module_description>,
    "typedefs": {
        "<typedef-1>": {
            "description": "<description>",
            "defined_type": "<defined_type>",
            "primitive_type": "<primitive_type>"
        },
        "<typedef-2>": {
            "description": "<description>",
            "defined_type": "<defined_type>",
            "primitive_type": "<primitive_type>"
        },
        ...
        "<typedef-N>": {
            "description": "<description>",
            "defined_type": "<defined_type>",
            "primitive_type": "<primitive_type>"
        }
    }
}
```

The discovery of module `typedefs`, their conversion to primitive types and the generation of catalog JSON files is done by a `pyang` plugin that we have developed: `data-types-discoverer`.

## Using the `pyang` plugin
You can find, view and download the plugin from the [`pyang`](pyang/data-types-discoverer.py) subdirectory.

Once downloaded, move it to `pyang`'s plugins directory, which is normally located under the following path in your Unix filesystem: `/home/<your_username>/.local/lib/<python_version>/site-packages/pyang/plugins/`.

To execute the plugin, run the following command. You can specify multiple YANG models and the plugin will generate the catalog file for each of one of them:

```
$ pyang -f data-types-discoverer <yang_module_1.yang> <yang_module_2.yang> ... <yang_module_N.yang>
```

Alternatively, you can run `pyang` and specify a custom directory path for plugins. In this case, use the `--plugindir` option and point to the path of the folder where you have stored the plugin.

The output is directly written to a JSON file with the following name: `<module_name>@<module_revision>.json`.

## Primitive YANG types
A list of the base (primitive) YANG types is attached below:

| **Data type** |                 **Description**                |
|:-------------:|:----------------------------------------------:|
|      int8     |              8-bit signed integer              |
|     int16     |              16-bit signed integer             |
|     int32     |              32-bit signed integer             |
|     int64     |              64-bit signed integer             |
|     uint8     |             8-bit unsigned integer             |
|     uint16    |             16-bit unsigned integer            |
|     uint32    |             32-bit unsigned integer            |
|     uint64    |             64-bit unsigned integer            |
|   decimal64   |      64-bit floating point decimal number      |
|     string    |             Sequence of characters             |
|    boolean    | Logic value (true/false), from Boolean algebra |
|  enumeration  |          Set of named/assigned values          |
|      bits     |                   Set of bits                  |
|     binary    |         Sequence of binary data/octets         |
|     empty     |                  Unvalued type                 |
|     union     |   Unrestricted union of other primitive types  |

## References
- YANG Data Types - YumaWorks Support: https://support.yumaworks.com/support/solutions/folders/1000233920.

# YANG data types catalog
YANG modules data types catalog with conversions to base/primitive YANG types.

This repository provides a registry or catalog of data types defined in YANG modules with the corresponding conversion to base or primitive YANG types.
The catalog consists of JSON files that contain key-value dictionaries with the data types association: the key is the custom data type defined in the YANG module, and the value is the conversion to the primitive YANG type. If there are several conversion steps, from a custom data type to another custom data type, the final conversion result with the primitive type is always given.
The name of the JSON files consists of the name of the corresponding YANG module with the latest revision date as per specified in it: e.g. `ietf-yang-types@2023-01-23.yang`.

## Primitive YANG types
A list of the base (primitive) YANG types is attached below:

| **Data type** |                 **Description**                |
|:-------------:|:----------------------------------------------:|
|      int8     |        8-bit signed integer (-128, +128)       |
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

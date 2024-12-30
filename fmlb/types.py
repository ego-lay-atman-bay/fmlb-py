from typing import Annotated

import dataclasses_struct as dcs


@dcs.dataclass()
class Header:
    magic: Annotated[bytes, 4] = b'_FML'
    unknown1: dcs.U32 = 0 # ?
    version: dcs.U32 = 8 # ?
    unkown2: dcs.U32 = 3 # ?
    num_files: dcs.U32 = 0
    data_offset: dcs.U32 = 0
    data_size: dcs.U32 = 0
    end: Annotated[bytes, dcs.PadAfter(16)] = b'END>'


@dcs.dataclass()
class FileMetadata:
    type: dcs.U32
    unknown: dcs.U32
    unknown2: dcs.U32
    name: Annotated[bytes, 64]
    data_offset: dcs.U32
    size: dcs.U32
    index: dcs.U16
    end: Annotated[bytes, 4] = b'\x00\x00>>'

from typing import BinaryIO, Annotated

import dataclasses_struct as dcs

from .file_utils import PathOrBinaryFile, open_binary


@dcs.dataclass()
class Header:
    magic: Annotated[bytes, 4] = b'_FML'
    version_major: dcs.U32 = 0 # ?
    version_minor: dcs.U32 = 8 # ?
    version_patch: dcs.U32 = 3 # ?
    num_files: dcs.U32 = 0
    data_offset: dcs.U32 = 0
    ender: Annotated[dcs.U32, dcs.PadAfter(16)] = 0

class FMLB:
    def __init__(self, file: PathOrBinaryFile):
        self.header = None

    def read(self, file: PathOrBinaryFile):
        with open_binary(file) as file:
            self.header = self._read_header(file)
    
    def _read_header(self, file: BinaryIO):
        file.seek(0)
        return Header.from_packed(
            file.read(dcs.get_struct_size(Header))
        )

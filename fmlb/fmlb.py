from typing import BinaryIO, Annotated

import dataclasses_struct as dcs

from .file_utils import PathOrBinaryFile, open_binary


@dcs.dataclass()
class Header:
    magic: Annotated[bytes, 4] = b'_FML'
    unknown1: dcs.U32 = 0 # ?
    version: dcs.U32 = 8 # ?
    unkown2: dcs.U32 = 3 # ?
    num_files: dcs.U32 = 0
    data_offset: dcs.U32 = 0
    data_size: dcs.U32 = 0
    ender: Annotated[dcs.U32, dcs.PadAfter(16)] = 0

@dcs.dataclass()
class FileMetadata:
    type: dcs.U32
    unknown: dcs.U32
    unknown2: dcs.U32
    name: Annotated[bytes, 64]
    data_offset: dcs.U32
    size: dcs.U32
    index: dcs.U16
    ender: dcs.U16

class FMLB:
    def __init__(self, file: PathOrBinaryFile | None = None):
        self.header = Header()
        self.file_metadata: list[FileMetadata] = []

        if file is not None:
            self.read(file)

    def read(self, file: PathOrBinaryFile):
        with open_binary(file) as file:
            self.header = self._read_header(file)
            self.file_metadata = self._read_file_list(file)
    
    def _read_header(self, file: BinaryIO) -> Header:
        file.seek(0)
        return Header.from_packed(
            file.read(dcs.get_struct_size(Header))
        )
    
    def _read_file_list(self, file: BinaryIO):
        metadatas = []
        
        for x in range(self.header.num_files):
            metadatas.append(
                FileMetadata.from_packed(
                    file.read(dcs.get_struct_size(FileMetadata))
                ),
            )
        
        return metadatas

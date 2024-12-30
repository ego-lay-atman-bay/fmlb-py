from typing import BinaryIO, Annotated

import dataclasses_struct as dcs

from .file_utils import PathOrBinaryFile, open_binary
from . import enums


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

class FMLB:
    def __init__(self, file: PathOrBinaryFile | None = None):
        self.header = Header()
        self.file_metadata: list[FileMetadata] = []
        self.files = []

        if file is not None:
            self.read(file)

    def read(self, file: PathOrBinaryFile):
        with open_binary(file) as file:
            self.header = self._read_header(file)
            self.file_metadata = self._read_file_list(file)
            
            for metadata in self.file_metadata:
                self.files.append(self._read_file(metadata, file))

    
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
                )
            )
        
        return metadatas
    
    def _read_file(self, file_metadata: FileMetadata, file: BinaryIO):
        match file_metadata.type:
            case enums.FileType.hier:
                pass
            case enums.FileType.txload:
                pass
            case enums.FileType.MATERIAL:
                pass
            case enums.FileType.GEOMETRY:
                pass
            case enums.FileType.PRIMITIVE:
                pass
            case enums.FileType.CLIP:
                pass
            case enums.FileType.aniplug:
                pass
            case enums.FileType.SOUND:
                pass
            case enums.FileType.SOUNDBANK:
                pass
            case enums.FileType.COLORSET:
                pass

from typing import BinaryIO

import dataclasses_struct as dcs

from fmlb.types import FileMetadata, Header

from . import enums
from .file_utils import PathOrBinaryFile, open_binary


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

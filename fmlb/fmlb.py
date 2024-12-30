from typing import BinaryIO

import dataclasses_struct as dcs

from fmlb.types import FileMetadata, Header

from . import enums
from .file_utils import PathOrBinaryFile, open_binary


class FMLB:
    def __init__(self, file: PathOrBinaryFile | None = None):
        self.header = Header()
        self.data_metadata: list[FileMetadata] = []
        self.data = []

        if file is not None:
            self.read(file)

    def read(self, file: PathOrBinaryFile):
        with open_binary(file) as file:
            self.header = self._read_header(file)
            self.data_metadata = self._read_data_list(file)
            
            for metadata in self.data_metadata:
                self.data.append(self._read_data(metadata, file))

    
    def _read_header(self, file: BinaryIO) -> Header:
        file.seek(0)
        return Header.from_packed(
            file.read(dcs.get_struct_size(Header))
        )
    
    def _read_data_list(self, file: BinaryIO):
        metadatas = []
        
        for x in range(self.header.num_files):
            metadatas.append(
                FileMetadata.from_packed(
                    file.read(dcs.get_struct_size(FileMetadata))
                )
            )
        
        return metadatas
    
    def _read_data(self, file_metadata: FileMetadata, file: BinaryIO):
        match file_metadata.type:
            case enums.DataType.hier:
                pass
            case enums.DataType.txload:
                pass
            case enums.DataType.MATERIAL:
                pass
            case enums.DataType.GEOMETRY:
                pass
            case enums.DataType.PRIMITIVE:
                pass
            case enums.DataType.CLIP:
                pass
            case enums.DataType.aniplug:
                pass
            case enums.DataType.SOUND:
                pass
            case enums.DataType.SOUNDBANK:
                pass
            case enums.DataType.COLORSET:
                pass

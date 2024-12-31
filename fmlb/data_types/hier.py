from typing import Annotated

import dataclasses_struct as dcs
from ..types import Vector3Float32

@dcs.dataclass()
class hierFoprmat:
    name: Annotated[bytes, 64]
    num_noes: dcs.U32
    center: Vector3Float32
    radius: dcs.F32
    label: Annotated[bytes, 140]
    
@dcs.dataclass()
class NodeFormat:
    type: dcs.U32
    name: Annotated[bytes, 64]
    

class hier:
    def __init__(self, data: bytes | None = None):
        if not data is None:
            self.read(data)
    
    def read(self, data: bytes):
        pass

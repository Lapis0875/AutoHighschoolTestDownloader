from __future__ import annotations
from enum import Enum
from typing import Dict, Any, Optional

JSON = Dict[str, Any]


class SubjectCode(Enum):
    Korean = 'kor'      # 국어
    English = 'eng'     # 영어
    MathA = 'matha'     # 수학 가형
    MathB = 'mathb'     # 수학 나형
    # 과학탐구
    Physics1 = 'g_phy1'   # 물리학1
    Physics2 = 'g_phy2'   # 물리학2
    # 사회탐구
    History = 's_his'

    @classmethod
    def parse(cls, value: str) -> Optional[SubjectCode]:
        for m in filter(lambda m: m.value == value, cls.__members__.values()):
            return m    # return first element
        # If no elements,
        return None

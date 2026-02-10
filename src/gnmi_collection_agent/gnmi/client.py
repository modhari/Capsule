from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class GnmiPath:
    origin: str
    path: str

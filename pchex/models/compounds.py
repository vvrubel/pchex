from __future__ import annotations

from typing import Iterable, Sequence

from pydantic import BaseModel

from .enums import Domain, NamespCmpd, Operation, Out, PropertyTags


class InputSpec(BaseModel):
    domain: Domain
    namespace: NamespCmpd
    ids: Iterable[str]


class OperationSpec(BaseModel):
    op: Operation
    tags: Sequence[PropertyTags]


class OutputSpec(BaseModel):
    out: Out


class CompoundUrlParams(BaseModel):
    input: InputSpec
    operation: OperationSpec
    output: OutputSpec


class RequestParams(BaseModel):
    start: int
    stop: int
    maxsize: int = 100

    @classmethod
    def from_string(cls, inp: str, sep: str = " ") -> RequestParams:
        start, stop, maxsize = map(int, inp.split(sep))
        return cls(start=start, stop=stop, maxsize=maxsize)

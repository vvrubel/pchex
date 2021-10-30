from typing import Iterator

from pchex.config import settings
from pchex.models.compounds import (
    CompoundUrlParams,
    InputSpec,
    OperationSpec,
    OutputSpec,
    RequestParams,
)
from pchex.models.enums import Domain, NamespCmpd, Operation, Out, PropertyTags


def generate_ids(start: int, stop: int, maxsize: int) -> Iterator[str]:
    chunk = []
    for i in range(start, stop + 1):
        chunk.append(str(i))
        if len(chunk) >= maxsize:
            yield ",".join(chunk)
            chunk.clear()
    if chunk:
        yield ",".join(chunk)


def generate_urls(params: RequestParams) -> Iterator[str]:
    obj = CompoundUrlParams(
        input=InputSpec(
            domain=Domain.COMPOUND,
            namespace=NamespCmpd.CID,
            ids=generate_ids(start=params.start, stop=params.stop, maxsize=params.maxsize),
        ),
        operation=OperationSpec(
            op=Operation.PROPERTY,
            tags=(
                PropertyTags.INCHI,
                PropertyTags.CANONICAL_SMILES,
            ),
        ),
        output=OutputSpec(out=Out.JSON),
    )
    for i in obj.input.ids:
        url = "/".join(
            [
                settings.pubchem_url,
                obj.input.domain,
                obj.input.namespace,
                i,
                obj.operation.op,
                ",".join(obj.operation.tags),
                obj.output.out,
            ]
        )
        yield url

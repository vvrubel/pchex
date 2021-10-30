from pchex.deps import generate_ids, generate_urls
from pchex.models.compounds import RequestParams


def test_generate_id() -> None:
    res = generate_ids(start=1, stop=14, maxsize=5)
    assert next(res) == "1,2,3,4,5"
    assert next(res) == "6,7,8,9,10"
    assert next(res) == "11,12,13,14"


def test_generate_url() -> None:
    params = RequestParams.from_string("1,14,5", sep=",")
    res = generate_urls(params=params)
    assert (
        next(res)
        == "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/1,2,3,4,5/property/InChI,"
        "CanonicalSMILES/JSON"
    )
    assert (
        next(res)
        == "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/6,7,8,9,10/property/InChI,"
        "CanonicalSMILES/JSON"
    )
    assert (
        next(res)
        == "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/11,12,13,14/property/InChI,"
        "CanonicalSMILES/JSON"
    )

import json
import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = json.load(open('testdata.json'))
testdata_ids = range(1, len(testdata) + 1)


@pytest.mark.parametrize('points, expected', testdata, ids=testdata_ids)
def test_run(points, expected):
    assert main.run(points).strip() == expected

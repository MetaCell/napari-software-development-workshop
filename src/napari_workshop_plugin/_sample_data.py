"""Return sample data."""
from pathlib import Path
from typing import List

from ._reader import read_numpy_file

here = Path(__file__).parent.resolve()


def load_sample_data() -> List[tuple]:
    """Load sample data."""
    path = str(here / "data" / "sample.npy")
    return read_numpy_file(path)

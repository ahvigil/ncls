from ncls.src.ncls import NCLS64
from ncls.src.ncls32 import NCLS32

import numpy as np

def NCLS(starts, ends, ids):

    if isinstance(starts, list) or "pandas" in str(type(starts)):
        starts, ends, ids = [np.array(s) for s in [starts, ends, ids]]

    ids = ids.astype(np.int64)
    if starts.dtype == np.int64:
        return NCLS64(starts.astype(np.int64), ends.astype(np.int64), ids)
    elif starts.dtype == np.int32:
        return NCLS32(starts.astype(np.int32), ends.astype(np.int32), ids)
    else:
        raise Exception("Starts/Ends not int64 or int32: " + str(starts.dtype))


def FNCLS(starts, ends, ids):

    from ncls.src.fncls import FNCLS

    if isinstance(starts, list) or "pandas" in str(type(starts)):
        starts, ends, ids = [np.array(s) for s in [starts, ends, ids]]

    if starts.dtype == np.double:
        return FNCLS(starts, ends.astype(np.double), ids)
    else:
        raise Exception("Starts/Ends not double: " + str(starts.dtype))

from ncls.version import __version__

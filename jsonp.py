import json
from urllib.request import urlopen
with urlopen("https://sheets.googleapis.com/$discovery/rest?version=v4") as res:
    data=res.read()
dat=json.loads(data)
print(json.dumps(dat,indent=2))

# testing codes

import unittest
import useModule
import math
class tes(unittest.TestCase):
    def test_phe(self):
        self.assertEqual(useModule.facto(12),math.factorial(12))

if __name__=="__main__":
    unittest.main()
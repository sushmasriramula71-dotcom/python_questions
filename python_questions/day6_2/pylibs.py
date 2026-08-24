import datetime
from datetime import datetime
now=datetime.now()
print(now)

from pathlib import Path
files=Path(".").glob("main.py")

for file in files:  
    print(file)

import sys
print(sys.argv)

from collections import Counter
nums=[1,2,3,4,4,5,6]
print(Counter(nums))



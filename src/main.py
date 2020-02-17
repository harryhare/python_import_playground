import dir001.c
import package001.b
dir001.c.test_c()
package001.a.test_a()
package001.b.test_b()

# use import in __init__.py
import package001

package001.test()
package001.test_a()
package001.test_not_in_all()

# user __all__ in __init.py
from package001 import *
test()
b.test_b() # if __all__ is not in use, this line cause error
#test_not_in_all() # if __all__ is in use, this line cause error
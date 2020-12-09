import cProfile
import WebSite.main as main

cProfile.run('main.show_achievements()', 'profile_stats')

import pstats
from pstats import SortKey
p = pstats.Stats('profile_stats')
p.strip_dirs().sort_stats(SortKey.CUMULATIVE).print_stats(20)
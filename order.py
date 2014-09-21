#
#
# This script orders packages in sys.argv[1] = /etc/portage/package.use in  Gentoo OS
# For example, add this script to crontab
#
#

import sys
from time import gmtime, strftime
import collections

def sort(filename):
    with open(filename) as f:

        d = dict()

        for line in [x.split(' ', 1) for x in f.readlines() if x != '\n' and not x.startswith('#')]:
            d[line[0]] = str.join(' ', sorted(line[1][:-1].split(' ')))

        od = collections.OrderedDict(sorted(d.items()))

    with open(filename, 'w') as f:
        f.write('## Last modified at {}\n## by {} script\n\n\n'.format(strftime("%d %m %Y, %H:%M:%S"), sys.argv[0]))
        for k, v in od.items():
            f.write('{} {}\n'.format(k, v))

if __name__ == '__main__':
    sort(sys.argv[1])

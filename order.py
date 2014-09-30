#
#
# This script orders packages in sys.argv[1] = /etc/portage/package.use in  Gentoo OS
# For example, add this script to crontab
#
#

import sys
from time import strftime
from collections import OrderedDict as OD

def sort(filename):
    d = dict()

    with open(filename, 'r') as f:
        for line in [x.split(' ', 1) for x in f.readlines() if x != '\n' and not x.startswith('#')]:
            d[line[0]] = str.join(' ', sorted(line[1][:-1].split(' ')))

    with open(filename, 'w') as f:
        od = OD(sorted(d.items()))
        print('## Last modified at {}\n## by {} script\n\n\n'.format(
                    strftime("%d %m %Y, %H:%M:%S"),
                    sys.argv[0]),
                    str.join('\n',
                            (
                                str.format('{} {}', *kv) for i, kv in enumerate(od.items(), start = 1) if True
                            )
                        ),
            file = f)

if __name__ == '__main__':
    sort(sys.argv[1])

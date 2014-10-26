#
#
# This script orders packages in sys.argv[1] = /etc/portage/package.use in  Gentoo OS
# For example, add this script to crontab
#
#

import sys
from time import strftime
from shutil import copyfile


def sort(filename):
    d = dict()

    with open(filename, 'r') as f:
        for line in [x.split(' ', 1) for x in f.readlines() if x != '\n' and not x.startswith('#')]:
            uses = line[1][:-1].split(' ')
            uses.sort(key = lambda s: s.startswith('-'))
            d[line[0]] = str.join(' ', uses)
            
            copyfile(filename, '{}.bak'.format(filename))


    with open(filename, 'w') as f:
        f.write('## Last modified at {}\n\n{}'.format(
            strftime("%d %m %Y, %H:%M:%S"),
            '\n'.join(
                (
                    ('{} {}'.format(k, v)) for k, v in sorted(d.items())
                )
            )
        ))

if __name__ == '__main__':
    sort(sys.argv[1])

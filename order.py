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
        print('## Last modified at {}\n## by {} script\n\n\n'.format(
                    strftime("%d %m %Y, %H:%M:%S"),
                    sys.argv[0]),
                    str.join('\n',
                            (
                                str.format('{} {}', *kv) for i, kv in enumerate(sorted(d.items()), start=1) if True
                            )
                        ),
            file = f)

if __name__ == '__main__':
    sort(sys.argv[1])

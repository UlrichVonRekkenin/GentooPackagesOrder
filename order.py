#
#
# This script orders packages in sys.argv[1] = /etc/portage/package.use/custom in  Gentoo OS
# and may add "on-the-fly" new packages from sys.argv[2]:str
# For example, add this script to crontab
#
#


import sys
from time import strftime
import shutil
import pathlib


def _copy(orig, target):

    with pathlib.Path(orig).open('r') as orig_file:
        with pathlib.Path(target).open('w') as target_file:

            for line in orig_file.readlines():
                target_file.write(line)


def _unique(orig):
    output = []

    for item in orig:
        if item not in output:
            output.append(item)
    return output


def sort(argv):

    filename = argv[0]
    new_pkg, new_use = argv[1].split(maxsplit=1)[0], argv[1].split(maxsplit=1)[1]

    print('Work with "{}"\npkg "{}"\nuses "{}"'.format(filename, new_pkg, new_use))

    d = dict()
    current_time = lambda fmt: strftime(fmt)
    path2bakcup = lambda arg, fmt: pathlib.Path().joinpath(
        pathlib.PurePath(arg).parent, '.' + pathlib.PurePath(arg).name + current_time(fmt)
    )

    _copy(filename, path2bakcup(filename, '.%d.%m.%Y-%H.%M'))


    with pathlib.Path(filename).open('r') as f:

        for pkg, uses in [x.split(' ', 1) for x in f.readlines() if x != '\n' and not x.startswith('#')]:


            d[pkg] = uses[:-1]

            if new_pkg == pkg:
                d[new_pkg] = ' '.join(_unique('{} {}'.format(d[new_pkg], new_use).split()))
            else:
                d[new_pkg] = new_use


        for pkg, uses in d.items():
            includes, excludes = [], []

            for use in uses.split():
                if use.startswith('-'):
                    excludes.append(use)
                else:
                    includes.append(use)

            d[pkg] = '{} {}'.format(' '.join(sorted(includes)), ' '.join(sorted(excludes)))


    with pathlib.Path(filename).open('w') as f:
        f.write('## Last modified at {time}\n\n{pkgs}'.format(

            time=current_time('%d.%m.%Y %H:%M'),

            pkgs='\n'.join(
                (
                    ('{} {}'.format(*kv)) for kv in sorted(d.items())
                )
            )

        ))


if __name__ == '__main__':

    if len(sys.argv) > 1 and len(sys.argv[2]):
        sort(sys.argv[1:])
    else:
        print('Usage:\npython3 order.py /etc/portage/package.use/custom "pkg use1 use2 etc"')

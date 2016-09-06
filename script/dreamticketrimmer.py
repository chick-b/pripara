import os, sys

argv = sys.argv

inputpath = os.path.abspath(argv[1])
base, ext = os.path.splitext(inputpath)
outputpath = inputpath.replace(ext, '_crop' + ext)

import subprocess
cmd = ['magick', 'convert', inputpath, '-crop', '959x943+63+724', outputpath ]
# cmd = ['magick', 'convert', inputpath, '-crop', '307x943+63+724', outputpath ]
subprocess.run(cmd)

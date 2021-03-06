# gozerbot/utils/fileutils.py
#
# Description: Various file utilities
# Author: Wijnand 'tehmaze' Modderman
# Author URL: http://tehmaze.com
# License: BSD

from generic import istr
import tarfile, os, types, cStringIO, gzip

def tarextract(package, fileobj=None, prefix=None, base=None):
    '''
    Extracts a tarball from ``package``, or, if ``fileobj`` is either a string or a seekable
    IO stream, it will extract the data from there. We only extract files from the tarball
    that are member of the ``base`` directory if a ``base`` is specified.
    '''
    extracted = []
    # if we have a fileobj, make sure it's a seekable stream, and not a string
    if fileobj:
        if type(fileobj) == types.StringType:
            fileobj = cStringIO.StringIO(fileobj)
        tarf = tarfile.open(mode='r|', fileobj=fileobj)
    else:
        tarf = tarfile.open(package, 'r')
    # iterate tarball and extract candidates
    for tarinfo in tarf:
        if tarinfo.name.startswith('/'):
            tarinfo.name = tarinfo.name[1:] # strip leading /
        if not base or ((tarinfo.name.rstrip('/') == base and tarinfo.isdir()) or tarinfo.name.startswith(base+os.sep)):
            if prefix:
                tarinfo.name = '/'.join([prefix, tarinfo.name])
            tarf.extract(tarinfo)
            extracted.append(tarinfo.name)
    tarf.close()
    # clean up
    if fileobj:
        try:
            fileobj.close()
        except:
            pass
        del fileobj
    return extracted


def gunzip(fileobj):
    if type(fileobj) == types.StringType or isinstance(fileobj, istr):
        fileobj = cStringIO.StringIO(str(fileobj))
    return gzip.GzipFile(mode='rb', fileobj=fileobj).read()

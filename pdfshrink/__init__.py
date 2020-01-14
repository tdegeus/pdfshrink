'''pdfshrink
    Shrink a PDFs file size using GhostScript.

Usage:
    pdfshrink [options] <files>...

Options:
    -o, --output=<N>    Specify output file. (default: overwrite the input file(s))
    -s, --silent        Do not print any progress.
        --verbose       Verbose all commands.
    -h, --help          Show help.
        --version       Show version.

(c - MIT) T.W.J. de Geus | tom@geus.me | www.geus.me
'''

# ==================================================================================================

import sys
import os
import re
import subprocess
import shutil
import tempfile
import docopt
import click

__version__ = '0.1.0'

# --------------------------------------------------------------------------------------------------
# Command-line error: show message and quit with exit code "1"
# --------------------------------------------------------------------------------------------------

def Error(text):

    print(text)
    sys.exit(1)

# --------------------------------------------------------------------------------------------------
# Run command (and verbose it), and return the command's output
# --------------------------------------------------------------------------------------------------

def Run(cmd, verbose=False):

    out = subprocess.check_output(cmd, shell=True).decode('utf-8')

    if verbose:
        print(cmd)
        print(out)

    return out

# --------------------------------------------------------------------------------------------------
# Main routine
# --------------------------------------------------------------------------------------------------

def main():

    args = docopt.docopt(__doc__, version=__version__)

    # Change keys to simplify implementation:
    # - remove leading "-" and "--" from options
    # - change "-" to "_" to facilitate direct use in print format
    # - remove "<...>"
    args = {re.sub(r'([\-]{1,2})(.*)',r'\2',key): args[key] for key in args}
    args = {key.replace('-','_'): args[key] for key in args}
    args = {re.sub(r'(<)(.*)(>)',r'\2',key): args[key] for key in args}

    if not shutil.which('gs'):
        Error('"gs" not found')

    for file in args['files']:
        if not os.path.isfile(file):
            Error('"{0:s}" does not exist'.format(file))

    if args['output']:
        if len(args['files']) > 1:
            Error('To use a custom output-file, call PDFs one-by-one')

    if args['output']:
        outdir = os.path.dirname(args['output'])
    else:
        outdir = tempfile.mkdtemp()

    if not os.path.isdir(outdir):
        os.makedirs(outdir)

    for file in args['files']:

        if args['output']:
            out = args['output']
        else:
            out = os.path.join(outdir, 'pdfshrink.pdf')

        cmd = ' '.join([
            'gs -q -dBATCH -dNOPAUSE -sDEVICE=pdfwrite',
            '-dPDFSETTINGS=/printer',
            '-dCompatibilityLevel=1.3',
            '-dColorImageDownsampleType=/Bicubic'
            '-dColorImageResolution=72',
            '-dGrayImageDownsampleType=/Bicubic',
            '-dGrayImageResolution=72',
            '-dMonoImageDownsampleType=/Bicubic',
            '-dMonoImageResolution=38',
            '-dOptimize=true',
            '-dEmbedAllFonts=true',
            '-dSubsetFonts=true',
            '-dDownsampleColorImages=true',
            '-dDownsampleGrayImages=true',
            '-dDownsampleMonoImages=true',
            '-dHaveTransparency=false',
            '-dColorConversionStrategy=/sRGB',
            '-sOutputFile="%s"' % out,
            '"%s"' % file,
        ])

        Run(cmd, args['verbose'])

        if not args['output']:
            shutil.move(out, file)
            if args['verbose']:
                print('mv {out:s} {file:s}'.format(out=out, file=file))
                print('')

        if not args['silent']:
            if args['output']:
                print('[pdfshrink] {file:s} {out:s}'.format(file=file, out=out))
            else:
                print('[pdfshrink] {file:s}'.format(file=file))

    if not args['output']:
        shutil.rmtree(outdir)
        if args['verbose']:
            print('rm -r {out:s}'.format(out=outdir))
            print('')

# --------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    main()

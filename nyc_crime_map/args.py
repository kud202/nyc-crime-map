import argparse
default = './data'
parser = argparse.ArgumentParser(description='Download crime data from the NYC Crime Map')
parser.add_argument('-v', '--verbose', action = 'store_true',
                    help = 'Pass this flag to turn on debugging output.')
parser.add_argument('-d', '--directory', type = str, default = default,
                    help = 'Outputs are saved to this directory. Default is "%s".' % default)

import sys
import argparse as ap

def read_args():
	p = ap.ArgumentParser()
	p.add_argument('-a', nargs='+', help='seperate by " "')
	p.add_argument('-b', help='b value', default=10)
	return p.parse_args()

if __name__ == '__main__':
	if len(sys.argv) == 1:
		sys.argv.append('-h')
arg = read_args()
print(arg)

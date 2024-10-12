#coding:utf-8

import sys
from loguru import logger

try:
	from hellokit import system, sequence
except ModuleNotFoundError:
    logger.error(f'<hellokit> required, try <pip3 install hellokit>.')
	sys.exit()

def fxlength(seq: str = None, plot: bool = False, avg_only: bool=False) -> None:
	'''
	stdout length of each sequence,
	plot a histgram if plot=True was set.

	args:
	-----

	seq: file
		input sequence file, fastq or fasta.
	plot: bool, default = False
		set to plot histgram of sequences' length.
	avg_only: bool, default = False
		set to print average length only.
	'''

	system.check_file(seq)

	length = {}
	length['length'] = {}
	if not avg_only: print(f'seqid\tlength\n')
	handle = system.open_file(seq)
	for name, seq, qual in sequence.readseq(handle):
		if not avg_only: print(f'{name}\t{len(seq)}\n')
		length['length'][name] = len(seq)

	if avg_only or plot:
		try:
			import pandas as pd
		except ModuleNotFoundError:
			sys.exit(f'<pandas> required, try <pip install pandas>.')

			# dict to DataFrame
		length = pd.DataFrame.from_dict(length)

	if avg_only: print(f'The mean length is {mean(length.length)}')

	if plot:

		try:
			import matplotlib
		except ModuleNotFoundError:
			sys.exit(f'<matplotlib> required, try <pip3 install matplotlib>.')

		matplotlib.use('Agg')
		import matplotlib.pyplot as plt

		ax = plt.subplot()
		xticks = [i for i in range(0, length.max()[0], 20)]
		s = 6 if len(xticks) <20 else 1
		ax.set_xticks(xticks)
		ax.set_xticklabels(xticks, fontdict={'fontsize':s})
		ax.text(0.95, 0.01, mean(length.length),
        		verticalalignment='bottom',
				horizontalalignment='right')
		# print(xticks)
		length.hist(column='length', grid=False, bins=10000, ax=ax)
		plt.savefig(f'{seq}.len.pdf', dpi=600)
		logger.info(f'The histogram stored at {seq}.len.pdf')

#coding:utf-8

import sys
from loguru import logger

try:
	import numpy as np
except ModuleNotFoundError:
    logger.error(f'<numpy> required, try <pip install numpy>.')
	sys.exit()

try:
	from hellokit import system, sequence
except ModuleNotFoundError:
    logger.error(f'<hellokit> required, try <pip install hellokit>.')
	sys.exit()


def check_pred(fq: str = None, num: int =  1000) -> None:

	'''
	Check phred value of input fastq.

	args:
	-----

	fq: file
		input fastq file.
	num : int
		number of sequence for phred check.
	'''

	system.check_file(fq)
	logger.info(f'Checking Phred value using {num} sequences.')
	universal_quals, universal_mins, c = [], [], 0
	fh = system.open_file(fq)
	for name, seq, qual in sequence.readseq(fh):
		if c < num:
			qual = [ord(i) for i in qual]
			universal_quals.extend(qual)
			universal_mins.append(min(qual))
			c += 1
		else:
			break
	fh.close()
	print(f'Mean of all input ASCII: {np.mean(universal_quals)}\n')
	print(f'Mean of all minimum ASCII: {np.mean(universal_mins)}\n')
	print(f'SD of all minimum ASCII: {np.std(universal_mins)}\n')

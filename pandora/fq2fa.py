#coding:utf-8

import os
import sys
from loguru import logger

from . import readseq

try:
	from hellokit import system
except ModuleNotFoundError:
    logger.error(f'<hellokit> required, try <pip3 install hellokit>.')
	sys.exit()


def fq2fa(fq: str = None):
	'''
	convert fastq to fasta.

	args:
	-----
	fq: file
		input fastq file (.gz).
	'''

	system.check_file(fq)
	handle = system.open_file(fq)
	for name, seq, qual in readseq.readseq(handle):
		print(f'>{name}\n{seq}\n')
	handle.close()

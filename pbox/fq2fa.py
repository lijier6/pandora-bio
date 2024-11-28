#coding:utf-8

import os
import sys
from loguru import logger

try:
	from ubox import usys, useq
except ModuleNotFoundError:
	logger.error('<hellokit> required, try <pip3 install hellokit>.')
	sys.exit()


def fq2fa(fq: str = None) -> None:
	'''
	Convert fastq to fasta.

	Parameter
	---------
	fq := str
		input fastq file (.gz).
	'''

	usys.check_file(fq)
	handle = usys.open_file(fq)
	for name, seq, qual in useq.readseq(handle):
		print(f'>{name}\n{seq}')
	handle.close()

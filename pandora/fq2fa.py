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


class FQ2FA:
	def __init__(self, fq: str = None):
		"""
		convert fastq to fasta.

		args:
			fq: file
				input fastq file (.gz).
		"""

		selt.fq = fq

		system.check_file(self.fq)

	def fq2fa(self):
		handle = system.open_file(self.fq)
		for name, seq, qual in readseq.readseq(handle):
			print(f'>{name}\n{seq}\n')
		handle.close()

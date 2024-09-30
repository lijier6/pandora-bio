#coding:utf-8

import sys
from loguru import logger

from . import readseq

try:
	import pandas as pd
except ModuleNotFoundError:
    sys.exit(f'<pandas> required, try <pip install pandas>.')

try:
	from hellokit import system
except ModuleNotFoundError:
    sys.exit(f'<hellokit> required, try <pip install hellokit>.')


class Extract_Seq:
	def __init__(self, seqid: str = None, idlist: str = None, seqin: str = None,
				fastq: bool = False, unmatch: bool = False):
		"""
		Extract sequences from fasta or fastq file.

		args:
			seqid: str
				sequence id to extract.
			idlist: file
				sequence id list to extract.
			seqin: file
				input fasta or fastq sequence file.
			fastq: bool
				set if input is fastq.
			unmatch: bool
				set to extract unmatch sequences
		"""

		self.seqid = seqid
		self.idlist = idlist
		self.seqin = seqin
		self.fastq = fastq
		self.unmatch = unmatch

		system.check_file(self.seqin)
		if self.idlist: system.check_file(self.idlist)

	def extract_seq(self):
		handle = system.open_file(self.seqin)
		allid = self.seqid and self.seqid or pd.read_csv(self.idlist, squeeze=False, header=None, index_col=0, sep='\t').index
		if not self.fastq:
			logger.info('Extracting sequences from fasta file.')
			if not self.unmatch:
				for name, seq, _ in readseq.readseq(handle):
					if name in allid:
						print(f'>{name}\n{seq}\n')
			else:
				for name, seq, _ in readseq.readseq(handle):
					if name not in allid:
						print(f'>{name}\n{seq}\n')
		else:
			logger.info('Extracting sequences from fastq file.')
			if not self.unmatch:
				for name, seq, qual in readseq.readseq(handle):
					if name in allid:
						print(f'@{name}\n{seq}\n+\n{qual}\n')
			else:
				for name, seq, qual in readseq.readseq(handle):
					if name not in allid:
						print(f'@{name}\n{seq}\n+\n{qual}\n')

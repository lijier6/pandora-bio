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



def extract_seq(seqid: str = None, idlist: str = None, seqin: str = None,
				fastq: bool = False, unmatch: bool = False):
	'''
	Extract sequences from fasta or fastq file.

	args:
	-----
	
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
		'''

		system.check_file(seqin)
		if idlist: system.check_file(idlist)

	def extract_seq(self):
		handle = system.open_file(seqin)
		allid = seqid and seqid or pd.read_csv(idlist, squeeze=False, header=None, index_col=0, sep='\t').index
		if not fastq:
			logger.info('Extracting sequences from fasta file.')
			if not unmatch:
				for name, seq, _ in readseq.readseq(handle):
					if name in allid:
						print(f'>{name}\n{seq}\n')
			else:
				for name, seq, _ in readseq.readseq(handle):
					if name not in allid:
						print(f'>{name}\n{seq}\n')
		else:
			logger.info('Extracting sequences from fastq file.')
			if not unmatch:
				for name, seq, qual in readseq.readseq(handle):
					if name in allid:
						print(f'@{name}\n{seq}\n+\n{qual}\n')
			else:
				for name, seq, qual in readseq.readseq(handle):
					if name not in allid:
						print(f'@{name}\n{seq}\n+\n{qual}\n')

#coding:utf-8

import sys
from loguru import logger

try:
	import pandas as pd
except ModuleNotFoundError:
    logger.error(f'<pandas> required, try <pip install pandas>.')
	sys.exit()

try:
	from hellokit import system
except ModuleNotFoundError:
    logger.error(f'<hellokit> required, try <pip install hellokit>.')
	sys.exit()



def abs2rel(table: str = None, out_table: str = None):
	'''
	Calculate relative abundance for each sample in the table
	and insert it to the table.

	args:
	-----
	
	table: file
		input table, column indicates sample, row indicates species, mags, OTU and so on.
	out_table: str
		name of output table. Print table if not set.
	'''

	system.check_file(table, check_empty=True)
	in_table = pd.read_csv(table, sep='\t', header=0, index_col=0)

	head = []
	for i in in_table.columns:
		head.extend([i, f'{i}(%)'])
		in_table[f'{i}(%)'] = in_table[i]/in_table[i].sum()*100
	out_table and in_table.to_csv(out_table, sep='\t') or print(in_table)

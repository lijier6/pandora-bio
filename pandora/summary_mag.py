
import sys

try:
	import pandas
except ModuleNotFoundError:
    sys.exit(f'<pandas> required, try <pip install pandas>.')

try:
	from hellokit import system
except ModuleNotFoundError:
    sys.exit(f'<hellokit> required, try <pip install hellokit>.')


def summary_mag(input=None, completeness: int = 80, contamination: int == 20):
	'''
	Summry mag quality from checkM result.

	args:
	-----

	input: str
		Input checkM result (list).
	completeness: int
		Completeness cutoff to summary.
	contamination: int
		Contamination cutoff to summary.
	'''

	def count_good_mag(df):
		read_df = pd.read_csv(df, sep='\t', header=0, index_col=0)
		read_df = read_df[(read_df.Completeness>=completness) & (read_df.Contamination<=contamination)]
		print(f'There are {len(read_df)} bins with completenss >= {completenss} \
				and contamination <= {contamination} in {df}.')
		return read_df

	def stat_mag(df):
		complet, contam, step = 100, 0, 5
		num = min([complet - completenss, contamination - contam])
		for i in range(num):
			comp, cont = complet-i*step, contam+i*step
			temp_df = df[(df.Completeness>=comp) & (df.Contamination<=cont)]
			print(f'There are {len(temp_df)} bins with completenss >= {comp} \
					and contamination <= {cont}.')

	if len(input) == 1:
		system.check_file(input)
		df = count_good_mag(input)
		stat_mag(df)
	else:
		all_df = []
		for i in input:
			system.check_file(i)
			df_i = count_good_mag(i)
			all_df.append(df_i)
		all_df = pd.concat(all_df)
		stat_mag(all_df)


"""############
TODO 28.08.2020:
-make it so that you can use different distance calculations

"""




"""By Radek, modified by Magnus
25-11-2019
This script is a modified version of Radek's featuring a slightly faster depth-algorithm(if you can
call this an algorithm), user-specified amount of branches per node and user specified amount of nodes.
In addition, I have implemented a measure to clean the graph of mirrored duplicates that occur in 
correlation matrices.
"""
import os
import io
import sys
import csv
import copy
import time
import json
import operator
from collections import Counter




class GraphNetwork:
	def __init__(self, root_node, max_depth, branches, nodes, min_score, transponse_flag, dataset):

		self.root_node=root_node
		self.max_depth=max_depth
		self.branches=branches
		self.nodes=nodes
		self.min_score=min_score
		self.transponse_flag = transponse_flag
		self.dataset = dataset


		if self.min_score<=0:
			self.min_score=0.0001
		if self.nodes>100:
			self.nodes=100

		self.headers = []
		self.data = {}
		self.n_headers = []
		self.n_data = {}
		self.t_headers = []
		self.t_data = {}

		self.result=[]

	#this is the sole function you need to call to process a dataset
	def pipeline(self):
		start=time.time()

		self.open_csv()
		self.result=sorted(self.get_intersected(self.root_node, self.headers, self.data, self.min_score), key=operator.itemgetter('score'), reverse=True)

		self.result=self.remove_duplicates(self.result)
		if self.branches>0:
				self.result=self.result[:self.branches]

		self.set_depth()

		if self.nodes>0:
			self.set_nodes()

		self.result=sorted(sorted(self.result, key=operator.itemgetter('score'), 
			reverse=True), key=operator.itemgetter('depth', 'root_symbol')) 	

		end=time.time()
		#return JSON array, amount of nodes and max depth

		if len(self.result)>0:
			return {"data": list(map(operator.itemgetter('root_symbol', 'cor_symbol'), self.result)), "total_nodes": len(self.result), "max_depth": self.result[-1]['depth'], "elapsed_time": round(end-start, 4) }
		else:
			return {"data": "empty_graph"}


	#incase dataset is a string for a file or is a file object
	def open_csv(self):
		if isinstance(self.dataset, str):
			with open(self.dataset) as file:
				self.delim=self.check_filetype(self.dataset)
				self.read_csv(file)
		else:
			self.delim=self.check_filetype(self.dataset.filename)
			self.read_csv(io.TextIOWrapper(self.dataset))


	def read_csv(self, dataset):
		#NAMING CONVENTION:
		"""	-csv_reader: the ordinary csv.reader object for the dataset
			-headers: the row/column labels of the dataset depending on trasnposing
			-n_header: nomincal headers, basically identical to headers
			-data: a dict with headers as keys and correlation scores in a list as value
			-t_headers: the opposite header of headers, used when the columns are unique from rows(eg. pharmaceutical companies on drug compounds)
			-t_csv: transposed variant of csv_reader
			-t_data: the transposed variant of data, same usecase as t_headers where the dataset has unique rows from colunmns

			PLEASE contact me if you think this look like crap and there's a better method"""
		
		csv_reader = csv.reader(dataset, delimiter=self.delim)
		if self.transponse_flag==1:
			csv_reader=self.zipper(csv_reader)

		#loads the labels into variables
		self.headers = [i.strip(' ') for i in next(csv_reader)[1:] if i.strip()]
		self.n_headers = self.headers[:]



		for row in csv_reader:
			temp=row[0].strip(' ')
			self.t_headers.append(temp)
			self.data[temp] = [float(x) for x in row[1:]]
		self.n_data = self.data.copy()

		#I don't really quite remember but I believe this is to check if this is a 1-on-1 correlation matrix or if the row labels are different from the column labels....
		if Counter(self.headers) == Counter(self.t_headers):
			self.t_headers=self.n_headers
			self.t_data=self.n_data


		else:
			t_csv=self.zipper(csv_reader)
			for row in t_csv:
				temp=row[0].strip(' ')
				self.t_data[temp] = [float(x) for x in row[1:]]

	"""------------------------------------------------------------------------------------------------"""

	#this function gets all the correlated symbols of the root symbol
	def get_intersected(self, symbol, headers, dict, min_score, depth=1):
		return [{'root_symbol':symbol, 'cor_symbol':headers[i].strip(), 'score':score, 'depth':depth} for i,
		score in enumerate(dict[symbol]) if score > min_score and headers[i].strip()!=symbol]



	def set_depth(self):
		#initialize 2 lists containing symbols

		symbols=[]
		covered_symbols=[]
		temp=[]
		count=0
		covered_symbols.append(self.root_node)

		#this is used for the while loop(subtracted by 1 because first level has already been covered above)
		remainer_depth=self.max_depth-1
		what_is_header=""

		while remainer_depth>0 and len(self.result)<self.nodes:
			if count%2==1:
				self.data=self.n_data.copy()
				self.headers=self.n_headers[:]
				what_is_header="nominal"

			else:
				self.data=self.t_data.copy()
				self.headers=self.t_headers[:]
				what_is_header="transposed"
			#print(what_is_header)


			#removes all symbols previously covered
			symbols=[x for x in symbols if x not in covered_symbols]
			for j in range(len(self.result)):
				#checking if the symbol in question has already been covered or not
				if(self.result[j]['cor_symbol'] not in covered_symbols and self.result[j]['cor_symbol'] not in symbols):
					symbols.append(self.result[j]['cor_symbol'])
			
			temp[:]=[]
			#print(what_is_header)
			if 0==0:
				for name in symbols:
					#performs the same function as with the root symbol
					temp[(len(temp)):]=self.get_intersected(name, self.headers, self.data, self.min_score, self.max_depth-remainer_depth+1)
			"""except:
				pass"""
			remainer_depth-=1


			temp=sorted(sorted(temp, key=operator.itemgetter('score'), reverse=True), 
				key=operator.itemgetter('depth'))

			#updates symbols already covered
			covered_symbols.extend(symbols)
			temp=self.remove_duplicates(temp)
			if self.branches>0:
				temp=self.set_branches(temp, covered_symbols)

			self.result.extend(temp)

			count+=1

	#removes duplicates because a correlation matrix is mirrored right? Please contribute if there's a better way of doing this
	def remove_duplicates(self, result):
		duplicates=[]
		for i in range(len(result)):
			for j in range(len(result)):
				#long if condition lmao
				if (((result[i]['root_symbol']==result[j]['cor_symbol'] and result[i]['cor_symbol']==result[j]['root_symbol']) or 
					(result[i]['root_symbol']==result[j]['root_symbol'] and result[i]['cor_symbol']==result[j]['cor_symbol'] and 
					result[i]['depth']!=result[j]['depth']))  and result[i] not in duplicates):
					duplicates.append(result[j])

		return [x for x in result if x not in duplicates]
	#limits the amount of branches per depth. May need to work more on this one
	def set_branches(self, result, covered_symbols):
		temp=[]
		temp2=[]
		symbol=None
		cor_symbol_lst=[]

		result=sorted(sorted(result, key=operator.itemgetter('score'), reverse=True), 
			key=operator.itemgetter('root_symbol', 'depth'))
		for i in range(len(result)):
			if symbol!=result[i]['root_symbol']:
				symbol=result[i]['root_symbol']
				temp[:]=[]
				count=0
				for item in result:
					if ((item['root_symbol'] == symbol or item['cor_symbol'] == symbol) and
						item['cor_symbol'] not in covered_symbols and count<self.branches):
						if item['cor_symbol'] not in cor_symbol_lst:
							cor_symbol_lst.append(item['cor_symbol'])
							temp.append(item)
							count+=1

				temp2.extend(temp)

		return temp2

	#limits amount of nodes by only displaying the top n nodes, prioritizing lower levels of depth
	def set_nodes(self):
		self.result = sorted(sorted(self.result, key=operator.itemgetter('score'), reverse=True), 
			key=operator.itemgetter('depth'))[:self.nodes]

	#used for saving the results locally
	def save_results(self, list, path, name):
		 timestring= time.strftime("%Y%m%d-%H%M%S")
		 full=path+timestring+"_"+name
		 with open(full, 'w') as outfile:
		 	json.dump(list, outfile, indent=2)

	#checks whether the dataset is a .csv or .tsv to provide the proper delimiter
	def check_filetype(self, filename):
		delim= None
		if filename[-4:]=='.csv':
			return ','
		else:
			return '\t'
	#transposes the dataset with izip/zip. Checks Python version to make sure that the right zip is running
	def zipper(self, csv):
		if sys.version_info[0] < 3:
			from itertools import izip
			return izip(*csv)
		else:
			return zip(*csv)


	"""def write_labels(filename):
		with open(filename) as file:
			delim=check_filetype(filename)

			column_csv = csv.reader(file, delimiter=delim)
			index_csv=None

			columns = next(column_csv)[1:]
			filename=filename.split('/', 1)[-1]
			filename=filename[:-4]
			with open("labels/column_labels_"+filename+".txt", 'w') as column_file:
				column_file.writelines("%s\n" % column for column in columns)

			index_csv=zipper(column_csv)

			rows = next(index_csv)[1:]
			with open("labels/row_labels_"+filename+".txt", 'w') as index_file:
				index_file.writelines("%s\n" % row for row in rows)
			print('*****')
			print('Labels saved to "row_labels_'+filename+'.txt" and "column_labels_'+filename+'.txt" in the folder "labels"')
			print('*****')
			os._exit(1)"""
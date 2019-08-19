class Solution:
	def lengthLongestPath(self, input):
		# 2 pointer approach
		def advance(ptr, input):
			level = 0
			while ptr < len(input) and input[ptr] != '\n':
				if input[ptr] == '\t':
					level += 1
				ptr += 1
			return level,ptr
		stack = []
		begin = 0
		num_tab = 0
		max_length = 0
		while begin < len(input):
			# advance till the next '\n'
			num_tab,end = advance(begin,input)
			# walk up the directory tree, if necessary
			while len(stack) > num_tab:
				stack.pop()
			# dir/file string length
			length = end-begin-num_tab
			if stack:
				length += 1 # add 1 for delimiter '\'
			# is this a file or dir?
			if '.' in input[begin:end]:
				max_length = max(max_length, sum(stack) + length)
			else:
				stack.append(length)
			# advance pointer to start from position after '\n'
			begin = end + 1
		return max_length

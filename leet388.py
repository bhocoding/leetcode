def lengthLongestPath(self, input):
	# 2 pointer approach
	def advance(begin, input):
		level = 0
		while begin < len(input) and input[begin] != '\n':
			if input[begin] == '\t':
				level += 1
			begin += 1
		return level,begin
	stack = []
	begin = 0
	level = 0
	max_length = 0
	while begin < len(input):
		# advance till the next '\n'
		level,end = advance(begin,input)
		# walk up the directory tree
		while len(stack) > level:
			stack.pop()
		# dir or file string length
		length = end-begin-level
		if stack:
			length += 1 # add 1 for delimiter '\'
		# if file calculate path length, else add to path
		if '.' in input[begin:end]:
			max_length = max(max_length, sum(stack) + length)
		else:
			stack.append(length)
		# advance pointer to start from position after '\n'
		begin = end + 1
	return max_length

def arithmetic_arranger(problems, answers=False):
	print(problems)
	if len(problems) > 5:
		arranged_problems = "Error: Too many problems."
	else:
		arranged_problems = ""
		total_first_operand = []
		total_second_operand = []
		total_answers = []
		operations_list = []
		#value extraction
		for x in problems:
			operation = x.split(" ")[1]
			problem_first_op = x.split(" " + operation + " ")[0]
			problem_second_op = x.split(" " + operation + " ")[1]
			if operation != "+" and operation != "-":
				arranged_problems = "Error: Operator must be '+' or '-'."
				break
			elif problem_first_op.isnumeric() == False or problem_second_op.isnumeric() == False:
				arranged_problems = "Error: Numbers must only contain digits."
				break
			elif len(problem_first_op) > 4 or len(problem_second_op) > 4:
				arranged_problems = "Error: Numbers cannot be more than four digits."
				break
			else:
				operations_list.append(operation)
				total_first_operand.append(problem_first_op)
				total_second_operand.append(problem_second_op)
				if answers:
					if operation == "+":
						total_answers.append(int(problem_first_op)+int(problem_second_op))
					else:
						total_answers.append(int(problem_first_op)-int(problem_second_op))
		
		if arranged_problems == "":
			max_length = [] #find length
			for x in range(len(problems)):
				if len(total_second_operand[x]) > len(total_first_operand[x]):
					max_length.append(len(total_second_operand[x]))
				else:
					max_length.append(len(total_first_operand[x]))

			#writing
			
			for x in range(len(problems)): #first operand
				arranged_problems += (" "*(max_length[x]-len(total_first_operand[x])+2))
				arranged_problems += total_first_operand[x]
				if x != (len(problems)-1): #only adds spaces if its still not the last part
					arranged_problems += " " * 4
			
			arranged_problems += "\n" #new line
			
			for x in range(len(problems)): #second operand
				arranged_problems += operations_list[x]
				arranged_problems += (" "*(max_length[x]-len(total_second_operand[x])+1))
				arranged_problems += total_second_operand[x]
				if x != (len(problems)-1): #only adds spaces if its still not the last part
					arranged_problems += " " * 4

			arranged_problems += "\n" #new line
			
			for x in range(len(problems)): #dashes
				arranged_problems += "-"*(max_length[x]+2)
				if x != (len(problems)-1): #only adds spaces if its still not the last part
					arranged_problems += " " * 4
			
			if answers:
				arranged_problems += "\n" #new line
				for x in range(len(problems)): #answers 
					length_answer = len(str(total_answers[x]))
					arranged_problems += (" "*(max_length[x]-length_answer+2))
					arranged_problems += str(total_answers[x])
					if x != (len(problems)-1): #only adds spaces if its still not the last part
						arranged_problems += " " * 4

	return arranged_problems
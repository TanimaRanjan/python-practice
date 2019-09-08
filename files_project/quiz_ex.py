"""
sample `questions.txt` file:
1+1=2
2+2=4
8-4=4
task description:
- read from `questions.txt`
- for each question, print out the question and and wait for the user's answer
    for example, for the first question, print out: `1+1=`
- after the user answers all the questions, calculate her score and write it to the `result.txt` file
    the result should be in such format: `Your final score is n/m.`
    where n and m are the number of correct answers and the maximum score respectively
"""
# your code starts here:

questions = open('questions.txt', 'r')

question = [line.strip() for line in questions]

questions.close();

print(question)
ques_ans = []

for ques in question:
    ques_ans.append(ques.split('='))

print(ques_ans)


print('Answer the following questions -- ')

answers = []
temp_ans =''
result = 0
for q_a in ques_ans:
    temp_ans = input(f'{q_a[0]} : ')
    if temp_ans == q_a[1]:
        answers.append(temp_ans)
        result = result + 1


ans_file = open('results.txt', 'w')
# for ans in answers:
#     ans_file.write(f'{ans}\n')

ans_file.write(f'Your final score is {result}/{len(question)}')

ans_file.close()




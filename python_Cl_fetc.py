import subprocess
import os

usernames = ['niketg', 'vipinsahu', 'kkharat', 'dasore']

cl_number = []
created_on = []
owner = []
status = []
comment = []



def ind_user():
	print('Available users: ')
	print('\n\u001b[1m')
	for value in usernames:
		print (value)
	print('\n\u001b[0m')
	for_user = input('Please enter an username: ')
	
	subprocess.call(f'clsearch a:{for_user} status:pending > temp.txt', shell=True)

	with open('temp.txt', 'r') as cls:
		text = cls.read()
		splitter = text.split('\n')
		splitter = splitter[:-1]	
		cls.close()

	for value in splitter:
		 cl_num = value.split(' ')[0]
		 cl_number.append(cl_num)
	#	 print(cl_num)

		 created_date = value.split(' ')[2]
		 created_on.append(created_date)
	#	 print(created_date)		 

		 own = value.split(' ')[4]
		 own = own.split('@')[0]
		 owner.append(own)
	#	 print(owner)

		 stat = value.split(' ')[5]
		 status.append(stat)
	#	 print(stat)

		 com = value.split("'")[1]
		 comment.append(com)
	#	 print(com)
		 
		 print(f'{cl_num}, {created_date}, {own}, {stat}, {com}')
	with open(f'cls_for_{for_user}.csv', 'w') as fi:
		i = 0
		fi.write('CL Number,Created on, Owner, Status, Comment' + '\n')
		for i in range(len(cl_number)):
			fi.write(cl_number[i] + ',' + created_on[i] + ',' + owner[i] + ',' + status[i] + ',' + comment[i] + '\n')
		fi.close()
	print('\n')
	print(f'\u001b[1mPending CL data for [{for_user}] is saved in \033[1;32mcls_for_{for_user}.csv\033[0m\u001b[0m')
	print('                                   ')
	os.remove('temp.txt')


def all_users():
	for data in usernames:
		subprocess.call(f'clsearch a:{data} status:pending > {data}.txt', shell=True)
		with open(f'{data}.txt', 'r') as cls:
			text = cls.read()
			splitter = text.split('\n')
			splitter = splitter[:-1]	
			cls.close()

		for value in splitter:
			 cl_num = value.split(' ')[0]
			 cl_number.append(cl_num)
		#	 print(cl_num)

			 created_date = value.split(' ')[2]
			 created_on.append(created_date)
		#	 print(created_date)		 

			 own = value.split(' ')[4]
			 own = own.split('@')[0]
			 owner.append(own)
		#	 print(owner)

			 stat = value.split(' ')[5]
			 status.append(stat)
		#	 print(stat)

			 com = value.split("'")[1]
			 comment.append(com)
		#	 print(com)
			
			 print(f'{cl_num}, {created_date}, {own}, {stat}, {com}')

		with open(f'cls_for_all_users.csv', 'w+') as fi:
			i = 0
			fi.write('CL Number,Created on, Owner, Status, Comment' + '\n')
			for i in range(len(cl_number)):
				fi.write(cl_number[i] + ',' + created_on[i] + ',' + owner[i] + ',' + status[i] + ',' + comment[i] + '\n')
			fi.close()

		os.remove(f'{data}.txt')
	print('\n')
	print(f'\u001b[1mPending CL data for all users is saved in \033[1;32mcls_for_all_users.csv\033[0m\u001b[0m')
	print('                                   ')

def start():
	print('                                   ')
	print(r'''
	 ╔═╗╦═╗╔═╗╦ ╦╔╦╗╦ ╦╦  ╔═╗╔╗   ╔╦╗╔═╗╔═╗╦  ╔═╗
 	 ║ ╦╠╦╝║ ║║║║ ║ ╠═╣║  ╠═╣╠╩╗   ║ ║ ║║ ║║  ╚═╗
	 ╚═╝╩╚═╚═╝╚╩╝ ╩ ╩ ╩╩═╝╩ ╩╚═╝   ╩ ╚═╝╚═╝╩═╝╚═╝
	''')
	print(' 	      Developed By: Pushkar Jadhav')
	print('               <\u001b[4mpushkarjadhav@google.com\u001b[0m>')
	print('                                   ')
	print('\u001b[1m	1. Fetch Pending CL data for INDIVIDUAL user.')
	print('	2. Fetch Pending CL data for ALL users.')
	print('	3. Exit\u001b[0m')
	print('                                   ')
	ch = int(input('Please enter your choice: '))
	print('                                   ')
	
	if ch == 1:
		ind_user()
	if ch == 2:
		all_users()
	if ch == 3:
		pass
		
if __name__ == "__main__":
	start()
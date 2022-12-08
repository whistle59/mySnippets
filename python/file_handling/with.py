# https://www.geeksforgeeks.org/with-statement-in-python/


# file handling without with
###########################

# 1) without using with statement
file = open('file_path', 'w')
file.write('hello world !')
file.close()
 
# 2) without using with statement
file = open('file_path', 'w')
try:
    file.write('hello world')
finally:
    file.close()
    
# Same example using with
# #######################
# with statement ensures that a resource is properly released 
# when the code using the resource is completely executed. 

with open('file_path', 'w') as file:
	file.write('hello world !')

'''
Day 3: Rename Database
1. Rename database 'project' to 'mydatabase' using ALTER DATABASE statement
2. Rename database 'mydatabase' back to 'project' again using RENAME DATABASE statement

Verify your changes by listing databases after you run the query
'''

# Mysql doesnot support Rename database using Alter database statement
# The RENAME DATABASE statement was deprecated and removed in MySQL 5.1.23 
# due to risks of data loss.
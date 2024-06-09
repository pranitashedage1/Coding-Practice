'''
Your Amazonian team is responsible for maintaining a monetary transaction service. The transactions are tracked in a log file.

A log file is provided as a string array where each entry represents a transaction to service. Each transaction consists of:

sender user id: Unique identifier for the user that initiated the transaction. It consists of only digits with at most 9 digits.
recipient user id: Unique identifier for the user that is receiving the transaction. It consists of onlv digits with at most 9 digits
amount of transaction: The amount of the transaction It consists of only digits with at most 9 digits
The values are separated by a soace. For example. "sender user id recipient user_id amount of_transaction".

Users that perform an excessive amount of transactions might be abusing the service so you have been tasked to identify the users 
that have a number of transactions over a threshold. 
The list of user ids should be ordered in ascending numeric value

size n = 4;
logs[] = ["1 2 50", "1 7 70", "1 3 20", "2 2 17"]
threshold = 2
Ouput:
1
2

size n = 4;
logs[] = ["9 7 50", "22 7 20", "33 7 50", "22 7 30"]
threshold = 3
'''
def logsfunction(logs, threshold):
    # log_entries = [s.split(',') for s in logs]
    result = {}
    test = []
    logs_entries = [(entry[0].split(' ')) for entry in [s.split(',') for s in logs]]
    print("log entries", logs_entries)
    for log in logs_entries:
        log.pop() 
        if log[0] == log[1]:
            log.pop()

    for logs in logs_entries:
        for log in logs:
            if log not in result:
                result[log] = 1
            else:
                result[log] = result.get(log) + 1
            if log not in test and result[log] >= threshold:
                test.append(log)
    # print(logs_entries)
    # print(result)
    test.sort()
    return test

logs = ["1 2 50", "1 7 70", "1 3 20", "2 2 17"]
threshold = 2
# logs = ["9 7 50", "22 7 20", "33 7 50", "22 7 30"]
# threshold = 3
a = logsfunction(logs, threshold)
print(a)

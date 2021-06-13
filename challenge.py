#Maximize reward and minimize weight

import csv

txid = []
fees = []
weights = []
parents = []

count = 0
flag = 0
current_weight = 0


def delete_from_list(i):
    fees.pop(i)
    weights.pop(i)
    txid.pop(i)
    parents.pop(i)

##Read the CSV file and append the data in the lists
with open('mempool.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        if count>=1:
            txid.append(row[0])
            fees.append(int(row[1]))
            weights.append(int(row[2]))
            parents.append(row[3])
        count=count+1



while len(fees)>0:
    while True:
        #Finding the transaction with the maximum fees
        max_index = fees.index(max(fees))      
        current_weight = current_weight + weights[max_index]
        #Check if the weight is within the limits
        if current_weight > 4000000:
            break
        else:
            #Checking if the transaction has any parent transaction
            if len(parents[max_index])>0:
                for i in parents[max_index].split(';'):
                    #Finding all the indices of the transaction who have the same parent transaction
                    find_index = [k for k,x in enumerate(txid) if x==i]
                    print(find_index)
                    for j in find_index:
                        current_weight = current_weight + weights[j]
                        if current_weight > 4000000:
                            flag=1
                            break
                    if flag==1:
                        break
                #Write to the TXT file and delete the record from the list    
                if flag==0:
                    for m in parents[max_index].split(';'):
                        find_index = [k for k,x in enumerate(txid) if x==m]
                        block_file = open("Block.txt","a")
                        for z in find_index:
                            block_file.write(txid[z] + "\n") 
                            delete_from_list(z)
        
        #Write to CSV file and delete the record from the list - For the maximum value
        block_file = open("Block.txt","a")
        block_file.write(txid[max_index] + "\n")
        delete_from_list(max_index)
        flag = 0

    current_weight = 0
    flag = 0
    block_file = open("Block.txt","a")
    block_file.write("##### NEXT BLOCK #####\n")

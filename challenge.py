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


with open('mempool.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        if count>=1:
            txid.append(row[0])
            fees.append(int(row[1]))
            weights.append(int(row[2]))
            parents.append(row[3])
        count=count+1

# if not fees:
#     if current_weight < 4000000:
#         max_index = fees.index(max(fees))
#         current_weight = current_weight + weights[max_index]
#         if not parents[max_index]:
#             for i in parents[max_index].split(';'):
#                 find_index = txid.index(i)
#                 current_weight = current_weight + weights[find_index]    

    
#     current_weight = 0


while len(fees)>0:

    while True:
        max_index = fees.index(max(fees))
        current_weight = current_weight + weights[max_index]
        if current_weight > 4000000:
            break
        else:
            if len(parents[max_index])>0:
                for i in parents[max_index].split(';'):
                    find_index = txid.index(i)
                    current_weight = current_weight + weights[find_index]
                    if current_weight > 4000000:
                        flag=1
                        break
                if flag==0:
                    for i in parents[max_index].split(';'):
                        find_index = txid.index(i)
                        block_file = open("Block.txt","a")
                        block_file.write(i + "\n") 
                        delete_from_list(find_index)
        
        block_file = open("Block.txt","a")
        block_file.write(txid[max_index] + "\n")
        delete_from_list(max_index)
        flag = 0

    current_weight = 0
    flag = 0
    block_file = open("Block.txt","a")
    block_file.write("##### NEXT BLOCK #####\n")

            

# findindex = txid.index("5c05321ac828925a32432290c7399eef4af2e153a480ed8fdfc761862f28a6eb")
# print(findindex)
# print(parents[findindex])
# print(txid[max_index])
# print(fees[max_index])
# print(weights[max_index])
# print(parents[max_index])

# fees.pop(max_index)
# print(txid[1])
# print(fees[1])
# print(weights[1])
# print(parents[1])
# print("Find index")

# print(txid[1])
# print(fees[1])
# print(weights[1])


# for i in parents[1].split(';'):
#     print(i)

# max_index = fees.index(max(fees))

# print(txid[max_index])
# print(fees[max_index])
# print(weights[max_index])
# print(parents[max_index])
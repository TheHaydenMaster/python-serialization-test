import pickle                                                                   #Import nessicary libraries

wallets = {'John': 100, 'George': 75}                                           #Creates a list of Users with a corresponding integer that is their money

serialize_wallets = pickle.dumps(wallets)                                       #Serializes the list

load_wallets = pickle.loads(serialize_wallets)                                  #Loads the wallets through the filehandler assigned in line 5

print(str(load_wallets['John']))                                                #Prints the value of John's wallet loaded through pickle

import numpy as np

#The function below return the test set from a bootsrap sample by taking as a parameter the sample and the original data set
#and returning an array with observations from the origial set that did not occurs on the bootstrap sample
def split_Samples(bootsrap_sample, origin_data_set):#bootsrap_sample have the same shape as origin_data_set
    data_size=len(bootsrap_sample)
    test_indexes, train_indexes=[], []
    for i in range(data_size):
        occurences_i=[]
        for j in range(data_size):
            if np.equal(origin_data_set[i,:], bootsrap_sample[j,:]).all():
                occurences_i.append(j)
        if len(occurences_i)==0:
            test_indexes.append(i)
        else:
            train_indexes.append(i)
    return np.take(origin_data_set, train_indexes, axis=0), np.take(origin_data_set, test_indexes, axis=0)

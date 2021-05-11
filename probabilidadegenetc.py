

def hamming_b (str1, str2):
    conta=0
    for i in range(len(str1)):
        if str1[i]!=str2[i]:
            conta=conta+1
    return conta

if __name__ == "__main__":


    large_dataset = open('sa.txt').read()

    str1, str2 = large_dataset.split()
    dist = hamming_b (str1, str2)

    print (dist)
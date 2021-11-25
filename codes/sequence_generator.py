#sequence generator

seq = "GGAUCCCUCACUUACUAGUCUGCAGAAGGAGAUAUACCCAUGG"
new_seq=[]
arr="AUGC"

for i in range (0, len(seq)):
	if seq[i]==arr[0]:
		new_seq.append(seq[:i]+arr[1]+seq[i+1:])
		new_seq.append(seq[:i]+arr[2]+seq[i+1:])
		new_seq.append(seq[:i]+arr[3]+seq[i+1:])
	elif seq[i]==arr[1]:
		new_seq.append(seq[:i]+arr[0]+seq[i+1:])
		new_seq.append(seq[:i]+arr[2]+seq[i+1:])
		new_seq.append(seq[:i]+arr[3]+seq[i+1:])
	elif seq[i]==arr[2]:
		new_seq.append(seq[:i]+arr[0]+seq[i+1:])
		new_seq.append(seq[:i]+arr[1]+seq[i+1:])
		new_seq.append(seq[:i]+arr[3]+seq[i+1:])
	elif seq[i]==arr[3]:
		new_seq.append(seq[:i]+arr[0]+seq[i+1:])
		new_seq.append(seq[:i]+arr[1]+seq[i+1:])
		new_seq.append(seq[:i]+arr[2]+seq[i+1:])

file=open("sequences.txt","w")
for x in new_seq:
	file.write(x)
	file.write('\n')

f=open("geo_ref.txt","r")
new_dict={}
i=0
for line in f:
    i=i+1
    if i>1:
        splitline=line.split()
        for i in range(9,4,-1):
            part_key=splitline[0][0:i]
            new_dict[part_key]=",".join(splitline[1:])
print (new_dict.keys())
f1=open("geo_impute.txt","r")
with open("geo_out.txt","w") as f1_out:
    i=0
    for line in f1:
       i=i+1
       if i==1:
           f1_out.write(line)
       if i>1:
           eachline=line.strip("\n").split()
           if eachline[1]==".":
               for j in range(9,4,-1):
                   if eachline[0][0:j] in new_dict.keys():
                      eachline[1]=new_dict[eachline[0][0:j]]
                      f1_out.write(eachline[0]+" "+eachline[1]+"\n")
                      break
           else:
               f1_out.write(eachline[0]+" "+eachline[1]+"\n")
f1_out.close()


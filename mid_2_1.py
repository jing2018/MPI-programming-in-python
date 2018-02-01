from mpi4py import MPI
comm = MPI.COMM_WORLD

size = comm.Get_size()
rank = comm.Get_rank()

if rank == 0:
   data = [(i)**2 for i in range(1,2**26+1)]
   chunk = [data[i:i+len(data)/size] for i in range(0,len(data),len(data)/size)]
else:
   newdata = None
   chunk = None

#Scatter Data
newdata = comm.scatter(chunk, root=0) 
sum = 0
for x in newdata:
     sum = sum+x


reducedSum = comm.reduce(sum, op=MPI.SUM, root=0) 

if rank == 0:
        print reducedSum 



from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
stat = MPI.Status()

message = rank
#print "Before Gather ",rank, message

message = comm.gather(message, root=0)

if rank == 0:
        print "size= ", max(message)+1


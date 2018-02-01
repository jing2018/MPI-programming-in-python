
from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
stat = MPI.Status()

message = rank**2
print "Before Gather ",rank, message

comm.Barrier()
message = comm.gather(message, root=0)

if rank == 0:

	print "After Gather ",rank,message

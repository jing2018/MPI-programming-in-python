from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
stat = MPI.Status()
	
if rank<size-1:
	if rank%2 == 0:
		if rank == size -2:
			destination = 1
		else:
			destination = rank +2
	else:
		destination = rank + 2
	message = "I am a message from rank %s" % rank
	comm.send(message, dest=destination)

if rank!=0:	

	incoming_message = comm.recv(source=MPI.ANY_SOURCE, status=stat)
	sender = stat.Get_source()

	print "Rank: %d\tSender: %d\tMessage: %s" % (rank,sender,incoming_message)



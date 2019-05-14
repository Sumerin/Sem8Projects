#include <stdio.h>
#include <mpi/mpi.h>
#include <time.h>

#define  L 100000
#define  R 600000
#define  N 10
#define  COUNT ((R - L) / N)


//#define SHOW_DEBUG
#define SHOW_RESULT

int IsPrime(int a)
{
    for (int i = 2; i < a; ++i)
    {
        if (a % i == 0)
        {
            return 0;
        }
    }
    return 1;
}

void fullfill_data(int package_count, int *out)
{
    for (int i = 0; i < N; ++i)
    {
        out[i] = L + (package_count * N) + i;
    }
}

void master_work(int myrank, int proccount)
{
    int package_count = 0;
    int recv_package_count = 0;
    int *buffer = new int[proccount];
    int buffer2[N];
    int number_of_primes = 0;
    int requestCompleted;
    MPI_Status status;
    MPI_Request *sRequest = new MPI_Request[proccount];
    MPI_Request *recvRequest = new MPI_Request[proccount];
    int i;
    int j;

    for (i = 1; i < proccount; ++i)
    {
#ifdef SHOW_DEBUG
        printf("init send to %d\n", i);
#endif
        fullfill_data(package_count, buffer2);
#ifdef SHOW_DEBUG
        printf("send 0\n");
#endif
        MPI_Send(buffer2, N, MPI_INT, i, package_count, MPI_COMM_WORLD);
        package_count++;

        fullfill_data(package_count, buffer2);
        MPI_Isend(buffer2, N, MPI_INT, i, package_count, MPI_COMM_WORLD, &sRequest[i]);
        package_count++;

#ifdef SHOW_DEBUG
        printf("init send end to %d\n", i);
#endif
    }

    for (j = 0; j < proccount; ++j)
    {
        recvRequest[j] = MPI_REQUEST_NULL;
    }

    for (j = 1; j < proccount; ++j)
    {
        recvRequest[j] = MPI_REQUEST_NULL;
#ifdef SHOW_DEBUG
        printf("init receive %d\n", j);
#endif
        MPI_Irecv(&(buffer[j]), 1, MPI_INT, j, MPI_ANY_TAG, MPI_COMM_WORLD, &(recvRequest[j]));
    }

    while (package_count < COUNT)
    {
        MPI_Waitany(proccount , recvRequest, &requestCompleted, &status);
        recv_package_count++;

        number_of_primes += buffer[requestCompleted];

        fullfill_data(package_count, buffer2);
#ifdef SHOW_DEBUG
        printf("send data to %d\n", requestCompleted);
#endif
        MPI_Isend(buffer2, N, MPI_INT, status.MPI_SOURCE, package_count, MPI_COMM_WORLD, &sRequest[status.MPI_SOURCE]);
        package_count++;

        MPI_Irecv(&(buffer[requestCompleted]), 1, MPI_INT, requestCompleted, MPI_ANY_TAG, MPI_COMM_WORLD,
                  &(recvRequest[requestCompleted]));
    }

#ifdef SHOW_DEBUG
    printf("##############End of data##########\n");
#endif

    while (recv_package_count < COUNT)
    {
        MPI_Waitany(proccount, recvRequest, &requestCompleted, &status);
        recv_package_count++;

        number_of_primes += buffer[requestCompleted];
#ifdef SHOW_DEBUG

        printf("package: %d out of %d\n", recv_package_count, COUNT);
        printf("send end to %d\n", requestCompleted);
#endif
        MPI_Isend(buffer2, N, MPI_INT, status.MPI_SOURCE, COUNT, MPI_COMM_WORLD,
                  &sRequest[status.MPI_SOURCE]);//end task
        MPI_Irecv(&(buffer[requestCompleted]), 1, MPI_INT, requestCompleted, MPI_ANY_TAG, MPI_COMM_WORLD,
                  &(recvRequest[requestCompleted]));
    }

#ifdef SHOW_RESULT
    printf("Primes: %d\n", number_of_primes);
#endif
    delete[] sRequest;
    delete[] buffer;

}

void slave_work(int myrank, int proccount)
{
    int *buffer = new int[N];
    int *buffer2 = new int[N];
    int result;
    int *tmp;
    int t;

    MPI_Status status;
    MPI_Request recvRequest;
    MPI_Request sRequest;

#ifdef SHOW_DEBUG
    printf("[%d]rec start \n", myrank);
#endif
    MPI_Recv(buffer, N, MPI_INT, 0, MPI_ANY_TAG, MPI_COMM_WORLD, &status);
    clock_t start = clock();
    clock_t stop = 0;
    t = 0;
    while (status.MPI_TAG < COUNT)
    {
        t++;
#ifdef SHOW_DEBUG
        printf("[%d] buffer %d  buffer2 %d\n", myrank, buffer, buffer2);
        printf("[%d] buffer %d %d  buffer2 %d %d\n", myrank, buffer[0], buffer[1], buffer2[0], buffer2[1]);
#endif
        MPI_Irecv(buffer2, N, MPI_INT, 0, MPI_ANY_TAG, MPI_COMM_WORLD, &recvRequest);
        result = 0;
        for (int i = 0; i < N; ++i)
        {
            result += IsPrime(buffer[i]);
        }

#ifdef SHOW_DEBUG
        printf("[%d]send data to master\n", myrank);
#endif
        MPI_Isend(&result, 1, MPI_INT, 0, status.MPI_TAG, MPI_COMM_WORLD, &sRequest);

#ifdef SHOW_DEBUG
        printf("[%d]wait for data\n", myrank);
#endif
        MPI_Wait(&recvRequest, &status);

        tmp = buffer;
        buffer = buffer2;
        buffer2 = tmp;

    }
#ifdef SHOW_RESULT
    stop = clock();
    printf("rank: %d mean: %f\n", myrank, (stop - start)*1.0/t);
#endif
    delete[] buffer;
    delete[] buffer2;
}

int main(int argc, char **argv)
{

    int myrank, proccount;
    // Initialize MPI
    MPI_Init(&argc, &argv);
    // find out my rank
    MPI_Comm_rank(MPI_COMM_WORLD, &myrank);
    // find out the number of processes in MPI_COMM_WORLD
    MPI_Comm_size(MPI_COMM_WORLD, &proccount);

    if (!myrank)
    {
#ifdef SHOW_DEBUG
        printf("Number of process: %d Count %d \n", proccount, COUNT);
#endif
        master_work(myrank, proccount);
    } else
    {
        slave_work(myrank, proccount);
    }

    MPI_Finalize();
    return 0;
}
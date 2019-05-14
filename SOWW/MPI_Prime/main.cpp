#include <stdio.h>
#include <mpi/mpi.h>

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
        out[i] =  L + (package_count * N) + i;
    }
}

void master_work(int myrank, int proccount)
{
    int package_count = 0;
    int recv_package_count = 0;
    int buffer;
    int buffer2[N];
    int number_of_primes = 0;
    MPI_Status status;
    int i;

    for (i = 1; i < proccount; ++i)
    {
#ifdef SHOW_DEBUG
        printf("init send to %d\n", i);
#endif
        fullfill_data(package_count, buffer2);
        MPI_Send(buffer2, N, MPI_INT, i, package_count, MPI_COMM_WORLD);
        package_count++;
#ifdef SHOW_DEBUG
        printf("init send end to %d\n", i);
#endif
    }

    while (package_count < COUNT)
    {
        MPI_Recv(&buffer, 1, MPI_INT, MPI_ANY_SOURCE, MPI_ANY_TAG, MPI_COMM_WORLD, &status);
        recv_package_count++;

        number_of_primes += buffer;

        fullfill_data(package_count, buffer2);
        MPI_Send(buffer2, N, MPI_INT, status.MPI_SOURCE, package_count, MPI_COMM_WORLD);
        package_count++;
    }

    while (recv_package_count < COUNT)
    {
        MPI_Recv(&buffer, 1, MPI_INT, MPI_ANY_SOURCE, MPI_ANY_TAG, MPI_COMM_WORLD, &status);
        recv_package_count++;

        number_of_primes += buffer;

        MPI_Send(buffer2, N, MPI_INT, status.MPI_SOURCE, COUNT, MPI_COMM_WORLD);//end task
    }
#ifdef SHOW_RESULT
    printf("Primes: %d\n", number_of_primes);
#endif

}

void slave_work(int myrank, int proccount)
{
    int buffer[N];
    int result;
    int i;
    MPI_Status status;

    MPI_Recv(buffer, N, MPI_INT, 0, MPI_ANY_TAG, MPI_COMM_WORLD, &status);
    clock_t  start = clock();
    clock_t  stop = 0;
    int t = 0;
    while (status.MPI_TAG < COUNT)
    {
        t++;
        result = 0;
        for (i = 0; i < N; ++i)
        {
            result += IsPrime(buffer[i]);
        }

        MPI_Send(&result, 1, MPI_INT, 0, status.MPI_TAG, MPI_COMM_WORLD);

        MPI_Recv(buffer, N, MPI_INT, 0, MPI_ANY_TAG, MPI_COMM_WORLD, &status);
    }
#ifdef SHOW_RESULT
    stop = clock();
    printf("rank: %d mean: %f\n", myrank, (stop - start)*1.0/t);
#endif
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
'''
In modern operating systems, processes are independent instances of program execution and are made up of one or more threads. Processes are largely independent of each other and only interact through inter-process communication channels. In comparison, threads in the same process share almost all resources, including memory space and file descriptors. As a result, threads are generally faster to create and destroy and can communicate between each other more quickly than processes can. Because threads execute concurrently, each thread needs to maintain independent call stack with information about the current state of execution. The call stack holds local variables, the return address, and the enclosing context of the current operation. But because they share memory with other threads in the same process, threads must synchronize access to shared data to maintain data integrity.
'''

Which of the following statements about threads and processes is true?

Select the correct answer:

Multi-core processors can execute multiple processes simultaneously, but not multiple threads.


Threads in a process share the same address space, but have their own call stacks.


One thread can have many processes, but a process can only belong to one thread.


Multi-process programs are vulnerable to deadlock, but multi-threaded code is always lock-free.



# Answer: Threads in a process share the same address space, but have their own call stacks

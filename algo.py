import util

# Initialization of semaphores, init counter
mutex = util.Sem(1)
attente = util.Sem(0)
nb_att: int = 0
N = 4


def run(pid):
    global mutex
    global attente
    global nb_att
    global N

    mutex.p(pid)
    nb_att = 1 + nb_att
    if nb_att == N:
        print("process %s will release awaiting process below..." % pid)
        attente.print_list()

        for i in range(1, N):
            attente.v()
        nb_att = 0
        mutex.v()
    else:
        mutex.v()
        attente.p(pid)

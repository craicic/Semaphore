class Sem:
    k: int
    file: []

    def __init__(self, val):
        # mask IT
        self.k = val
        self.file = []
        # unmask IT

    def p(self, pid):
        # mask IT
        self.k = self.k - 1
        if self.k < 0:
            self.file.append(pid)
            print("process %s blocked" % pid)
        # unmask IT

    def v(self):
        # mask IT
        self.k = self.k + 1
        if self.k <= 0:
            print("process %s awakened" % self.file[0])
            self.file.pop(0)
        # unmask IT

    def print_list(self):
        print(self.file)

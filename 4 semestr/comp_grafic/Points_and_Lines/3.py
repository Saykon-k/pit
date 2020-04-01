class Line:
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C
    def __str__(self):
        for_pr_A = "%.2f" % (self.A)
        for_pr_B = "+ %.2f" % (self.B)
        for_pr_C = "+ %.2f" % (self.C)
        if self.A < 0:
            for_pr_A = "-" + for_pr_A
        if self.B < 0:
            for_pr_B = "-" + for_pr_B[1:len(for_pr_B)]
        if self.C < 0:
            for_pr_C = "-" + for_pr_C[1:len(for_pr_C)]
        return "{}x {}y {} = 0".format (for_pr_A, for_pr_B, for_pr_C)
L = Line(3, -5, 6)
# check __str__()
print(L)
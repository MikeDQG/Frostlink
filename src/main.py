import reporter


class Main():
    def __init__(self):
        self.reporter = reporter.Reporter()
        self.run()

    def run(self):
        self.reporter.main()


m = Main()
m.run()
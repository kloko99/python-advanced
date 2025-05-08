from abc import ABC, abstractmethod


class BasisWorker(ABC):
    """Abstrakte Basisklassen werden selber nicht instanziiert,
    sondern nur geerbt."""

    @abstractmethod
    def set_tools(self, tools): ...

    def show_tools(self):
        """Diese Methode muss nicht überschrieben werden, da sie keine
        abstractmethod ist."""
        for tool in self.tools:
            print(tool)


class SystemWorker(BasisWorker):
    """muss alle abstrakte Methoden von Basisworker überschreiben."""

    def set_tools(self, tools):
        """Konkrete Implementierung von set_tools."""
        self.tools = tools


class PipelineWorker(BasisWorker):
    def set_tools(self, tools):
        self.tools = tools


system_worker = SystemWorker()
system_worker.set_tools(["cleaner", "builder"])

pipeline_worker = PipelineWorker()
pipeline_worker.set_tools(["cleaner", "builder"])


def do_something(worker: BasisWorker):
    """Gegen Abstraktion implementieren und nicht gegen konkrete Implementierungen."""
    print(worker)


do_something(system_worker)

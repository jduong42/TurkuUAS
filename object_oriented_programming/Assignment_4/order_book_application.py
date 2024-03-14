class Task:
    id_counter = 1

    def __init__(self, description: str, programmer: str, workload: int):
        self.id = Task.id_counter
        Task.id_counter += 1
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.finished = False

    def is_finished(self):
        return self.finished

    def mark_finished(self):
        self.finished = True

    def __str__(self):
        status = "FINISHED" if self.finished else "NOT FINISHED"
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {status}"

class OrderBook:
    def __init__(self):
        self.orders = []
        self._programmers = set()

    def add_order(self, description: str, programmer: str, workload: int):
        task = Task(description, programmer, workload)
        self.orders.append(task)
        self._programmers.add(programmer)

    def all_orders(self):
        return self.orders

    def programmers(self):
        return list(self._programmers)
    
    def mark_finished(self, id: int):
        for order in self.orders:
            if order.id == id:
                order.mark_finished()
                return
        raise ValueError("No task with id {id} was found.")

    def finished_orders(self):
        return [order for order in self.orders if order.is_finished()]
    
    def unfinished_orders(self):
        return [order for order in self.orders if not order.is_finished()]

    def status_of_programmer(self, programmer: str):
        if programmer not in self._programmers:
            raise ValueError(f"No programmer {programmer} was found.")
        
        finished_tasks = [order for order in self.orders if order.is_finished() and order.programmer == programmer]
        unfinished_tasks = [order for order in self.orders if not order.is_finished() and order.programmer == programmer]
        finished_workload = sum([order.workload for order in finished_tasks])
        unfinished_workload = sum([order.workload for order in unfinished_tasks])

        return len(finished_tasks), len(unfinished_tasks), finished_workload, unfinished_workload
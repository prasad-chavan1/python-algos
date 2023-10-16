class Queue:
	def __init__(self, size):

		self.queue = []
		self.front = self.rear = 0
		self.size = size

	def enqueue(self, data):

		if(self.size == self.rear):
			print("\nOverflow")

		else:
			self.rear += 1
			self.queue.append(data)

	def dequeue(self):

		if(self.front == self.rear):
			print("Underflow")

		else:
			x = self.queue.pop(0)
			self.rear -= 1

	def printQueue(self):

		if(self.front == self.rear):
			print("\nQueue is Empty")

		for i in self.queue:
			print(i, " ", end='')


if __name__ == '__main__':

	q = Queue(4)

	q.printQueue()

	q.enqueue(20)
	q.enqueue(30)
	q.enqueue(40)
	q.enqueue(50)


	q.printQueue()


	q.enqueue(60)

	q.printQueue()

	q.dequeue()
	q.dequeue()
	print("\n\nafter two node deletion\n")

	q.printQueue()

class Job:
    def __init__ (self,task,profit,deadline):
        self.task=task
        self.profit=profit
        self.deadline=deadline
def scheduledjobs(jobs,T):
    slot=[-1]*T
    profit=0
    jobs.sort(key=lambda x:x.profit ,reverse=True)
    for job in jobs:
        for j in reversed(range(job.deadline)):
            if j<T and slot[j]==-1:
                slot[j]=job.task
                profit+=job.profit
                break
    print("Scheduled jobs are :",list(filter(lambda x:x!=-1,slot)))
    print("The total Profit :",profit)
    
if __name__=="__main__":
    jobs=[]
    n=int(input("Enter the number :"))
    for i in range(n):
        task=int(input(f"Enter the taskId of {i+1} : "))
        profit=int(input(f"Enter the profit of {i+1} : "))
        deadline=int(input(f"Enter the deadline of {i+1} : "))
        jobs.append(Job(task,profit,deadline))
    T=int(input("Enter the Timeline"))
    scheduledjobs(jobs,T)




# Enter the number :6
# Enter the taskId of 1 : 1
# Enter the profit of 1 : 200
# Enter the deadline of 1 : 2
# Enter the taskId of 2 : 2
# Enter the profit of 2 : 180
# Enter the deadline of 2 : 3
# Enter the taskId of 3 : 3
# Enter the profit of 3 : 120
# Enter the deadline of 3 : 2
# Enter the taskId of 4 : 4
# Enter the profit of 4 : 100
# Enter the deadline of 4 : 3
# Enter the taskId of 5 : 5
# Enter the profit of 5 : 50
# Enter the deadline of 5 : 4
# Enter the taskId of 6 : 6
# Enter the profit of 6 : 30
# Enter the deadline of 6 : 1
# Enter the Timeline4
# Scheduled jobs are : [3, 1, 2, 5]
# The total Profit : 550

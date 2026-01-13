
# Simple autonomous AI agent skeleton
def agent_loop(task):
    memory = []
    while True:
        action = decide(task, memory)
        result = execute(action)
        memory.append(result)
        if task_done(result):
            break

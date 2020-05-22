log_file = open('log', 'r', encoding='UTF8')
log_file = log_file.read()

print(log_file)

log_file = log_file.split('\n')
lg = list(map(lambda x: x.partition(',')[0], log_file))
lg.sort()

print()
print(f"Дата последнего лога: {lg[-1]}")



def snmp_collect(*args, **kwargs):
    print(args)
    if len(args) > 2:
        print("<<<<<<<1234<<<<<<<<<")
        print(args[1] + args[2])
    return '>>>>准备收集'


def print5(text):
    print(text)
    return str(text)


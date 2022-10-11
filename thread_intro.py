from threading import Thread, current_thread
print("#######################")
def display():
    print('current thread :___: -', current_thread)
    print('#####################')
    print('defualt')

t=Thread(target=display)
t.start()
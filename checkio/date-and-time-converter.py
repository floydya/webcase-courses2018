def date_time(time):
    month = [' January ', ' February ', ' March ', ' April ', ' May ', ' June ', ' July ', ' August ', ' September ', ' October ', ' November ', ' December ']
    time = time.replace('.', ' ')
    time = time.replace(':', ' ')
    nt = time.split(' ')
    chas = ' hours ' if int(nt[3]) != 1 else ' hour '
    minu = ' minutes' if int(nt[4]) != 1 else ' minute'
    return str(int(nt[0])) + month[int(nt[1])-1] + str(int(nt[2])) + ' year ' + str(int(nt[3])) + chas + str(int(nt[4])) + minu

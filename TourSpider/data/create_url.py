f_city = open('tuniu_start_city')
f_url = open('tuniu_end_city&url')
f_end = open('tuniu_url', 'w')


l_city = f_city.readlines()
l_url = f_url.readlines()
l_end = []

for s1 in l_city:
    for s2 in l_url:
        l_end.append(s2.replace('?', s1.strip()))

f_end.writelines(l_end)


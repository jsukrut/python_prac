def seq():
    no = 1
    while no <=30:
        sq = no * no
        yield sq
        no += 1

gen_obj = seq()
print(gen_obj)

for obj in gen_obj:
    print(obj)

# import random 
# from test import db
# base = {

# }

# io = db.users.get_all()


# for i in io:
#     base[i.number] = i.login
#     o = random.choice(list(base.items()))

# print(", ".join(o))








# # for i in io:
# #     base[i.number] = i.login
# #     data = list(base.items())
# #     key,val = data[random.randint(0, len(base)-1)]     
          
# # print(key,val)

from test import db

    # global output
io = db.items.get_all()
for i in io: 
    
    print()

    # for i in io:
    #     data[i.id] = i.login
    #     o = random.choice(list(data.items()))
    #     output = ", ".join(o)
    # return jsonify(output)


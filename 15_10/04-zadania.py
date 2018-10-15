import pickle

base = [{'id':1, 'first_name': 'Jphn', 'phone': [11111,2222]},
        {'id':2, 'first_name': 'Jphn', 'phone': [2222]}
        ]

with open('test_base.pickle', 'wb') as file:
    pickle.dump(base, file)
    pickle.dumps(base)

base_read = None
with open('test_base.pickle','rb') as file:
    base_read = pickle.load(file)
    print(base_read)
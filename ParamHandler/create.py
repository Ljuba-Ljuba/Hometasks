import pickle


with open ('./test.pickle', 'wb') as f:
    pickle.dump('1234', f)

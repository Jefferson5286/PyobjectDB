from pyobjectdb import database, create, obj

create('main.db', {
    'nomes': obj(keys={
        'nome1': 'Jefferson',
        'nome2': 'Mikaelly',
        'nome3': 'Python'
    }),

    'idades': obj(keys={
        'idade1': 17,
        'idade2': 14,
        'idade3': 32
    })
})

db = database('main.db')
db.connect()

print(db.query().nomes.convert())
print(db.query().idades.convert())

print(db.query().convert())

db.submit('peso', obj(keys={
    'var1': 50.0,
    'var2': 70.0,
    'var3': 14.0
}))

print(db.query().convert())

print(db.query().nomes.convert())

db.remove('peso')

print(db.query().convert())

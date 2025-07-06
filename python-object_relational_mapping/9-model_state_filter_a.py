#!/usr/bin/python3
"""Listeo all State objects that contain the letter 'a' from the database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Conexión a la base de datos
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    # Crear sesión
    Session = sessionmaker(bind=engine)
    session = Session()

    # Buscar estados que contengan 'a'
    states = session.query(State)\
        .filter(State.name.like('%a%'))\
        .order_by(State.id)\
        .all()

    # Mostrar resultados
    for state in states:
        print(f"{state.id}: {state.name}")

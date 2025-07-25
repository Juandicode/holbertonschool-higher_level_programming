#!/usr/bin/python3
"""listar  all State objects from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Crear engine de conexión a la base de datos
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    # Crear sesiónn
    Session = sessionmaker(bind=engine)
    session = Session()

    # Consultar todos los State ordenados por id
    states = session.query(State).order_by(State.id).all()

    # Mostrar resultados
    for state in states:
        print(f"{state.id}: {state.name}")

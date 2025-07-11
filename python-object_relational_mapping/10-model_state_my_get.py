#!/usr/bin/python3
"""Printeo el State object with the name passed as argument"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Conexión
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    # Crear sesión
    Session = sessionmaker(bind=engine)
    session = Session()

    # Buscar el estado por nombre (sin riesgo de SQL injection)
    state = session.query(State)\
        .filter(State.name == sys.argv[4])\
        .first()

    # Mostrar resultado
    if state:
        print(f"{state.id}")
    else:
        print("Not found")

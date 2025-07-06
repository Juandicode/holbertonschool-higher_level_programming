#!/usr/bin/python3
"""update the name of the State object con el id = 2"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Crear engine
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    # Crear sesión
    Session = sessionmaker(bind=engine)
    session = Session()

    # Buscar el estado con id = 2
    state = session.query(State).filter(State.id == 2).first()

    # Si existe, cambiar el nombre
    if state:
        state.name = "New Mexico"
        session.commit()

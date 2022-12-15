import db
from sqlalchemy.orm import sessionmaker
import random

# new session
Session = sessionmaker(bind=db.engine)
session = Session()

# adding random data
for t_id in range(10, 20):
    item_id = random.randint(0, 1000)
    price = random.randint(20, 50)

    tr = db.transactions(t_id, '2022/05/06', item_id, price)
    session.add(tr)

# Save changes to the database
session.commit()


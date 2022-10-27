import sys

from uuid import uuid4
from datetime import datetime

sys.path.append("..")
from models import db, DF_User


def start_application():
    db_query_addition()
    print("[NOTICE] Running Function=> [db_query_addition] Complete !")


def db_query_addition():
    df_user = DF_User(
        df_user_id=str(uuid4),
        df_user_name="ryan",
        df_user_pass="Ab-123456",
        df_user_mail="suigege23@163.com",
        df_user_phone="17306178678",
        df_user_address="Earth",
        df_user_gender="male"
    )
    db.session.add(df_user)
    db.session.commit()
    print("####################################################################################")
    print("[CONSOLE] DB Query Successfuly ! Please Check at DBeaver ^_^")
    print("####################################################################################")


def main():
    print("====================================================================================")
    print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    print("####################################################################################")
    start_application()
    print("####################################################################################")
    print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    print("====================================================================================")


if __name__ == '__main__':
    main()

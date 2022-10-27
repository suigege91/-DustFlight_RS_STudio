import sys

from uuid import uuid4
from datetime import datetime

sys.path.append("..")
from models import db, DF_User


def start_application():
    db_query_delete()
    print("[NOTICE] Running Function=> [db_query_delete] Complete !")


def db_query_delete():
    target_data = db.session.query(DF_User).filter_by(df_user_name='ryan').first()
    print("------------------------------------------------------------------------------------")
    print("[CONSOLE] Result_Target_Data => <[%s]>" % str(target_data))
    print("------------------------------------------------------------------------------------")
    db.session.delete(target_data)
    db.session.commit()
    print("####################################################################################")
    print("[CONSOLE] DB Query Delete Successfuly ! Please Check at DBeaver ^_^")
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

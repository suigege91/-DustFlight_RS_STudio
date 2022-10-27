import sys

from uuid import uuid4
from datetime import datetime

sys.path.append("..")
from models import db, DF_User


def start_application():
    db_query_uppdate()
    print("[NOTICE] Running Function=> [db_query_uppdate] Complete !")
    db_query_select_result_data_array()
    print("[NOTICE] Running Function=> [db_query_select_result_data_array] Complete !")


def db_query_uppdate():
    # target_data = db.session.query(DF_User).filter_by(DF_User.df_user_name == 'ryan').all()
    target_data = db.session.query(DF_User).first()
    print("------------------------------------------------------------------------------------")
    print("[CONSOLE] Result_Target_Data => <[%s]>" % str(target_data))
    print("------------------------------------------------------------------------------------")
    target_data = db.session.query(DF_User).update({"df_user_mail": "suigege23@163.com"})
    print("------------------------------------------------------------------------------------")
    print("[CONSOLE] Result_Target_Data => <[%s]>" % str(target_data))
    print("------------------------------------------------------------------------------------")
    db.session.commit()
    print("####################################################################################")
    print("[CONSOLE] DB Query Update Successfuly ! Please Check at DBeaver ^_^")
    print("####################################################################################")


def db_query_select_result_data_array():
    result_data_array = db.session.query(DF_User).order_by(DF_User.df_user_name).all()
    print("[CONSOLE] Result_Data => <[%s]>" % str(result_data_array))
    print("####################################################################################")
    print("[CONSOLE] DB Query Update Successfuly ! Please Check at DBeaver ^_^")
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

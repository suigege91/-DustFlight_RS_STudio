from flask import Blueprint

blueprint_name = "df_blog_application"
blueprint_url_prefix = "/df_blog_application"
blueprint_static_folder_path = "../Resource/static"
blueprint_template_folder_path = "../Resource/templates/DF_Blog_Application"

df_blog_application = Blueprint(blueprint_name, __name__, url_prefix=blueprint_url_prefix,
                                static_folder=blueprint_static_folder_path,
                                template_folder=blueprint_template_folder_path)

from . import handler

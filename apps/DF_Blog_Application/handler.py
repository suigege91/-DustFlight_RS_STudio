from . import df_blog_application


@df_blog_application.route("/")
@df_blog_application.route("/home")
@df_blog_application.route("/index")
@df_blog_application.route("/default")
def df_blog_application_index():
    return "<strong>[CONSOLE_OUTPUT] This is Module of DF_Blog_Application !</strong>"

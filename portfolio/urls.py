from django.urls import path
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from . import views

app_name = "portfolio"

urlpatterns = [
    # Dashboard + Holdings
    path("", views.dashboard, name="dashboard"),
    path("add/", views.add_holding, name="add_holding"),
    path("edit/<int:pk>/", views.edit_holding, name="edit_holding"),
    path("delete/<int:pk>/", views.delete_holding, name="delete_holding"),
    path("export_excel/", views.export_excel, name="export_excel"),

    # Auth
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("register/", views.register_view, name="register"),
    path("logout/", LogoutView.as_view(next_page="portfolio:login"), name="logout"),

    # ✅ Password Reset URLs
    path(
        "password_reset/",
        auth_views.PasswordResetView.as_view(
            template_name="portfolio/password_reset.html",
            email_template_name="portfolio/password_reset_email.html",  # 👈 create this
            success_url="/password_reset_done/"
        ),
        name="password_reset"
    ),
    path(
        "password_reset_done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="portfolio/password_reset_done.html"
        ),
        name="password_reset_done"
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="portfolio/password_reset_confirm.html",
            success_url="/reset/done/"
        ),
        name="password_reset_confirm"
    ),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="portfolio/password_reset_complete.html"
        ),
        name="password_reset_complete"
    ),
]

from django.urls import path, re_path
from faq import views
app_name = 'e_gov_faq'


urlpatterns = [
    path('e_faq/', views.e_faq, name='e_faq'),
    path('generate_faq/', views.generate_faq, name='generate_faq'),
    path('download_faq/', views.download_file, name='download_faq'),
]
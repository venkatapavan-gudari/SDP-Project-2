from django.urls import path
from .views import signup, login_view, logout_view, home, survey_create,survey_types,customersurvey,websitefeedback
urlpatterns = [

    path('', login_view, name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', logout_view, name='logout'),


    path('home/', home, name='home'),
    path('survey_create/', survey_create, name='survey_create'),
    path('survey-types/', survey_types, name='survey_types'),
    path('customersurvey/', customersurvey, name='customersurvey'),
    path('websitefeedback/', websitefeedback, name='websitefeedback'),

    #Add other URL patterns as needed
]

from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('info/', views.PersonalInformation_List.as_view()),
    path('info/<int:pk>', views.PersonalInformation_Details.as_view()),
    path('rest/', views.RenalFunctionTests_List.as_view()),
    path('rest/<int:pk>', views.RenalFunctionTests_Details.as_view())
]


urlpatterns = format_suffix_patterns(urlpatterns)
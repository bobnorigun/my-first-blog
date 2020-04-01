

# The main page is caldist/test. This is the gateway.
# If the user successfully enters two airport codes, okay
# Otherwise, he goes to caldist/fail
# the caldist/get_names is used for autocomplete

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .import views


app_name = 'caldist'
urlpatterns = [
	# 두 지점간 거리구하기 haversine
	path('', views.caldistview, name="imhere"),
	# main view of the app
	path('test/', views.formview, name="test"),
	#this is used for autocomplete
	path('get_names/', views.getnamesview, name="get_names"),
	#this view is activated when the user input-ed codes are not found
	path('fail/', views.failview, name="fail"),
]

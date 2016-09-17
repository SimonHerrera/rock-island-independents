from django.conf.urls import url, include
from rii_Api import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'games', views.GameList)
router.register(r'years', views.YearList)
router.register(r'players', views.PlayerList)
router.register(r'locations', views.LocationList)
router.register(r'opponents', views.OpponentList)
router.register(r'coaches', views.CoachList)
router.register(r'managers', views.ManagerList)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')) #allows logout
]

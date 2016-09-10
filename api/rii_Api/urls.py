from rest_framework import routers
from django.conf.urls import url, include
from rii_Api import views

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
]

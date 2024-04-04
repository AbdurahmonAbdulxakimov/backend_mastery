from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView

from l_celery.tasks import get_teams_task
from l_celery.models import Team
from l_celery.serializers import TeamSerializer


class TeamListAPIView(ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    # def get(self, request):
    #     get_teams_task.delay()
    #     return super().get(request)

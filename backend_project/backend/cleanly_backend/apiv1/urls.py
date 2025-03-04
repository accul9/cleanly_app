from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

router = DefaultRouter()  # ルータを作成
router.register(r"tasks", TaskViewSet, basename="task")  # ルータにviewsetを登録
# 引数1のr"tasks"はraw stringでURLのプレフィクスを指定。
# 引数2のTaskViewSetはviewsetのクラスを指定。
# 引数3のbasename="tasks"はURLの名称空間を指定。モデルまたは、クエリセット属性がない場合、指定する必要がある。

# ルータで作成したURLをincludeで追加
app_name = "tasks"
urlpatterns = [
    path("tasks/", include(router.urls)),
]

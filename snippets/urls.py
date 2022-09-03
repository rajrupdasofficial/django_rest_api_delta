from django.urls import path
#from  .views import snippet_list,snippet_detail
from snippets import views
urlpatterns = [
        #path('snippets/',snippet_list),
        #path('snippets/<int:pk>',snippet_detail)
        path('snippets/', views.SnippetList.as_view()),
        path('snippets/<int:pk>/', views.SnippetDetail.as_view()),

]


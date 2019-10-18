"""untitled2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from MyEva import views



urlpatterns = [
   path('index/',views.index,name="index"),
   path('login/',views.login,name="login"),
   path('register/',views.register,name="register"),
   path('indexandmethod/',views.indexandmethod,name="indexandmethod"),
   path('newBlankEva/',views.newBlankEva,name="newBlankEva"),
   path('newEva/',views.newEva,name="newEva"),
   path('addQNaire/',views.addQNaire,name="addQNaire"),
   path('chooseEva/',views.chooseEva,name="chooseEva"),
   path('getFillAssess/',views.getFillAssess,name="getFillAssess"),
   path('FillQNaire/',views.FillQNaire,name="FillQNaire"),
   path('deleteAssess/',views.deleteAssess,name="deleteAssess"),
   path('AnalysisData/',views.AnalysisData,name="AnalysisData"),
   path('getEvaInfo/',views.getEvaInfo,name="getEvaInfo"),
   path('showEvaInfo/',views.showEvaInfo,name="showEvaInfo"),
   path('postAssessInfo/',views.postAssessInfo,name="postAssessInfo"),
   path('getAssessPlan/',views.getAssessPlan,name="getAssessPlan"),
   path('savePlanQNaire/',views.savePlanQNaire,name="savePlanQNaire"),
   path('getEvaAnswer/',views.getEvaAnswer,name="getEvaAnswer"),
   path('logout/',views.logout,name="logout"),
   path('manageModel/',views.manageModel,name="manageModel"),
   path('setModel/',views.setModel,name="setModel"),
   path('deleteModel/',views.deleteModel,name="deleteModel"),
   path('newEvaFromModel/',views.newEvaFromModel,name="newEvaFromModel"),
   path('searchAssess/',views.searchAssess,name="searchAssess"),
   path('silk/',include("silk.urls"))
]

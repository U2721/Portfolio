from django.shortcuts import render, redirect, reverse, render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from MyEva.models import UserList
from MyEva.models import MethodList
from MyEva.models import IndexList
from MyEva.models import SurveyList
from MyEva.models import AssessList
from MyEva.models import QuestionList
from MyEva.models import ChoiceList
from MyEva.models import ScaleList
from MyEva.models import PaperList
from MyEva.models import AnswerList
from MyEva.models import FIBAnswerList
from MyEva.models import SCAList
from MyEva.models import MCAList
from MyEva.models import ScaleAnswerList
from MyEva.models import PlanList
from MyEva.models import HeuEvaResult
from MyEva.models import PerformanceRecord
from MyEva.models import ModelList
from django.contrib import messages
import os
import json
import math
import numpy
import jieba
import datetime
import re
from collections import Counter

import sys

# Create your views here.

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def index(request):  # 测试页面用
    return render(request, "results2.html")


def logout(request):
    global USER
    USER.online = False
    USER.save()
    return render(request, "login.html")


def login(request):  # 登录
    result = ""
    global USER
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        thisUser = UserList.objects.filter(UserName=username)
        print(type(thisUser))
        print(thisUser)
        # 判断是否为空
        if thisUser.exists():
            for user in thisUser:
                if user.Password == password:
                    result = "登录成功"
                    USER = user
                    user.online = True
                    user.save()
                    return HttpResponseRedirect(reverse('chooseEva'))
                else:
                    messages.error(request, "密码错误")
                    result = "密码错误"
        else:
            messages.error(request, "用户不存在")
            result = "用户不存在"
    print(result)
    return render(request, "login.html")


def register(request):  # 注册
    if request.method == "POST":
        username = request.POST.get("Regusername", None)
        password = request.POST.get("Regpassword", None)
        status = request.POST.get("user_type", None)
        if status == "VIP":
            STANumber = 1
        else:
            STANumber = 0
        if UserList.objects.filter(UserName=username):
            messages.error(request, "用户名已存在")
            return render(request, "login.html")
        else:
            UserList.objects.create(UserName=username, Password=password, Status=STANumber)
            messages.success(request, "注册成功")
    return render(request, "login.html")


def indexandmethod(request):  # 指标与方法库
    HtmlIndexList = []
    HtmlMethodList = []
    MyIndexList = IndexList.objects.values('FatherName', 'Description').distinct()
    MyMethodList = MethodList.objects.values('MethodName', 'Description').distinct()
    i = 0
    for index in MyIndexList:
        tempIndex = {'id': i, 'title': 'title', 'content': 'content'}
        tempIndex['title'] = index['FatherName']
        tempIndex['content'] = index['Description'].replace("\n", "<br/>")
        i = i + 1
        HtmlIndexList.append(tempIndex)
    j = 0
    for method in MyMethodList:
        tempMethod = {'id': j, 'title': 'title', 'content': 'content'}
        tempMethod['title'] = method['MethodName']
        tempMethod['content'] = method['Description'].replace("\n", "<br/>")
        j = j + 1
        HtmlMethodList.append(tempMethod)
    return render(request, "IndexAndMethod.html",
                  {'IndexList': json.dumps(HtmlIndexList), 'MethodList': json.dumps(HtmlMethodList)})


def newEva(request):  # 转到新建评估界面
    HtmlModelList = getAllModels()
    global USER
    # user=UserList.objects.get(online=True)
    tempUser = {'userid': USER.UserId, 'username': USER.UserName, 'userStatus': USER.Status}
    return render(request, "newEva.html", {'ModelList': HtmlModelList, 'User': tempUser})


def getIndexInfo(choosedIndexList):  # 获取指标信息
    IndexInfo = []
    AllIndexFamilyName = IndexList.objects.all().values('FamilyName').distinct()
    j = 1
    for familyname in AllIndexFamilyName:

        thisFamily = familyname['FamilyName']
        thisFamilyMembers = IndexList.objects.filter(FamilyName=thisFamily)
        tempFamily = {'id': j, 'name': thisFamily, 'FirstList': []}
        Fathers = []
        # 统计FatherName
        for member in thisFamilyMembers:  # 这个家族的成员
            FatherName = member.FatherName
            Fathers.append(FatherName)
        Fathers = set(Fathers)  # 去重
        k = 1
        for father in Fathers:
            tempFather = {'id': j * 10 + k, 'listTitle': father, 'selected': [], 'SecondList': []}
            l = 1
            for member in thisFamilyMembers:
                if member.FatherName == father:
                    tempIndex = {'id': j * 100 + k * 10 + l, 'listTitle': member.IndexName, 'method': member.thisMethod}
                    tempFather['SecondList'].append(tempIndex)
                    l = l + 1
                    if (str(member.IndexId) in choosedIndexList):
                        print(member.IndexId)
                        print(tempIndex['listTitle'])
                        tempFather['selected'].append(tempIndex)
            tempFamily['FirstList'].append(tempFather)
            k = k + 1
        IndexInfo.append(tempFamily)
        j = j + 1
    return IndexInfo


def newBlankEva(request):  # 新建空白评估
    global USER
    if request.method == "POST":
        EvaType = request.POST.get("eva", None)
        EvaName = request.POST.get("name", None)
        EvaDetail = request.POST.get("detail", None)
        EvaUseNum = request.POST.get("peopleNum", None)

        if EvaType == "survey":
            # 新建评估 插入新建的

            AssessList.objects.create(AssessName=EvaName, AssessOneDes=EvaDetail, AssessType=0, AssessUseNum=EvaUseNum,
                                      UserId=USER)
            # 获取新建的这个id
            thisAssess = AssessList.objects.get(AssessName=EvaName, AssessOneDes=EvaDetail, AssessType=0,
                                                AssessUseNum=EvaUseNum, UserId=USER)
            # thisAssessId=thisAssess.AssessId
            SurveyList.objects.create(AssessId=thisAssess, SurveyName=EvaName, SurveyUseNum=EvaUseNum)

            ThisQNaire = SurveyList.objects.get(AssessId=thisAssess, SurveyName=EvaName)
            tempQNaire = {'name': ThisQNaire.SurveyName, 'id': ThisQNaire.SurveyId}
            return render(request, "newQNaire.html", {'QNaire': tempQNaire, 'AllQuestions': []})
        elif EvaType == "comprehensive":  # 新建综合评估
            AssessList.objects.create(AssessName=EvaName, AssessOneDes=EvaDetail, AssessType=1, AssessUseNum=EvaUseNum,
                                      UserId=USER)
            thisAssess = AssessList.objects.get(AssessName=EvaName, AssessOneDes=EvaDetail, AssessType=1,
                                                AssessUseNum=EvaUseNum, UserId=USER)
            # 获取指标信息
            IndexInfo = []
            IndexInfo = getIndexInfo([])
            print(IndexInfo)
            Assess = {'AssessId': thisAssess.AssessId, 'AssessName': thisAssess.AssessName}
            return render(request, "edit1.html", {'Assess': Assess, 'IndexInfo': IndexInfo, 'ModelId': -1})
    return render(request, "newEva.html")


def newPlan(Assess, Indexs, Methods, ModelId):  # 为评估增加预设方案
    print("新增方案")
    print(Assess)
    thisAssess = AssessList.objects.get(AssessId=Assess['AssessId'])
    indexNum = 0
    indexIdList = []
    temppeople = []
    Model = AssessList.objects.filter(AssessId=ModelId)
    for family in Indexs:
        for father in family['FirstList']:
            for selectedIndex in father['selected']:
                indexNum = indexNum + 1
                thisMethods = selectedIndex['method'].split(",")
                indexId = IndexList.objects.get(IndexName=selectedIndex['listTitle'])
                print(indexId.IndexName)
                indexIdList.append(str(indexId.IndexId))
                for thismethod in thisMethods:
                    tempPlanName = "针对" + selectedIndex['listTitle'] + "的" + thismethod
                    PlanList.objects.create(PlanName=tempPlanName, PlanTypeId=thismethod, AssessId=thisAssess)
                    if Model.exists():
                        print(tempPlanName)
                        print(Model)
                        for mo in Model:
                            ModelPlan = PlanList.objects.filter(PlanName=tempPlanName, AssessId=mo)
                            print("ModelPlan")
                            print(ModelPlan)
                            if ModelPlan.exists():  # 存在
                                for mplan in ModelPlan:
                                    thisPlan = PlanList.objects.get(PlanName=tempPlanName, PlanTypeId=thismethod,
                                                                    AssessId=thisAssess)
                                    thisPlan.PlanTypeId = mplan.PlanTypeId
                                    thisPlan.save()
                            else:
                                print("不存在")
                    for method in Methods:
                        if (thismethod == method['MethodName']):
                            temppeople.append(method['people'])

    temppeople = list(set(temppeople))
    thisAssess.AssessIndexNum = indexNum
    thisAssess.People = temppeople


    thisAssess.AssessIndexId = ";".join(indexIdList)
    thisAssess.save()
    print("存入数量")
    #print(len(thisAssess.AssessIndexId))

    print("建立方案完毕")
    return True


def getAssessPlan(request):  # 获取方案用于新建方案的人查看（不包含问卷）
    assessId = json.loads(request.GET['assess'])
    thisAssess = AssessList.objects.get(AssessId=assessId)
    Assess = {"AssessId": assessId, "AssessName": thisAssess.AssessName}
    AllPlans = PlanList.objects.filter(AssessId=thisAssess)
    HtmlPlans = []
    j = 1
    HtmlQNaires = []
    for plan in AllPlans:
        temp = {"id": j, "PlanId": plan.PlanId, "PlanName": plan.PlanName, "PlanType": plan.PlanTypeId}
        HtmlPlans.append(temp)
        j = j + 1
        if (str(plan.PlanTypeId).isdigit()):  # 判断里面是不是数字，是的话则为survey
            temp['PlanType'] = "可用性测试"
            HtmlQuestionsList = []
            surveyId = plan.PlanTypeId
            thisSurvey = SurveyList.objects.get(SurveyId=surveyId)
            Questions = QuestionList.objects.filter(SurveyId=thisSurvey)
            print(type(Questions))
            q = 1
            for que in Questions:

                if que.QuestionType == 1:
                    tempQue = {'id': q, 'queId': '', 'title': 'title', 'type': 'SingleChoose', 'ChooseA': '',
                               'ChooseB': '', 'ChooseC': '', 'ChooseD': '', "answer": ''}
                    tempQue['queId'] = que.QuestionId
                    tempQue['title'] = que.QueDescription
                    choices = ChoiceList.objects.get(QuestionId=que)
                    tempQue['ChooseA'] = choices.ChoiceA
                    tempQue['ChooseB'] = choices.ChoiceB
                    tempQue['ChooseC'] = choices.ChoiceC
                    tempQue['ChooseD'] = choices.ChoiceD
                    HtmlQuestionsList.append(tempQue)
                    q = q + 1
                elif que.QuestionType == 2:
                    tempQue = {'id': q, 'queId': '', 'title': 'title', 'type': 'MultiChoose', 'ChooseA': '',
                               'ChooseB': '', 'ChooseC': '', 'ChooseD': '', 'answer': []}
                    tempQue['queId'] = que.QuestionId
                    tempQue['title'] = que.QueDescription
                    choices = ChoiceList.objects.get(QuestionId=que)
                    tempQue['ChooseA'] = choices.ChoiceA
                    tempQue['ChooseB'] = choices.ChoiceB
                    tempQue['ChooseC'] = choices.ChoiceC
                    tempQue['ChooseD'] = choices.ChoiceD
                    HtmlQuestionsList.append(tempQue)
                    q = q + 1
                elif que.QuestionType == 3:
                    tempQue = {'id': q, 'queId': '', 'title': 'title', 'type': 'FillInBlank', 'answer': ''}
                    tempQue['queId'] = que.QuestionId
                    tempQue['title'] = que.QueDescription
                    HtmlQuestionsList.append(tempQue)
                    q = q + 1
                elif que.QuestionType == 4:
                    tempQue = {'id': q, 'queId': '', 'title': 'title', 'type': 'Scale', 'lowest': 'lowest',
                               'highest': 'highest', 'ScaleCount': 0, 'answer': ''}
                    tempQue['queId'] = que.QuestionId
                    tempQue['title'] = que.QueDescription
                    scale = ScaleList.objects.get(QuestionId=que)
                    tempQue['lowest'] = scale.BeginIndex
                    tempQue['highest'] = scale.EndIndex
                    tempQue['ScaleCount'] = scale.DegreeNum
                    HtmlQuestionsList.append(tempQue)
                    q = q + 1
                elif que.QuestionType == 5:
                    # "id": 3, "title": "嘻嘻嘻嘻", "type": "Paragraph"
                    tempQue = {'id': q, 'queId': '', 'title': 'title', 'type': 'Paragraph'}
                    tempQue['queId'] = que.QuestionId
                    tempQue['title'] = que.QueDescription
                    HtmlQuestionsList.append(tempQue)
                    #q = q + 1
            print(HtmlQuestionsList)
            tempQNaire = {"PlanId": plan.PlanId, "Question": HtmlQuestionsList}
            HtmlQNaires.append(tempQNaire)

    return render(request, "editEvaPlan.html", {'Assess': Assess, 'plans': HtmlPlans, 'QNaires': HtmlQNaires})


def savePlanQNaire(request):  # 存储新建方案中的新建问卷
    Messages = json.loads(request.body)
    QNaires = Messages['QNaires']
    print(QNaires)
    for QNaire in QNaires:
        PlanId = QNaire['PlanId']
        questions = QNaire['Question']
        thisPlan = PlanList.objects.get(PlanId=PlanId)
        thisAssess = thisPlan.AssessId
        tempSurveyName = str(thisAssess.AssessId) + thisPlan.PlanName
        SurveyList.objects.create(SurveyName=tempSurveyName, SurveyUseNum=thisAssess.AssessUseNum,
                                  SurveyQueNum=len(questions), AssessId=thisAssess)
        thisSurvey = SurveyList.objects.get(SurveyName=tempSurveyName, SurveyUseNum=thisAssess.AssessUseNum,
                                            SurveyQueNum=len(questions), AssessId=thisAssess)
        thisPlan.PlanTypeId = thisSurvey.SurveyId  # 将SurveyId对应上Plan
        thisPlan.save()
        for que in questions:
            print(que)
            print(que['type'])
            QueDes = que['title']
            if que['type'] == 'SingleChoose':
                queType = 1
                QuestionList.objects.create(QueDescription=QueDes, QuestionType=queType, SurveyId=thisSurvey)
                thisQuestion = QuestionList.objects.get(QueDescription=QueDes, QuestionType=queType,
                                                        SurveyId=thisSurvey)
                ChoiceList.objects.create(SCQorMCQ=1, ChoiceA=que['ChooseA'], ChoiceB=que['ChooseB'],
                                          ChoiceC=que['ChooseC'], ChoiceD=que['ChooseD'], QuestionId=thisQuestion)
                print("插入成功")
            elif que['type'] == 'MultiChoose':
                queType = 2
                QuestionList.objects.create(QueDescription=QueDes, QuestionType=queType, SurveyId=thisSurvey)
                thisQuestion = QuestionList.objects.get(QueDescription=QueDes, QuestionType=queType,
                                                        SurveyId=thisSurvey)
                ChoiceList.objects.create(SCQorMCQ=2, ChoiceA=que['ChooseA'], ChoiceB=que['ChooseB'],
                                          ChoiceC=que['ChooseC'], ChoiceD=que['ChooseD'], QuestionId=thisQuestion)
            elif que['type'] == 'FillInBlank':
                queType = 3
                QuestionList.objects.create(QueDescription=QueDes, QuestionType=queType, SurveyId=thisSurvey)
            elif que['type'] == 'Scale':
                queType = 4
                QuestionList.objects.create(QueDescription=QueDes, QuestionType=queType, SurveyId=thisSurvey)
                thisQuestion = QuestionList.objects.get(QueDescription=QueDes, QuestionType=queType,
                                                        SurveyId=thisSurvey)
                ScaleList.objects.create(BeginIndex=que['lowest'], EndIndex=que['highest'], DegreeNum=que['ScaleCount'],
                                         QuestionId=thisQuestion)
            elif que['type'] == 'Paragraph':
                queType = 5
                QuestionList.objects.create(QueDescription=QueDes, QuestionType=queType, SurveyId=thisSurvey)
    print("新建方案成功")
    return render(request, "editEvaPlan.html")


def postAssessInfo(request):  # 提交方案描述 评估对象等信息
    Messages = json.loads(request.body)
    EvaDes = Messages['description']
    EvaObject = Messages['object']
    Assess = Messages['Assess']
    thisAssess = AssessList.objects.get(AssessId=Assess['AssessId'])
    thisAssess.AssessDes = EvaDes
    thisAssess.AssessObject = EvaObject
    thisAssess.save()
    return render(request, "editEva2.html")


def getEvaInfo(request):  # 新建评估中 获取选择的指标
    global ASSESS
    global INDEXS
    INDEXS = []
    print(request.body)
    Messages = json.loads(request.body)
    ASSESS = Messages['Assess']
    INDEXS = Messages['Indexs']  # 复杂嵌套数据用request.body
    ModelId = Messages['ModelId']  # 有无模板，模板编号

    methods = MethodList.objects.all()
    htmlMethods = []
    for method in methods:
        temp = {'MethodId': method.MethodId, 'MethodName': method.MethodName, 'dataSource': method.dataSource,
                'dealData': method.dealData, 'people': method.people}
        htmlMethods.append(temp)
    print(ASSESS)
    newPlan(ASSESS, INDEXS, htmlMethods, ModelId)
    methods = MethodList.objects.all()
    print(INDEXS)
    return render(request, "editEva2.html", {'Assess': ASSESS, 'Index': INDEXS, 'Method': htmlMethods})


def showEvaInfo(request):  # 新建评估中将指标和方法等信息展示
    global INDEXS  # 正规来讲，index也应该在上个函数中存入数据库，再从数据库中读出
    assessid = json.loads(request.GET['assess'])
    thisAssess = AssessList.objects.get(AssessId=assessid)
    myAssess = {'AssessId': assessid, 'AssessName': thisAssess.AssessName}
    methods = MethodList.objects.all()
    htmlMethods = []
    for method in methods:
        temp = {'MethodId': method.MethodId, 'MethodName': method.MethodName, 'dataSource': method.dataSource,
                'dealData': method.dealData, 'people': method.people}
        htmlMethods.append(temp)
    print(INDEXS)
    return render(request, "editEva2.html", {'Assess': myAssess, 'Index': INDEXS, 'Method': htmlMethods})


def addQNaire(request):  # 新建问卷的问题
    print('newQuestions')
    print(request.body)
    message = json.loads(request.body)
    obj = message['Questions']
    QNaire = message['QNaire']
    print(obj)
    QNaireId = QNaire['id']
    ThisQNaire = SurveyList.objects.get(SurveyId=QNaireId)
    if request.method == "POST":

        Questions = []
        Questions = obj
        print(type(Questions))
        print(Questions)
        ThisQNaire.SurveyQueNum = len(Questions)
        ThisQNaire.save()
        for que in Questions:
            print(que)
            print(que['type'])
            QueDes = que['title']
            if que['type'] == 'SingleChoose':
                queType = 1
                QuestionList.objects.create(QueDescription=QueDes, QuestionType=queType, SurveyId=ThisQNaire)
                thisQuestion = QuestionList.objects.get(QueDescription=QueDes, QuestionType=queType,
                                                        SurveyId=ThisQNaire)
                ChoiceList.objects.create(SCQorMCQ=1, ChoiceA=que['ChooseA'], ChoiceB=que['ChooseB'],
                                          ChoiceC=que['ChooseC'], ChoiceD=que['ChooseD'], QuestionId=thisQuestion)
                print("插入成功")
            elif que['type'] == 'MultiChoose':
                queType = 2
                QuestionList.objects.create(QueDescription=QueDes, QuestionType=queType, SurveyId=ThisQNaire)
                thisQuestion = QuestionList.objects.get(QueDescription=QueDes, QuestionType=queType,
                                                        SurveyId=ThisQNaire)
                ChoiceList.objects.create(SCQorMCQ=2, ChoiceA=que['ChooseA'], ChoiceB=que['ChooseB'],
                                          ChoiceC=que['ChooseC'], ChoiceD=que['ChooseD'], QuestionId=thisQuestion)
            elif que['type'] == 'FillInBlank':
                queType = 3
                QuestionList.objects.create(QueDescription=QueDes, QuestionType=queType, SurveyId=ThisQNaire)
            elif que['type'] == 'Scale':
                queType = 4
                QuestionList.objects.create(QueDescription=QueDes, QuestionType=queType, SurveyId=ThisQNaire)
                thisQuestion = QuestionList.objects.get(QueDescription=QueDes, QuestionType=queType,
                                                        SurveyId=ThisQNaire)
                ScaleList.objects.create(BeginIndex=que['lowest'], EndIndex=que['highest'], DegreeNum=que['ScaleCount'],
                                         QuestionId=thisQuestion)
            elif que['type'] == 'Paragraph':
                queType = 5
                QuestionList.objects.create(QueDescription=QueDes, QuestionType=queType, SurveyId=ThisQNaire)

    return render(request, "newEva.html")


def getAllSearchData():
    GASDStartTime = datetime.datetime.now()
    AllSearchList = UserList.objects.all().values('SearchHistory')
    SearchData = []
    for search in AllSearchList:
        if (search['SearchHistory'] != None):
            SearchData.append(search['SearchHistory'])
    CFStartTime = datetime.datetime.now()
    htmlFrequency = countFrequency(SearchData)
    CFEndTime = datetime.datetime.now()
    print("CF总执行时间")
    print((CFEndTime - CFStartTime).seconds)
    GASDEndTime = datetime.datetime.now()
    print("GASD总执行时间")
    print((GASDEndTime - GASDStartTime).seconds)
    return htmlFrequency


def getUserRecommend():
    global USER
    searchData = USER.SearchHistory
    searchList = []
    recommendAssess = []
    if (searchData != None):
        searchList = searchData.split(';')
        print("searchList")
        print(searchList)
        searchFrequency = countFrequency(searchList)
        mostWord = searchFrequency[0]['name']
        recommendAssess = fuzzySearch(mostWord)
    return recommendAssess


def chooseEva(request):  # 展示评估方案列表

    chooseEvaStartTime = datetime.datetime.now()

    print("chooseEva")
    evalist = AssessList.objects.all().select_related()
    HtmlEvaList = []
    global USER
    tempUser = {'userid': USER.UserId, 'username': USER.UserName, 'userStatus': USER.Status}
    WCResultsStartTime = datetime.datetime.now()
    WCResults = getAllSearchData()
    WCResultsEndTime = datetime.datetime.now()
    print("WCResults执行时间")
    print((WCResultsEndTime - WCResultsStartTime).seconds)
    RecommendStartTime = datetime.datetime.now()
    recommend = getUserRecommend()
    RecommendEndTime = datetime.datetime.now()
    print("Recommend执行时间")
    print((RecommendEndTime - RecommendStartTime).seconds)
    HtmlAssessNameList = []
    for eva in evalist:
        HtmlAssessNameList.append(eva.AssessName)
        tempeva = {'id': 0, 'name': '', 'person': '', 'InShort': '', 'BeginTime': '', 'process': '', 'condition': ''}
        tempeva['id'] = eva.AssessId
        tempeva['name'] = eva.AssessName
        tempeva['person'] = eva.UserId.UserName
        tempeva['InShort'] = eva.AssessOneDes
        tempeva['BeginTime'] = str(eva.AssessBeginTime)[0:16]
        tempeva['process'] = eva.AssessPro
        if eva.AssessPro < 100:
            tempeva['condition'] = 'ing'
        else:
            tempeva['condition'] = 'End'
        HtmlEvaList.append(tempeva)
    chooseEvaEndTime = datetime.datetime.now()
    print("总执行时间")
    print((chooseEvaEndTime - chooseEvaStartTime).seconds)
    return render(request, "chooseEva.html",
                  {'EvaList': json.dumps(HtmlEvaList), 'User': tempUser, 'AssessNameList': HtmlAssessNameList,
                   'WCResults': WCResults, 'Recommend': recommend})


def getFillAssess(request):  # 录入评估数据
    assessId = json.loads(request.GET['assess'])
    readOnly = json.loads(request.GET['readOnly'])
    print(readOnly)
    # 先get到assess的id
    Assess = AssessList.objects.get(AssessId=assessId)
    global USER
    if (USER.SearchHistory != None):
        USER.SearchHistory = USER.SearchHistory + ";" + Assess.AssessName
    else:
        USER.SearchHistory = Assess.AssessName
    USER.save()
    if Assess.AssessType == 0:  # 录入问卷
        HtmlQuestionsList = []
        Survey = SurveyList.objects.get(AssessId=Assess.AssessId)
        Questions = QuestionList.objects.filter(SurveyId=Survey)
        print(type(Questions))
        j = 1
        for que in Questions:
            if que.QuestionType == 1:
                tempQue = {'id': j, 'queId': '', 'title': 'title', 'type': 'SingleChoose', 'ChooseA': '', 'ChooseB': '',
                           'ChooseC': '', 'ChooseD': '', "answer": ''}
                tempQue['queId'] = que.QuestionId
                tempQue['title'] = que.QueDescription
                choices = ChoiceList.objects.get(QuestionId=que)
                tempQue['ChooseA'] = choices.ChoiceA
                tempQue['ChooseB'] = choices.ChoiceB
                tempQue['ChooseC'] = choices.ChoiceC
                tempQue['ChooseD'] = choices.ChoiceD
                HtmlQuestionsList.append(tempQue)
                j = j + 1
            elif que.QuestionType == 2:
                tempQue = {'id': j, 'queId': '', 'title': 'title', 'type': 'MultiChoose', 'ChooseA': '', 'ChooseB': '',
                           'ChooseC': '', 'ChooseD': '', 'answer': []}
                tempQue['queId'] = que.QuestionId
                tempQue['title'] = que.QueDescription
                choices = ChoiceList.objects.get(QuestionId=que)
                tempQue['ChooseA'] = choices.ChoiceA
                tempQue['ChooseB'] = choices.ChoiceB
                tempQue['ChooseC'] = choices.ChoiceC
                tempQue['ChooseD'] = choices.ChoiceD
                HtmlQuestionsList.append(tempQue)
                j = j + 1
            elif que.QuestionType == 3:
                tempQue = {'id': j, 'queId': '', 'title': 'title', 'type': 'FillInBlank', 'answer': ''}
                tempQue['queId'] = que.QuestionId
                tempQue['title'] = que.QueDescription
                HtmlQuestionsList.append(tempQue)
                j = j + 1
            elif que.QuestionType == 4:
                tempQue = {'id': j, 'queId': '', 'title': 'title', 'type': 'Scale', 'lowest': 'lowest',
                           'highest': 'highest', 'ScaleCount': 0, 'answer': ''}
                tempQue['queId'] = que.QuestionId
                tempQue['title'] = que.QueDescription
                scale = ScaleList.objects.get(QuestionId=que)
                tempQue['lowest'] = scale.BeginIndex
                tempQue['highest'] = scale.EndIndex
                tempQue['ScaleCount'] = scale.DegreeNum
                HtmlQuestionsList.append(tempQue)
                j = j + 1
            elif que.QuestionType == 5:
                # "id": 3, "title": "嘻嘻嘻嘻", "type": "Paragraph"
                tempQue = {'id': j, 'queId': '', 'title': 'title', 'type': 'Paragraph'}
                tempQue['queId'] = que.QuestionId
                tempQue['title'] = que.QueDescription
                HtmlQuestionsList.append(tempQue)

        print(HtmlQuestionsList)
        return render(request, "FillQNaire.html",
                      {'QuestionList': json.dumps(HtmlQuestionsList), 'SurveyId': Survey.SurveyId,
                       'readOnly': readOnly})
    else:  # 是综合评估
        HtmlAssess = {"AssessId": assessId, "AssessName": Assess.AssessName}
        AllPlans = PlanList.objects.filter(AssessId=Assess)
        HtmlPlans = []
        j = 1
        HtmlQNaires = []
        HtmlHeuRegular = []
        for plan in AllPlans:
            temp = {"id": j, "PlanId": plan.PlanId, "PlanName": plan.PlanName, "PlanType": plan.PlanTypeId}
            if (str(plan.PlanTypeId).isdigit()):  # 判断里面是不是数字，是的话则为survey
                temp['PlanType'] = "可用性测试"
                HtmlQuestionsList = []
                surveyId = plan.PlanTypeId
                thisSurvey = SurveyList.objects.get(SurveyId=surveyId)
                Questions = QuestionList.objects.filter(SurveyId=thisSurvey)
                print(type(Questions))
                q = 1
                for que in Questions:

                    if que.QuestionType == 1:
                        tempQue = {'id': q, 'queId': '', 'title': 'title', 'type': 'SingleChoose', 'ChooseA': '',
                                   'ChooseB': '', 'ChooseC': '', 'ChooseD': '', "answer": ''}
                        tempQue['queId'] = que.QuestionId
                        tempQue['title'] = que.QueDescription
                        choices = ChoiceList.objects.get(QuestionId=que)
                        tempQue['ChooseA'] = choices.ChoiceA
                        tempQue['ChooseB'] = choices.ChoiceB
                        tempQue['ChooseC'] = choices.ChoiceC
                        tempQue['ChooseD'] = choices.ChoiceD
                        HtmlQuestionsList.append(tempQue)
                        q = q + 1
                    elif que.QuestionType == 2:
                        tempQue = {'id': q, 'queId': '', 'title': 'title', 'type': 'MultiChoose', 'ChooseA': '',
                                   'ChooseB': '', 'ChooseC': '', 'ChooseD': '', 'answer': []}
                        tempQue['queId'] = que.QuestionId
                        tempQue['title'] = que.QueDescription
                        choices = ChoiceList.objects.get(QuestionId=que)
                        tempQue['ChooseA'] = choices.ChoiceA
                        tempQue['ChooseB'] = choices.ChoiceB
                        tempQue['ChooseC'] = choices.ChoiceC
                        tempQue['ChooseD'] = choices.ChoiceD
                        HtmlQuestionsList.append(tempQue)
                        q = q + 1
                    elif que.QuestionType == 3:
                        tempQue = {'id': q, 'queId': '', 'title': 'title', 'type': 'FillInBlank', 'answer': ''}
                        tempQue['queId'] = que.QuestionId
                        tempQue['title'] = que.QueDescription
                        HtmlQuestionsList.append(tempQue)
                        q = q + 1
                    elif que.QuestionType == 4:
                        tempQue = {'id': q, 'queId': '', 'title': 'title', 'type': 'Scale', 'lowest': 'lowest',
                                   'highest': 'highest', 'ScaleCount': 0, 'answer': ''}
                        tempQue['queId'] = que.QuestionId
                        tempQue['title'] = que.QueDescription
                        scale = ScaleList.objects.get(QuestionId=que)
                        tempQue['lowest'] = scale.BeginIndex
                        tempQue['highest'] = scale.EndIndex
                        tempQue['ScaleCount'] = scale.DegreeNum
                        HtmlQuestionsList.append(tempQue)
                        q = q + 1
                    elif que.QuestionType == 5:
                        # "id": 3, "title": "嘻嘻嘻嘻", "type": "Paragraph"
                        tempQue = {'id': q, 'queId': '', 'title': 'title', 'type': 'Paragraph'}
                        tempQue['queId'] = que.QuestionId
                        tempQue['title'] = que.QueDescription
                        HtmlQuestionsList.append(tempQue)
                        #q = q + 1
                print(HtmlQuestionsList)
                tempQNaire = {"PlanId": plan.PlanId, "Question": HtmlQuestionsList}
                HtmlQNaires.append(tempQNaire)
            elif (plan.PlanTypeId == '启发式评估'):
                thisIndexName = plan.PlanName[2:].split('的')[0]
                thisIndex = IndexList.objects.get(IndexName=thisIndexName)
                heuregular = thisIndex.HeuRegular
                tempHeu = {"PlanId": plan.PlanId, "HeuRegular": heuregular}
                HtmlHeuRegular.append(tempHeu)
            HtmlPlans.append(temp)

            j = j + 1
        return render(request, "evaPlan.html",
                      {'Assess': HtmlAssess, 'plans': HtmlPlans, 'QNaires': HtmlQNaires, 'HeuRegulars': HtmlHeuRegular,
                       'readOnly': readOnly})


def FillQNaire(request):  # 填写问卷
    Messages = json.loads(request.body)
    Answers = Messages['AllQuestions']
    thisSurveyId = Messages['Survey']
    global USER
    print(USER.UserName)
    thisSurvey = SurveyList.objects.get(SurveyId=thisSurveyId)
    thisPaper = PaperList.objects.filter(UserId=USER, SurveyId=thisSurvey)
    if thisPaper.exists():
        print("您已填过该问卷！不可重复填写！")
        messages.error(request, "您已填过该问卷！不可重复填写！")
        return render(request, "FillQNaire.html")
    else:
        # 增加一个填问卷的人
        surveyedNum = math.ceil((thisSurvey.SurveyUseNum * thisSurvey.SurveyPro) / 100)
        print(surveyedNum)
        surveyedNum = surveyedNum + 1
        print(surveyedNum)
        pro = surveyedNum * 100 / thisSurvey.SurveyUseNum
        print(pro)
        if (pro > 100):
            pro = 100
        thisSurvey.SurveyPro = pro
        thisSurvey.save()
        assessId = thisSurvey.AssessId
        assessedNum = math.ceil((assessId.AssessUseNum * assessId.AssessPro) / 100)  # 向上取整
        assessedNum = assessedNum + 1
        assessPro = assessedNum * 100 / assessId.AssessUseNum
        if (assessPro > 100):
            assessPro = 100
        assessId.AssessPro = assessPro
        assessId.save()

        PaperList.objects.create(UserId=USER, SurveyId=thisSurvey)
        thisPaper = PaperList.objects.get(UserId=USER, SurveyId=thisSurvey)
        for ans in Answers:
            print(type(ans))
            print(ans['queId'])
            thisQuestion = QuestionList.objects.get(QuestionId=ans['queId'])
            if ans['type'] == 'SingleChoose':  # 单选题
                AnswerList.objects.create(QuestionType=1, PaperId=thisPaper, QuestionId=thisQuestion)
                thisAnswer = AnswerList.objects.get(QuestionType=1, PaperId=thisPaper, QuestionId=thisQuestion)
                SCAList.objects.create(ChoiceAnswer=ans['answer'], AnswerId=thisAnswer)
            elif ans['type'] == 'MultiChoose':  # 多选题
                AnswerList.objects.create(QuestionType=2, PaperId=thisPaper, QuestionId=thisQuestion)
                thisAnswer = AnswerList.objects.get(QuestionType=2, PaperId=thisPaper, QuestionId=thisQuestion)
                MCAanswers = ','.join(ans['answer'])
                MCAList.objects.create(ChoiceAnswer=MCAanswers, ChoiceNum=len(ans['answer']), AnswerId=thisAnswer)
            elif ans['type'] == 'FillInBlank':  # 填空题
                AnswerList.objects.create(QuestionType=3, PaperId=thisPaper, QuestionId=thisQuestion)
                thisAnswer = AnswerList.objects.get(QuestionType=3, PaperId=thisPaper, QuestionId=thisQuestion)
                print(ans['answer'])
                FIBAnswerList.objects.create(FIBAnswer=ans['answer'], AnswerId=thisAnswer)
            elif ans['type'] == 'Scale':  # 量表题
                AnswerList.objects.create(QuestionType=4, PaperId=thisPaper, QuestionId=thisQuestion)
                thisAnswer = AnswerList.objects.get(QuestionType=4, PaperId=thisPaper, QuestionId=thisQuestion)
                ScaleAnswerList.objects.create(DegreeAnswer=ans['answer'], AnswerId=thisAnswer)
            elif ans['type'] == 'Paragraph':
                print("段落")

        messages.success(request, "成功提交！")
        return render(request, "chooseEva.html")


def deleteAssess(request):  # 删除评估方案
    Messages = json.loads(request.body)
    assessId = Messages['assess']
    AssessList.objects.filter(AssessId=assessId).delete()
    print("删除成功")
    return render(request, "chooseEva.html")


def countFrequency(answers):  # 计算词频
    # print(answers)
    htmlFrequency = []
    if (answers != []):
        myTxt = ''.join(answers)
        myTxt_words = [x for x in jieba.cut(myTxt) if len(x) >= 2]
        c = Counter(myTxt_words).most_common(10)
        print(json.dumps(c, ensure_ascii=False))
        for oneWord in c:
            temp = {'name': '', 'value': 0}
            temp['name'] = oneWord[0]
            temp['value'] = oneWord[1]
            htmlFrequency.append(temp)
    return htmlFrequency


def analysisQNaire(thisSurvey):  # 分析问卷结果
    thisPapers = PaperList.objects.filter(SurveyId=thisSurvey)
    thisQuestions = QuestionList.objects.filter(SurveyId=thisSurvey)
    # AllAnswerList=AnswerList.objects.all().select_related()
    thisAnswers = []
    for paper in thisPapers:
        # answers=[]
        answers = AnswerList.objects.filter(PaperId=paper)
        for ans in answers:
            thisAnswers.append(ans)
    j = 1
    HtmlAnswers = []
    for que in thisQuestions:
        if que.QuestionType == 1:  # 单选题
            thisSCQ = ChoiceList.objects.get(QuestionId=que)  # 获取题目
            # #thisSCQ=[]
            # for choicelist in AllChoiceList:
            #     if(choicelist.QuestionId==que):
            #         thisSCQ=choicelist

            chooseANum = 0
            chooseBNum = 0
            chooseCNum = 0
            chooseDNum = 0
            completePeople = 0

            for thisAns in thisAnswers:
                if thisAns.QuestionId == que:  # 是这道题的答案
                    completePeople = completePeople + 1  # 有效回答人数+1
                    choiced = SCAList.objects.get(AnswerId=thisAns)  # 获取具体答案

                    if (choiced.ChoiceAnswer == 'A'):
                        chooseANum = chooseANum + 1
                    elif (choiced.ChoiceAnswer == 'B'):
                        chooseBNum = chooseBNum + 1
                    elif (choiced.ChoiceAnswer == 'C'):
                        chooseCNum = chooseCNum + 1
                    elif (choiced.ChoiceAnswer == 'D'):
                        chooseDNum = chooseDNum + 1
            temp = {'Id': j, 'queId': que.QuestionId, 'queType': 'SingleChoose', 'title': que.QueDescription,
                    'filledPeople': completePeople, 'chooseA': thisSCQ.ChoiceA, 'chooseB': thisSCQ.ChoiceB,
                    'chooseC': thisSCQ.ChoiceC, 'chooseD': thisSCQ.ChoiceD,
                    'results': [chooseANum, chooseBNum, chooseCNum, chooseDNum],
                    'resultRatio': [chooseANum / completePeople, chooseBNum / completePeople,
                                    chooseCNum / completePeople, chooseDNum / completePeople]}
            HtmlAnswers.append(temp)
            j = j + 1
        elif que.QuestionType == 2:  # 多选题
            thisMCQ = ChoiceList.objects.get(QuestionId=que)

            chooseANum = 0
            chooseBNum = 0
            chooseCNum = 0
            chooseDNum = 0
            completePeople = 0
            for thisAns in thisAnswers:
                if thisAns.QuestionId == que:  # 是这道题的答案
                    completePeople = completePeople + 1  # 有效回答人数+1
                    choiced = MCAList.objects.get(AnswerId=thisAns)

                    choicedAnswers = choiced.ChoiceAnswer.split(',')
                    for ca in choicedAnswers:
                        if (ca == 'A'):
                            chooseANum = chooseANum + 1
                        elif (ca == 'B'):
                            chooseBNum = chooseBNum + 1
                        elif (ca == 'C'):
                            chooseCNum = chooseCNum + 1
                        elif (ca == 'D'):
                            chooseDNum = chooseDNum + 1
            temp = {'Id': j, 'queId': que.QuestionId, 'queType': 'MultiChoose', 'title': que.QueDescription,
                    'filledPeople': completePeople, 'chooseA': thisMCQ.ChoiceA, 'chooseB': thisMCQ.ChoiceB,
                    'chooseC': thisMCQ.ChoiceC, 'chooseD': thisMCQ.ChoiceD,
                    'results': [chooseANum, chooseBNum, chooseCNum, chooseDNum],
                    'resultRatio': [chooseANum / completePeople, chooseBNum / completePeople,
                                    chooseCNum / completePeople, chooseDNum / completePeople]}
            HtmlAnswers.append(temp)
            j = j + 1
        elif que.QuestionType == 4:  # 量表题
            thisScale = ScaleList.objects.get(QuestionId=que)
            # thisScale = []
            chooseNum = []
            for i in range(0, thisScale.DegreeNum):
                chooseNum.append(0)
            print("长度")
            print(len(chooseNum))
            completePeople = 0
            for thisAns in thisAnswers:
                if thisAns.QuestionId == que:
                    completePeople = completePeople + 1
                    choosed = ScaleAnswerList.objects.get(AnswerId=thisAns)
                    print("下标")
                    print(choosed.DegreeAnswer - 1)
                    chooseNum[choosed.DegreeAnswer - 1] = chooseNum[choosed.DegreeAnswer - 1] + 1
            chooseRatio = []
            for i in range(0, thisScale.DegreeNum):
                chooseRatio.append(chooseNum[i] / completePeople)
            degree = []
            degree = (numpy.arange(1, thisScale.DegreeNum + 1, 1)).tolist()
            temp = {'Id': j, 'queId': que.QuestionId, 'queType': 'Scale', 'title': que.QueDescription,
                    'Begin': thisScale.BeginIndex, 'End': thisScale.EndIndex, 'filledPeople': completePeople,
                    'ScaleDegree': degree, 'results': chooseNum, 'resultRatio': chooseRatio}
            HtmlAnswers.append(temp)
            j = j + 1
        elif que.QuestionType == 3:  # 填空题
            FIBAnswers = []
            completePeople = 0
            for thisAns in thisAnswers:
                if thisAns.QuestionId == que:  # 是这道题的答案
                    completePeople = completePeople + 1  # 有效回答人数+1
                    thisFIBAns = FIBAnswerList.objects.get(AnswerId=thisAns)
                    FIBAnswers.append(thisFIBAns.FIBAnswer)
            htmlFrequency = countFrequency(FIBAnswers)
            temp = {'Id': j, 'queId': que.QuestionId, 'queType': 'FillInBlank', 'title': que.QueDescription,
                    'results': FIBAnswers, 'WCResults': htmlFrequency}
            HtmlAnswers.append(temp)
            j = j + 1

    return HtmlAnswers


def getEvaAnswer(request):  # 获取用户填的评估数据
    message = json.loads(request.body)
    print(message)
    Assess = message['Assess']
    AllInfo = message['AllInfo']
    AssessId = Assess['AssessId']
    global USER

    thisAssess = AssessList.objects.get(AssessId=AssessId)

    for info in AllInfo:
        PlanId = info['Planid']
        PlanType = info['PlanType']
        thisPlan = PlanList.objects.get(PlanId=PlanId)
        IndexName = thisPlan.PlanName[2:].split('的')[0]  # 截取“针对”之后，“的”之前
        thisIndex = IndexList.objects.get(IndexName=IndexName)
        if (PlanType == "启发式评估"):
            UseTables = []
            nowUseTables = HeuEvaResult.objects.filter(PlanId=thisPlan, UserId=USER)
            if nowUseTables.exists():
                print("您已填过该评估方案！不可重复填写！")
                messages.error(request, "您已填过该评估方案！不可重复填写！")
                return render(request, "evaPlan.html")
            UseTables = info['UseTables']
            for usetable in UseTables:
                HeuEvaResult.objects.create(Interface=usetable['local'], HeuProblem=usetable['problem'],
                                            SeriousDegree=usetable['serious'], Advice=usetable['advice'],
                                            IndexId=thisIndex, PlanId=thisPlan, UserId=USER)
        elif (PlanType == "数据记录"):
            print("录入数据记录！")
            dataInfo = []
            dataInfo = info['myInfo'].split(',')
            nowPerformanceRecord = PerformanceRecord.objects.filter(PlanId=thisPlan, UserId=USER)
            if nowPerformanceRecord.exists():
                print("您已填过该评估方案！不可重复填写！")
                messages.error(request, "您已填过该评估方案！不可重复填写！")
                return render(request, "evaPlan.html")
            PerformanceRecord.objects.create(ErrorRate=int(dataInfo[0]), FinishTime=int(dataInfo[1]),
                                             SuccessRate=int(dataInfo[2]), LookingTime=int(dataInfo[3]),
                                             BlinkingFre=int(dataInfo[4]), PlanId=thisPlan, UserId=USER)
        elif (PlanType == "可用性测试"):
            Answers = info['QNaireInfo']
            surveyId = thisPlan.PlanTypeId
            thisSurvey = SurveyList.objects.get(SurveyId=surveyId)
            thisPaper = PaperList.objects.filter(UserId=USER, SurveyId=thisSurvey)
            if thisPaper.exists():
                print("您已填过该评估方案！不可重复填写！")
                messages.error(request, "您已填过该评估方案！不可重复填写！")
                return render(request, "evaPlan.html")
            else:
                # 增加一个填问卷的人
                surveyedNum = math.ceil((thisSurvey.SurveyUseNum * thisSurvey.SurveyPro) / 100)
                print(surveyedNum)
                surveyedNum = surveyedNum + 1
                print(surveyedNum)
                pro = surveyedNum * 100 / thisSurvey.SurveyUseNum
                print(pro)
                if (pro > 100):
                    pro = 100
                thisSurvey.SurveyPro = pro
                thisSurvey.save()

                PaperList.objects.create(UserId=USER, SurveyId=thisSurvey)
                thisPaper = PaperList.objects.get(UserId=USER, SurveyId=thisSurvey)
                for ans in Answers:
                    print(type(ans))
                    print(ans['queId'])
                    thisQuestion = QuestionList.objects.get(QuestionId=ans['queId'])
                    if ans['type'] == 'SingleChoose':  # 单选题
                        AnswerList.objects.create(QuestionType=1, PaperId=thisPaper,
                                                  QuestionId=thisQuestion)
                        thisAnswer = AnswerList.objects.get(QuestionType=1, PaperId=thisPaper,
                                                            QuestionId=thisQuestion)
                        SCAList.objects.create(ChoiceAnswer=ans['answer'], AnswerId=thisAnswer)
                    elif ans['type'] == 'MultiChoose':  # 多选题
                        AnswerList.objects.create(QuestionType=2, PaperId=thisPaper,
                                                  QuestionId=thisQuestion)
                        thisAnswer = AnswerList.objects.get(QuestionType=2, PaperId=thisPaper,
                                                            QuestionId=thisQuestion)
                        MCAanswers = ','.join(ans['answer'])
                        MCAList.objects.create(ChoiceAnswer=MCAanswers, ChoiceNum=len(ans['answer']),
                                               AnswerId=thisAnswer)
                    elif ans['type'] == 'FillInBlank':  # 填空题
                        AnswerList.objects.create(QuestionType=3, PaperId=thisPaper,
                                                  QuestionId=thisQuestion)
                        thisAnswer = AnswerList.objects.get(QuestionType=3, PaperId=thisPaper,
                                                            QuestionId=thisQuestion)
                        print(ans['answer'])
                        FIBAnswerList.objects.create(FIBAnswer=ans['answer'], AnswerId=thisAnswer)
                    elif ans['type'] == 'Scale':  # 量表题
                        AnswerList.objects.create(QuestionType=4, PaperId=thisPaper,
                                                  QuestionId=thisQuestion)
                        thisAnswer = AnswerList.objects.get(QuestionType=4, PaperId=thisPaper,
                                                            QuestionId=thisQuestion)
                        ScaleAnswerList.objects.create(DegreeAnswer=ans['answer'], AnswerId=thisAnswer)
                    elif ans['type'] == 'Paragraph':
                        print("段落")
        else:
            print("暂未开发")

    assessedNum = math.ceil((thisAssess.AssessUseNum * thisAssess.AssessPro) / 100)  # 向上取整
    assessedNum = assessedNum + 1
    assessPro = assessedNum * 100 / thisAssess.AssessUseNum
    if (assessPro > 100):
        assessPro = 100
    thisAssess.AssessPro = assessPro
    thisAssess.save()
    messages.success(request, "填写评估方案成功！")
    return render(request, "evaPlan.html")


#
def getAllPerformance():  # 全部评估数据的分析结果

    AllPerformance = PerformanceRecord.objects.all()
    meanerror = 0
    meanfinish = 0
    meansuccessrate = 0
    meanlookingtime = 0
    meanblinkingfre = 0
    ErrorRate = []
    FinishTime = []
    SuccessRate = []
    LookingTime = []
    BlinkingFre = []
    for performance in AllPerformance:
        if (performance.ErrorRate != 0):
            ErrorRate.append(performance.ErrorRate)
        if (performance.FinishTime != 0):
            FinishTime.append(performance.FinishTime)
        if (performance.SuccessRate != 0):
            SuccessRate.append(performance.SuccessRate)
        if (performance.LookingTime != 0):
            LookingTime.append(performance.LookingTime)
        if (performance.BlinkingFre != 0):
            BlinkingFre.append(performance.BlinkingFre)
    meanerror = numpy.mean(ErrorRate)
    meanfinish = numpy.mean(FinishTime)
    meansuccessrate = numpy.mean(SuccessRate)
    meanlookingtime = numpy.mean(LookingTime)
    meanblinkingfre = numpy.mean(BlinkingFre)
    AveragePerformanceData = {'ErrorRate': meanerror, 'FinishTime': meanfinish, 'SuccessRate': meansuccessrate,
                              'LookingTime': meanlookingtime, 'BlinkingFre': meanblinkingfre}
    return AveragePerformanceData


def AnalysisData(request):  # 分析评估数据
    assessId = json.loads(request.GET['assess'])
    thisAssess = AssessList.objects.get(AssessId=assessId)
    # 问卷
    if (thisAssess.AssessType == 0):
        print("单一问卷")
        myQNaireResults = []
        thisSurvey = SurveyList.objects.get(AssessId=assessId)
        myQNaireResults = analysisQNaire(thisSurvey)
        return render(request, "results2.html", {'AnswerList': json.dumps(myQNaireResults)})

    else:  # 综合评估
        thisPlans = PlanList.objects.filter(AssessId=thisAssess)
        HtmlPlanList = []
        allUseProblems = []
        QNaireResults = []
        ErrorRate = []
        FinishTime = []
        SuccessRate = []
        LookingTime = []
        BlinkingFre = []
        AssessAllUseProblems = []
        usernum = 0

        Efficiency = []  # 绩效
        Fatigue = []  # 疲劳度

        j = 1
        for plan in thisPlans:

            if plan.PlanTypeId == '启发式评估':
                temp = {"id": j, "PlanId": plan.PlanId, "PlanName": plan.PlanName, "PlanType": plan.PlanTypeId}
                HtmlPlanList.append(temp)
                j = j + 1
                # 列出可用性问题清单
                thisHeus = HeuEvaResult.objects.filter(PlanId=plan).order_by('-SeriousDegree')
                heucount = 1
                useProblems = []
                for heu in thisHeus:
                    tempHeu = {'id': heucount, 'serious': heu.SeriousDegree, 'problem': heu.HeuProblem,
                               'local': heu.Interface, 'advice': heu.Advice}
                    useProblems.append(tempHeu)
                    AssessAllUseProblems.append(tempHeu)
                    heucount = heucount + 1
                tempPlanHeu = {'PlanId': plan.PlanId, 'useProblems': useProblems}
                allUseProblems.append(tempPlanHeu)
            elif plan.PlanTypeId == '数据记录':
                temp = {"id": j, "PlanId": plan.PlanId, "PlanName": plan.PlanName, "PlanType": plan.PlanTypeId}
                HtmlPlanList.append(temp)
                j = j + 1
                # 算出平均值
                thisPerformance = PerformanceRecord.objects.filter(PlanId=plan)
                usernum = len(thisPerformance)
                for performance in thisPerformance:
                    if (performance.ErrorRate != 0):
                        ErrorRate.append(performance.ErrorRate)
                    if (performance.FinishTime != 0):
                        FinishTime.append(performance.FinishTime)
                    if (performance.SuccessRate != 0):
                        SuccessRate.append(performance.SuccessRate)
                    if (performance.LookingTime != 0):
                        LookingTime.append(performance.LookingTime)
                    if (performance.BlinkingFre != 0):
                        BlinkingFre.append(performance.BlinkingFre)
            elif (str(plan.PlanTypeId).isdigit()):  # 可用性测试
                temp = {"id": j, "PlanId": plan.PlanId, "PlanName": plan.PlanName, "PlanType": "可用性测试"}
                HtmlPlanList.append(temp)
                j = j + 1
                thisSurveyId = plan.PlanTypeId
                thisSurvey = SurveyList.objects.get(SurveyId=thisSurveyId)
                ResultsData = analysisQNaire(thisSurvey)
                tempQNairePlan = {'PlanId': plan.PlanId, 'ResultsData': ResultsData}
                QNaireResults.append(tempQNairePlan)
            else:
                print("主观量表，暂未开发")
        meanErrorRate = 0
        meanFinishTime = 0
        meanSuccessRate = 0
        meanLookingTime = 0
        meanBlinkingFre = 0
        maxErrorRate = 0
        maxFinishTime = 0
        maxSuccessRate = 0
        maxLookingTime = 0
        maxBlinkingFre = 0
        minErrorRate = 0
        minFinishTime = 0
        minSuccessRate = 0
        minLookingTime = 0
        minBlinkingFre = 0
        stdErrorRate = 0
        stdFinishTime = 0
        stdSuccessRate = 0
        stdLookingTime = 0
        stdBlinkingFre = 0
        cwsysErrorRate = ""
        cwstdErrorRate = ""
        cwsysFinishTime = ""
        cwstdFinishTime = ""
        cwsysSuccessRate = ""
        cwstdSuccessRate = ""
        cwsysLookingTime = ""
        cwstdLookingTime = ""
        cwsysBlinkingFre = ""
        cwstdBlinkingFre = ""

        if (len(ErrorRate) != 0):
            meanErrorRate = round(numpy.mean(ErrorRate), 2)
            stdErrorRate = round(numpy.std(ErrorRate, ddof=1), 2)
            maxErrorRate = max(ErrorRate)
            minErrorRate = min(ErrorRate)
        if (len(FinishTime) != 0):
            meanFinishTime = round(numpy.mean(FinishTime), 2)
            stdFinishTime = round(numpy.std(FinishTime), 2)
            maxFinishTime = max(FinishTime)
            minFinishTime = min(FinishTime)
        if (len(SuccessRate) != 0):
            meanSuccessRate = round(numpy.mean(SuccessRate), 2)
            stdSuccessRate = round(numpy.std(SuccessRate), 2)
            maxSuccessRate = max(SuccessRate)
            minSuccessRate = min(SuccessRate)
        if (len(LookingTime) != 0):
            meanLookingTime = round(numpy.mean(LookingTime), 2)
            stdLookingTime = round(numpy.std(LookingTime), 2)
            maxLookingTime = max(LookingTime)
            minLookingTime = min(LookingTime)
        if (len(BlinkingFre) != 0):
            meanBlinkingFre = round(numpy.mean(BlinkingFre), 2)
            stdBlinkingFre = round(numpy.std(BlinkingFre), 2)
            maxBlinkingFre = max(BlinkingFre)
            minBlinkingFre = min(BlinkingFre)

        AveragePerformanceData = getAllPerformance()
        print(AveragePerformanceData)
        StandardPerformanceData = IndexList.objects.filter(thisMethod="数据记录")
        for per in StandardPerformanceData:
            if (per.IndexName == "出错频率"):
                ErrorRatePer = -((meanErrorRate - per.Standard) / per.Standard)  # 出错频率表现
                Efficiency.append(ErrorRatePer)
                if (meanErrorRate > AveragePerformanceData['ErrorRate']):
                    cwsysErrorRate = "出错频率比评估系统内存储数据平均值高。"
                elif (meanErrorRate < AveragePerformanceData['ErrorRate']):
                    cwsysErrorRate = "出错频率比评估系统内存储数据平均值低。"
                if (meanErrorRate > per.Standard):  # 比标准值高
                    cwstdErrorRate = per.HigherAdvice
                elif (meanErrorRate < per.Standard):
                    cwstdErrorRate = per.LowerAdvice

            elif (per.IndexName == "完成时间"):
                FinishTimePer = -((meanFinishTime - per.Standard) / per.Standard)  # 完成时间表现
                Efficiency.append(FinishTimePer)
                if (meanFinishTime > AveragePerformanceData['FinishTime']):
                    cwsysFinishTime = "完成时间比评估系统内存储数据平均值高。"
                elif (meanFinishTime < AveragePerformanceData['FinishTime']):
                    cwsysFinishTime = "完成时间比评估系统内存储数据平均值低。"
                if (meanFinishTime > per.Standard):  # 比标准值高
                    cwstdFinishTime = per.HigherAdvice
                elif (meanFinishTime < per.Standard):
                    cwstdFinishTime = per.LowerAdvice

            elif (per.IndexName == "成功率"):
                SuccessRatePer = (meanSuccessRate - per.Standard) / per.Standard  # 成功率表现
                Efficiency.append(SuccessRatePer)
                if (meanSuccessRate > AveragePerformanceData['SuccessRate']):
                    cwsysSuccessRate = "成功率比评估系统内存储数据平均值高。"
                elif (meanSuccessRate < AveragePerformanceData['SuccessRate']):
                    cwsysSuccessRate = "成功率比评估系统内存储数据平均值低。"
                if (meanSuccessRate > per.Standard):  # 比标准值高
                    cwstdSuccessRate = per.HigherAdvice
                elif (meanSuccessRate < per.Standard):
                    cwstdSuccessRate = per.LowerAdvice
            elif (per.IndexName == "平均注视时间"):
                LookingTimePer = (meanLookingTime - per.Standard) / per.Standard  # 平均注视时间表现
                Fatigue.append(LookingTimePer)
                if (meanLookingTime > AveragePerformanceData['LookingTime']):
                    cwsysLookingTime = "平均注视时间比评估系统内存储数据平均值高。"
                elif (meanLookingTime < AveragePerformanceData['LookingTime']):
                    cwsysLookingTime = "平均注视时间比评估系统内存储数据平均值低。"
                if (meanLookingTime > per.Standard):  # 比标准值高
                    cwstdLookingTime = per.HigherAdvice
                elif (meanLookingTime < per.Standard):
                    cwstdLookingTime = per.LowerAdvice
            elif (per.IndexName == "眨眼频率"):
                BlinkingFrePer = (meanBlinkingFre - per.Standard) / per.Standard  # 眨眼频率表现
                Fatigue.append(BlinkingFrePer)
                if (meanBlinkingFre > AveragePerformanceData['BlinkingFre']):
                    cwsysBlinkingFre = "眨眼频率比评估系统内存储数据平均值高。"
                elif (meanBlinkingFre < AveragePerformanceData['BlinkingFre']):
                    cwsysBlinkingFre = "眨眼频率比评估系统内存储数据平均值低。"
                if (meanBlinkingFre > per.Standard):  # 比标准值高
                    cwstdBlinkingFre = per.HigherAdvice
                elif (meanBlinkingFre < per.Standard):
                    cwstdBlinkingFre = per.LowerAdvice

        meanEfficiency = 0
        meanFatigue = 0
        stdEfficiencyAdvice = ""
        stdFatigueAdvice = ""
        if (Efficiency != []):
            meanEfficiency = round(numpy.mean(Efficiency), 2)
            if (meanEfficiency > 0):
                stdEfficiencyAdvice = "该系统操作员绩效较高。"
            elif (meanEfficiency < 0):
                stdEfficiencyAdvice = "该系统操作员绩效较低。"
            else:
                stdEfficiencyAdvice = "该系统操作员绩效符合平均水平。"
        if (Fatigue != []):
            meanFatigue = round(numpy.mean(Fatigue), 2)
            if (meanFatigue > 0):
                stdFatigueAdvice = "该系统操作员疲劳度较高。"
            elif (meanFatigue < 0):
                stdFatigueAdvice = "该系统操作员疲劳度较低。"
            else:
                stdFatigueAdvice = "该系统操作员疲劳度符合平均水平。"

        HtmlSumInfoList = [{'name': '绩效', 'degree': meanEfficiency, 'Advice': stdEfficiencyAdvice},
                           {'name': '疲劳度', 'degree': meanFatigue, 'Advice': stdFatigueAdvice}]
        HtmlInfoList = [{'name': '出错频率', 'unit': '次/小时', 'meandata': meanErrorRate, 'stddata': stdErrorRate,
                         'maxdata': maxErrorRate, 'mindata': minErrorRate, 'SysAdvice': cwsysErrorRate,
                         'StdAdvice': cwstdErrorRate},
                        {'name': '完成时间', 'unit': '分钟', 'meandata': meanFinishTime, 'stddata': stdFinishTime,
                         'maxdata': maxFinishTime, 'mindata': minFinishTime, 'SysAdvice': cwsysFinishTime,
                         'StdAdvice': cwstdFinishTime},
                        {'name': '成功率', 'unit': '%', 'meandata': meanSuccessRate, 'stddata': stdSuccessRate,
                         'maxdata': maxSuccessRate, 'mindata': minSuccessRate, 'SysAdvice': cwsysSuccessRate,
                         'StdAdvice': cwstdSuccessRate},
                        {'name': '平均注视时间 ', 'unit': '毫秒', 'meandata': meanLookingTime, 'stddata': stdLookingTime,
                         'maxdata': maxLookingTime, 'mindata': minLookingTime, 'SysAdvice': cwsysLookingTime,
                         'StdAdvice': cwstdLookingTime},
                        {'name': '眨眼频率 ', 'unit': '次/分钟', 'meandata': meanBlinkingFre, 'stddata': stdBlinkingFre,
                         'maxdata': maxBlinkingFre, 'mindata': minBlinkingFre, 'SysAdvice': cwsysBlinkingFre,
                         'StdAdvice': cwstdBlinkingFre}]
        print(AssessAllUseProblems)
        Sorted_AssessAllUseProblems = AssessAllUseProblems.sort(key=lambda s: int(s['serious']), reverse=True)
        print("排序后")
        print(AssessAllUseProblems)
        return render(request, "EvaResult.html",
                      {'PlanList': HtmlPlanList, 'infoList': HtmlInfoList, 'SumInfoList': HtmlSumInfoList,
                       'QNaireResults': QNaireResults, 'allUseProblems': allUseProblems,
                       'AssessUseProblems': AssessAllUseProblems})
    return render(request, "chooseEva.html")


def setModel(request):
    assessId = json.loads(request.GET['assess'])
    thisAssess = AssessList.objects.get(AssessId=assessId)
    isModel = ModelList.objects.filter(AssessId=thisAssess)
    if isModel.exists():
        messages.error(request, "此评估已经是模板")
    else:
        # 刚存储时是综合和表单，有使用之后设为历史模板
        ModelList.objects.create(ModelType=thisAssess.AssessType, AssessId=thisAssess)
        print("设为模板成功")

    return render(request, "chooseEva.html")


# id:1,
# 		name:"历史模板名称1",
# 		InShort:"历史模板1一句话描述一句话描述",
# 		type:"history"

def getAllModels():
    Models = ModelList.objects.all()
    j = 0
    ModelsList = []
    for model in Models:

        if (model.AssessId.AssessType == 0):
            if (model.ModelType == 2):  # 历史
                temp = {'ModelId': model.ModelId, 'id': j, 'name': model.AssessId.AssessName,
                        'InShort': model.AssessId.AssessOneDes,
                        'type': 'list', 'isHistory': 'yes', 'AssessId': model.AssessId.AssessId}
                ModelsList.append(temp)
                j = j + 1
            else:
                temp = {'ModelId': model.ModelId, 'id': j, 'name': model.AssessId.AssessName,
                        'InShort': model.AssessId.AssessOneDes,
                        'type': 'list', 'isHistory': 'no', 'AssessId': model.AssessId.AssessId}
                ModelsList.append(temp)
                j = j + 1
        elif (model.AssessId.AssessType == 1):
            if (model.ModelType == 2):  # 历史
                temp = {'ModelId': model.ModelId, 'id': j, 'name': model.AssessId.AssessName,
                        'InShort': model.AssessId.AssessOneDes,
                        'type': 'coll', 'isHistory': 'yes', 'AssessId': model.AssessId.AssessId}
                ModelsList.append(temp)
                j = j + 1
            else:
                temp = {'ModelId': model.ModelId, 'id': j, 'name': model.AssessId.AssessName,
                        'InShort': model.AssessId.AssessOneDes,
                        'type': 'coll', 'isHistory': 'no', 'AssessId': model.AssessId.AssessId}
                ModelsList.append(temp)
                j = j + 1
    return ModelsList


def manageModel(request):
    HtmlModelList = getAllModels()
    return render(request, "manageModel.html", {'AllModel': HtmlModelList})


def deleteModel(request):  # 删除模板
    Messages = json.loads(request.body)
    ModelId = Messages['model']
    ModelList.objects.filter(ModelId=ModelId).delete()
    print("删除成功")
    return render(request, "manageModel.html")


def newEvaFromModel(request):  # 从模板新建
    originAssessId = request.POST.get("assessid", None)

    newAssessName = request.POST.get("name", None)
    newAssessDetail = request.POST.get("detail", None)
    newAssessUseNum = request.POST.get("person", None)
    global USER
    originAssess = AssessList.objects.get(AssessId=originAssessId)
    thisModel = ModelList.objects.get(AssessId=originAssess)
    thisModel.ModelType = 2  # 设为历史模板
    thisModel.save()
    if (originAssess.AssessType == 0):  # 是单一问卷
        AssessList.objects.create(AssessName=newAssessName, AssessOneDes=newAssessDetail, AssessPro=0, AssessType=0,
                                  AssessUseNum=newAssessUseNum, UserId=USER)
        thisAssess = AssessList.objects.get(AssessName=newAssessName, AssessOneDes=newAssessDetail, AssessPro=0,
                                            AssessType=0, AssessUseNum=newAssessUseNum, UserId=USER)
        SurveyList.objects.create(SurveyName=newAssessName, SurveyPro=0, SurveyUseNum=newAssessUseNum,
                                  AssessId=thisAssess)
        thisSurvey = SurveyList.objects.get(SurveyName=newAssessName, SurveyPro=0, SurveyUseNum=newAssessUseNum,
                                            AssessId=thisAssess)
        tempQNaire = {'name': thisSurvey.SurveyName, 'id': thisSurvey.SurveyId}
        HtmlQuestionsList = []  # 获取原有问题
        Survey = SurveyList.objects.get(AssessId=originAssess)
        Questions = QuestionList.objects.filter(SurveyId=Survey)
        print(type(Questions))
        j = 1
        for que in Questions:

            if que.QuestionType == 1:
                tempQue = {'id': j, 'queId': '', 'title': 'title', 'type': 'SingleChoose', 'ChooseA': '', 'ChooseB': '',
                           'ChooseC': '', 'ChooseD': '', "answer": ''}
                tempQue['queId'] = que.QuestionId
                tempQue['title'] = que.QueDescription
                choices = ChoiceList.objects.get(QuestionId=que)
                tempQue['ChooseA'] = choices.ChoiceA
                tempQue['ChooseB'] = choices.ChoiceB
                tempQue['ChooseC'] = choices.ChoiceC
                tempQue['ChooseD'] = choices.ChoiceD
                HtmlQuestionsList.append(tempQue)
                j = j + 1
            elif que.QuestionType == 2:
                tempQue = {'id': j, 'queId': '', 'title': 'title', 'type': 'MultiChoose', 'ChooseA': '', 'ChooseB': '',
                           'ChooseC': '', 'ChooseD': '', 'answer': []}
                tempQue['queId'] = que.QuestionId
                tempQue['title'] = que.QueDescription
                choices = ChoiceList.objects.get(QuestionId=que)
                tempQue['ChooseA'] = choices.ChoiceA
                tempQue['ChooseB'] = choices.ChoiceB
                tempQue['ChooseC'] = choices.ChoiceC
                tempQue['ChooseD'] = choices.ChoiceD
                HtmlQuestionsList.append(tempQue)
                j = j + 1
            elif que.QuestionType == 3:
                tempQue = {'id': j, 'queId': '', 'title': 'title', 'type': 'FillInBlank', 'answer': ''}
                tempQue['queId'] = que.QuestionId
                tempQue['title'] = que.QueDescription
                HtmlQuestionsList.append(tempQue)
                j = j + 1
            elif que.QuestionType == 4:
                tempQue = {'id': j, 'queId': '', 'title': 'title', 'type': 'Scale', 'lowest': 'lowest',
                           'highest': 'highest', 'ScaleCount': 0, 'answer': ''}
                tempQue['queId'] = que.QuestionId
                tempQue['title'] = que.QueDescription
                scale = ScaleList.objects.get(QuestionId=que)
                tempQue['lowest'] = scale.BeginIndex
                tempQue['highest'] = scale.EndIndex
                tempQue['ScaleCount'] = scale.DegreeNum
                HtmlQuestionsList.append(tempQue)
                j = j + 1
            elif que.QuestionType == 5:
                # "id": 3, "title": "嘻嘻嘻嘻", "type": "Paragraph"
                tempQue = {'id': j, 'queId': '', 'title': 'title', 'type': 'Paragraph'}
                tempQue['queId'] = que.QuestionId
                tempQue['title'] = que.QueDescription
                HtmlQuestionsList.append(tempQue)
                #j = j + 1
        print(HtmlQuestionsList)
        return render(request, "newQNaire.html", {'AllQuestions': HtmlQuestionsList, 'QNaire': tempQNaire})
    elif (originAssess.AssessType == 1):  # 是综合评估
        print(originAssess.AssessIndexId)
        MyIndexIdList = originAssess.AssessIndexId.split(";")
        print("从模板获取到的")
        print(MyIndexIdList)
        #print(len(originAssess.AssessIndexId))
        #print(len(MyIndexIdList))
        HtmlIndexList = getIndexInfo(MyIndexIdList)  # 获取了指标
        AssessList.objects.create(AssessName=newAssessName, AssessOneDes=newAssessDetail, AssessType=1,
                                  AssessUseNum=newAssessUseNum,
                                  UserId=USER)
        thisAssess = AssessList.objects.get(AssessName=newAssessName, AssessOneDes=newAssessDetail, AssessType=1,
                                            AssessUseNum=newAssessUseNum,
                                            UserId=USER)
        # 获取指标信息
        Assess = {'AssessId': thisAssess.AssessId, 'AssessName': thisAssess.AssessName}
        return render(request, "edit1.html",
                      {'Assess': Assess, 'IndexInfo': HtmlIndexList, 'ModelId': originAssess.AssessId})
    print("到这儿了")
    return render(request, 'newEva.html')


def fuzzySearch(userInput):
    AllAssessList = AssessList.objects.all()
    AllCollection = []  # 包含所有评估名称、一句话描述和具体描述
    for assess in AllAssessList:
        AllCollection.append(assess.AssessName)
        if (assess.AssessDes != None):
            AllCollection.append(assess.AssessDes)
        if (assess.AssessOneDes != None):
            AllCollection.append(assess.AssessOneDes)
    print(userInput)
    print(AllCollection)
    resultList = fuzzyfinder(str(userInput), AllCollection)
    resultAssess = []
    j = 0
    tempeva = {'id': 0, 'name': '', 'person': '', 'InShort': '', 'BeginTime': '', 'process': '', 'condition': ''}
    # print("result!!!!")
    # print(resultList)
    AllAssess = AssessList.objects.all().select_related()
    for result in resultList:
        NameAssess = []
        OneDesAssess = []
        DesAssess = []
        for assess in AllAssess:
            if (assess.AssessName == result):
                NameAssess.append(assess)
            if (assess.AssessOneDes == result):
                OneDesAssess.append(assess)
            if (assess.AssessDes == result):
                DesAssess.append(assess)
        # print(result)
        if len(NameAssess) != 0:
            for nameeva in NameAssess:
                tempeva = {'id': 0, 'name': '', 'person': '', 'InShort': '', 'BeginTime': '', 'process': '',
                           'condition': ''}
                tempeva['id'] = nameeva.AssessId
                tempeva['name'] = nameeva.AssessName
                tempeva['person'] = nameeva.UserId.UserName
                tempeva['InShort'] = nameeva.AssessOneDes
                tempeva['BeginTime'] = str(nameeva.AssessBeginTime)[0:16]
                tempeva['process'] = nameeva.AssessPro
                if nameeva.AssessPro < 100:
                    tempeva['condition'] = 'ing'
                else:
                    tempeva['condition'] = 'End'
                # print(tempeva)
                resultAssess.append(tempeva)
        if len(OneDesAssess) != 0:
            for onedeseva in OneDesAssess:
                tempeva = {'id': 0, 'name': '', 'person': '', 'InShort': '', 'BeginTime': '', 'process': '',
                           'condition': ''}
                tempeva['id'] = onedeseva.AssessId
                tempeva['name'] = onedeseva.AssessName
                tempeva['person'] = onedeseva.UserId.UserName
                tempeva['InShort'] = onedeseva.AssessOneDes
                tempeva['BeginTime'] = str(onedeseva.AssessBeginTime)[0:16]
                tempeva['process'] = onedeseva.AssessPro
                if onedeseva.AssessPro < 100:
                    tempeva['condition'] = 'ing'
                else:
                    tempeva['condition'] = 'End'
                resultAssess.append(tempeva)
                # print(tempeva)
        if len(DesAssess) != 0:
            for deseva in DesAssess:
                tempeva = {'id': 0, 'name': '', 'person': '', 'InShort': '', 'BeginTime': '', 'process': '',
                           'condition': ''}
                tempeva['id'] = deseva.AssessId
                tempeva['name'] = deseva.AssessName
                tempeva['person'] = deseva.UserId.UserName
                tempeva['InShort'] = deseva.AssessOneDes
                tempeva['BeginTime'] = str(deseva.AssessBeginTime)[0:16]
                tempeva['process'] = deseva.AssessPro
                if deseva.AssessPro < 100:
                    tempeva['condition'] = 'ing'
                else:
                    tempeva['condition'] = 'End'
                # print(tempeva)
                resultAssess.append(tempeva)
    global USER
    # print(resultAssess)
    resultAssess = [dict(t) for t in set([tuple(d.items()) for d in resultAssess])]  # 去重
    return resultAssess


def searchAssess(request):
    print(request.GET['userinput'])
    userInput = request.GET['userinput']
    resultAssess = fuzzySearch(userInput)

    global USER
    if (USER.SearchHistory != None):
        USER.SearchHistory = USER.SearchHistory + ";" + userInput
    else:
        USER.SearchHistory = userInput
    USER.save()
    tempUser = {'userid': USER.UserId, 'username': USER.UserName, 'userStatus': USER.Status}
    HtmlAssessNameList = []
    AssessNameList = AssessList.objects.all().values('AssessName')
    for assessname in AssessNameList:
        HtmlAssessNameList.append(assessname['AssessName'])
    WCResults = getAllSearchData()
    recommend = getUserRecommend()
    return render(request, 'chooseEva.html',
                  {'EvaList': resultAssess, 'User': tempUser, 'AssessNameList': HtmlAssessNameList,
                   'WCResults': WCResults, 'Recommend': recommend})


def fuzzyfinder(user_input, collection):
    suggestions = []
    pattern = '.*?'.join(user_input)  # Converts 'djm' to 'd.*?j.*?m'
    regex = re.compile(pattern)  # Compiles a regex.
    for item in collection:
        # print(type(item))
        match = regex.search(item)  # Checks if the current item matches the regex.
        if match:
            suggestions.append((len(match.group()), match.start(), item))
    return [x for _, _, x in sorted(suggestions)]

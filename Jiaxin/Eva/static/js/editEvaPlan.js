var SingleChoose = {
    id: 0,
    title: "xxx",
    type: "SingleChoose",
    ChooseA: "xxx",
    ChooseB: "xxx",
    ChooseC: "xxx",
    ChooseD: "xxx"
}


var MultiChoose = {
    id: 0,
    title: "xxx",
    type: "MultiChoose",
    ChooseA: "xxx",
    ChooseB: "xxx",
    ChooseC: "xxx",
    ChooseD: "xxx"
}

var FillInBlank = {
    id: 0,
    title: "xxx",
    type: "FillInBlank",
}

var ScaleGraph = {
    id: 0,
    title: "xxx",
    type: "Scale",
    lowest: "xxx",
    highest: "xxx",
    ScaleCount: 5
}

var Paragraph = {
    id: 0,
    title: "xxx",
    type: "Paragraph"
}


var UseTable = {
    id: 1,
    local: "",
    problem: "",
    serious: "",
    advice: ""

};
/*var PlanList=[
{
    id:1,
    PlanId:"1123",
    PlanName:"方案一一一一",
    PlanType:"启发式评估"
},
{
    id:2,
    PlanId:"1124",
    PlanName:"方案二二二二",
    PlanType:"可用性测试"
},
{
    id:3,
    PlanId:"1144",
    PlanName:"方案三三三三",
    PlanType:"数据收集"
},
{
    id:4,
    PlanId:"1129",
    PlanName:"方案四四四四",
    PlanType:"数据收集"
},
{
    id:5,
    PlanId:"34342",
    PlanName:"方案五五五五",
    PlanType:"启发式评估"
},
{
    id:6,
    PlanId:"1123456",
    PlanName:"方案六六六六",
    PlanType:"可用性测试"


}
]
*/
var Info = [

    {
        name: "出错频率",
        unit: "次/小时",
        value: ""
    },
    {
        name: "完成时间",
        unit: "分钟",
        value: ""
    },
    {
        name: "成功率",
        unit: "%",
        value: ""
    },
    {
        name: "平均操作注视时间",
        unit: "毫秒",
        value: ""
    },
    {
        name: "眨眼频率",
        unit: "次/分钟",
        value: ""

    }
]
/*
var QNaires=[
{
	Planid:"1124",
	Question:[ { "id": 1, "title": "丁程鑫帅不帅", "type": "SingleChoose", "ChooseA": "超帅", "ChooseB": "特别帅", "ChooseC": "帅炸了", "ChooseD": "巨帅","answer":""}, { "id": 2, "title": "李汶翰能不能出道", "type": "MultiChoose", "ChooseA": "C位出道", "ChooseB": "必须top", "ChooseC": "一位必须的", "ChooseD": "当然可以","answer":[]}, { "id": 3, "title": "嘻嘻嘻嘻", "type": "Paragraph" }, { "id": 4, "title": "爱不爱我", "type": "Scale", "lowest": "不爱", "highest": "爱", "ScaleCount": 5,"answer":"" }, { "id": 5, "title": "你猜我是谁", "type": "FillInBlank","answer":"" } ]
},
{
	Planid:"1123456",
	Question:[ { "id": 1, "title": "丁程鑫帅不帅", "type": "SingleChoose", "ChooseA": "超帅", "ChooseB": "特别帅", "ChooseC": "帅炸了", "ChooseD": "巨帅","answer":""}, { "id": 2, "title": "李汶翰能不能出道", "type": "MultiChoose", "ChooseA": "C位出道", "ChooseB": "必须top", "ChooseC": "一位必须的", "ChooseD": "当然可以","answer":[]}, { "id": 3, "title": "嘻嘻嘻嘻", "type": "Paragraph" }, { "id": 4, "title": "爱不爱我", "type": "Scale", "lowest": "不爱", "highest": "爱", "ScaleCount": 5,"answer":"" }, { "id": 5, "title": "你猜我是谁", "type": "FillInBlank","answer":"" } ]
}
]*/

var app = new Vue({
    el: '#app',
    data: {
        Assess: Assess,
        plans: PlanList,
        OneUseTable: UseTable,
        UseTables: [],
        InfoList: Info,
        SaveInfo: [],
        AllInfo: [],
        activePlan: 1,
        questions: [],
        SChoose: SingleChoose,
        MChoose: MultiChoose,
        FIB: FillInBlank,
        Scale: ScaleGraph,
        Para: Paragraph,
        QNaires: QNaires,
        PlanInfoName: ""

    },
    mounted() {
        this.clickPlan(1);
    },
    methods: {
        clickPlan: function (id) {


            for (var i = 0; i < this.plans.length; i++) {

                if (id == this.plans[i].id) {
                    this.activePlan = id;
                    if (this.plans[i].PlanType == "启发式评估") {
                        this.UseTables = [];
                        this.initialTable();

                        document.getElementById('HeuInfo').style.visibility = "visible";
                        document.getElementById('Information').style.visibility = "hidden";
                        document.getElementById('QNaire').style.visibility = "hidden";
                        document.getElementById('modelQNaire').style.visibility = "hidden";
                    } else if (this.plans[i].PlanType == "数据记录") {
                        this.PlanInfoName = this.plans[i].PlanName.substring(2).split('的')[0];
                        console.log(this.PlanInfoName);

                        for (var d = 0; d < this.InfoList.length; d++) {
                            this.InfoList[d].value = "";
                        }

                        document.getElementById('HeuInfo').style.visibility = "hidden";
                        document.getElementById('Information').style.visibility = "visible";
                        document.getElementById('QNaire').style.visibility = "hidden";
                        document.getElementById('modelQNaire').style.visibility = "hidden";

                    } else if (this.plans[i].PlanType == "可用性测试") {
                        this.questions = [];
                        for (var q = 0; q < this.QNaires.length; q++) {
                            if (this.QNaires[q].PlanId == this.plans[i].PlanId) {
                                console.log("问卷匹配到了");
                                this.questions = this.QNaires[q].Question;
                                break;
                            }
                        }
                        document.getElementById('HeuInfo').style.visibility = "hidden";
                        document.getElementById('Information').style.visibility = "hidden";
                        document.getElementById('QNaire').style.visibility = "visible";
                        document.getElementById('modelQNaire').style.visibility = "hidden";
                    } else if (this.plans[i].PlanType == "主观感知") {
                        document.getElementById('HeuInfo').style.visibility = "hidden";
                        document.getElementById('Information').style.visibility = "hidden";
                        document.getElementById('QNaire').style.visibility = "hidden";
                        document.getElementById('modelQNaire').style.visibility = "visible";
                    }
                }
            }
        },

        /*initialInfo:function()
        {//为什么会覆盖啊啊啊啊啊啊啊啊啊啊啊啊啊
            for (var i=0;i<Info.length;i++)
            {
                var item={};
                item.name=Info[i].name;
                item.unit=Info[i].unit;
                item.value="";

                this.SaveInfo.
            }



        }
        ,*/
        initialTable: function () {
            var item = {};
            item.id = 1;
            item.local = "";
            item.problem = "";
            item.serious = "";
            item.advice = "";
            this.OneUseTable = item;
            this.UseTables.push(this.OneUseTable);
        },
        newTable: function () {
            var item = {};
            item.id = this.UseTables.length + 1;
            item.local = "";
            item.problem = "";
            item.serious = "";
            item.advice = "";
            this.OneUseTable = item;
            this.UseTables.push(this.OneUseTable);
        },
        addSingleChoose: function () {

            var item = {};
            console.log(app.questions.length);
            QuestionId=1;
            for(var qi=0;qi<app.questions.length;qi++)
            {
                if(app.questions[qi].type!="Paragraph")
                {
                    QuestionId=QuestionId+1;
                }
            }
            //item.id = app.questions.length + 1;
            item.id=QuestionId;
            item.title = "";
            item.type = "SingleChoose";
            item.ChooseA = "";
            item.ChooseB = "";
            item.ChooseC = "";
            item.ChooseD = "";
            this.SChoose = item;
            app.questions.push(this.SChoose);
            console.log(this.SChoose);
            console.log(app.questions);
        },

        addMultiChoose: function () {
            var item = {};
            QuestionId=1;
            for(var qi=0;qi<app.questions.length;qi++)
            {
                if(app.questions[qi].type!="Paragraph")
                {
                    QuestionId=QuestionId+1;
                }
            }
            //item.id = app.questions.length + 1;
            item.id=QuestionId;
            item.title = "";
            item.type = "MultiChoose";
            item.ChooseA = "";
            item.ChooseB = "";
            item.ChooseC = "";
            item.ChooseD = "";
            this.MChoose = item;
            app.questions.push(this.MChoose);
        },

        addFillInBlank: function () {
            var item = {};
            QuestionId=1;
            for(var qi=0;qi<app.questions.length;qi++)
            {
                if(app.questions[qi].type!="Paragraph")
                {
                    QuestionId=QuestionId+1;
                }
            }
            //item.id = app.questions.length + 1;
            item.id=QuestionId;
            item.title = "";
            item.type = "FillInBlank";
            this.FIB = item;
            app.questions.push(this.FIB);
        },

        addScale: function () {
            var item = {};
            QuestionId=1;
            for(var qi=0;qi<app.questions.length;qi++)
            {
                if(app.questions[qi].type!="Paragraph")
                {
                    QuestionId=QuestionId+1;
                }
            }
            //item.id = app.questions.length + 1;
            item.id=QuestionId;
            item.title = "";
            item.type = "Scale";
            item.lowest = "";
            item.highest = "";
            item.ScaleCount = 5;
            this.ScaleGraph = item;
            app.questions.push(this.ScaleGraph);
        },

        addParagraph: function () {
            var item = {};
            item.id = app.questions.length + 1;
            item.title = "";
            item.type = "Paragraph";
            this.Para = item;
            app.questions.push(this.Para);
        },

        deleteQuestion: function (item) {
            var index = -1;
            //console.log("进来"+item.id+"题目"+item.title);

            for (var i = 0; i < app.questions.length; i++) {
                if (item.id == app.questions[i].id) {
                    index = i;
                }
            }
            if (index > -1) {
                for (var i = index; i < app.questions.length; i++) {
                    nowid = app.questions[i].id;
                    //console.log(nowid);
                    app.questions[i].id = nowid - 1;
                    //console.log(app.questions[i].id);
                }
                //console.log("查找"+app.questions[index].id+"题目"+app.questions[index].title);
                app.questions.splice(index, 1);

                console.log("删除成功");

            }
        },
        displayPreview: function () {
            console.log("预览！");
            if (showDiv = document.getElementById('previewDiv').style.display == 'none') {
                console.log("get到了！");
                //document.getElementById('zhezhao').style.height=document.getElementById('questions').height;
                document.getElementById('zhezhao').style.display = 'block';
                document.getElementById('previewDiv').style.display = 'block';

            }

        },

        closePreview: function () {
            if (showDiv = document.getElementById('previewDiv').style.display == 'block') {

                document.getElementById('zhezhao').style.display = 'none';
                document.getElementById('previewDiv').style.display = 'none';

            }

        },
        saveQNaire: function () {
            var activePlanId = 0;
            for (var plancount = 0; plancount < this.plans.length; plancount++) {
                if (this.activePlan == this.plans[plancount].id) {
                    activePlanId = this.plans[plancount].PlanId;
                }
            }
            for (var i = 0; i < this.QNaires.length; i++) {

                if (this.QNaires[i].PlanId == activePlanId) {

                    this.QNaires.splice(i, 1);//删除此元素 在之后重新保存
                    break;
                }
            }
            for (var i = 0; i < this.plans.length; i++) {
                if (this.activePlan == this.plans[i].id) {
                    var tempQNaire = {};
                    tempQNaire.id = this.plans[i].id;
                    tempQNaire.PlanId = this.plans[i].PlanId;
                    tempQNaire.Question = this.questions;
                    this.QNaires.push(tempQNaire);
                }
            }
            alert("增加问卷成功！");
            console.log(this.QNaires, length);
            console.log(this.QNaires);
        },
        postPlan: function () {
            axios.post('/savePlanQNaire/',

                JSON.stringify({
                    QNaires: this.QNaires
                }))
                .then(function (response) {
                    alert("增加方案成功！")
                    window.location.href = '/chooseEva/'
                    console.log(response);
                })
                .catch(function (error) {
                    console.log(error);
                    alert("增加方案失败！")
                })
        }

    }

})



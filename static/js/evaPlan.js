var UseTable = {
    id: 1,
    local: "",
    problem: "",
    serious: "",
    advice: ""

};
/*
var PlanList=[
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
        name: "平均注视时间",
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
	Question:[ { "id": 1, "title": "李汶翰帅不帅", "type": "SingleChoose", "ChooseA": "超帅", "ChooseB": "特别帅", "ChooseC": "帅炸了", "ChooseD": "巨帅","answer":""}, { "id": 2, "title": "李汶翰能不能出道", "type": "MultiChoose", "ChooseA": "C位出道", "ChooseB": "必须top", "ChooseC": "一位必须的", "ChooseD": "当然可以","answer":[]}, { "id": 3, "title": "嘻嘻嘻嘻", "type": "Paragraph" }, { "id": 4, "title": "爱不爱我", "type": "Scale", "lowest": "不爱", "highest": "爱", "ScaleCount": 5,"answer":"" }, { "id": 5, "title": "你猜我是谁", "type": "FillInBlank","answer":"" } ]
}
]
*/
var app = new Vue({
    el: '#app',
    data: {
        plans: PlanList,
        OneUseTable: UseTable,
        UseTables: [],
        InfoList: Info,
        AllInfo: [],
        activePlan: 1,
        AllQNaires: QNaires,
        questions: [],
        readOnly: readOnly,
        HeuRegular: "",
        HeuRegulars: HeuRegulars,
        PlanInfoName: ""

    },
    mounted() {
        this.clickPlan(1);
    },
    methods: {
        saveNowPlan: function () {
            //之前有没有保存过 是重新编辑的
            for (var a = 0; a < this.AllInfo.length; a++) {
                if (this.AllInfo[a].id == this.activePlan) {
                    console.log("删了一个")
                    this.AllInfo.splice(a, 1);//删除此元素 在之后重新保存
                    break;
                }
            }
            //保存当前正在填写的
            for (var j = 0; j < this.plans.length; j++) {
                if (this.activePlan == this.plans[j].id) {

                    if (this.plans[j].PlanType == "启发式评估") {

                        if (this.UseTables.length == 1) {
                            if (this.UseTables[0].problem == "") {
                                console.log("启发式为空！")
                            } else {
                                var tempUse = {
                                    "id": this.activePlan,
                                    "Planid": this.plans[j].PlanId,
                                    "PlanType": "启发式评估",
                                    "UseTables": this.UseTables
                                };
                                this.AllInfo.push(tempUse);
                                alert("保存成功！");
                            }
                        } else {
                            var tempUse = {
                                "id": this.activePlan,
                                "Planid": this.plans[j].PlanId,
                                "PlanType": "启发式评估",
                                "UseTables": this.UseTables
                            };
                            this.AllInfo.push(tempUse);
                            alert("保存成功！");
                        }
                    } else if (this.plans[j].PlanType == "数据记录") {

                        this.PlanInfoName = this.plans[j].PlanName.substring(2).split('的')[0];
                        console.log(this.PlanInfoName);
                        //var SaveInfo=[];
                        thisInfoStr = "";
                        for (var il = 0; il < this.InfoList.length; il++) {
                            if (this.InfoList[il].value == "") {
                                this.InfoList[il].value = 0;
                            }
                            if (thisInfoStr == "") {
                                thisInfoStr = "" + this.InfoList[il].value;
                            } else {

                                thisInfoStr = thisInfoStr + "," + this.InfoList[il].value
                            }
                        }

                        var tempInfo = {
                            "id": this.activePlan,
                            "Planid": this.plans[j].PlanId,
                            "PlanType": "数据记录",
                            "myInfo": thisInfoStr
                        }


                        //var tempInfo={"id":this.activePlan,"Planid":this.plans[j].PlanId,"PlanType":"数据收集","myInfo":SaveInfo};
                        this.AllInfo.push(tempInfo);
                        alert("保存成功！");
                    } else if (this.plans[j].PlanType == "可用性测试") {
                        AllAnswer = true;
                        for (var tq = 0; tq < this.questions.length; tq++) {
                            if (this.questions[tq].answer == "") {
                                AllAnswer = false;
                            }
                        }
                        if (AllAnswer) {
                            var tempQNaire = {
                                "id": this.activePlan,
                                "Planid": this.plans[j].PlanId,
                                "PlanType": "可用性测试",
                                "QNaireInfo": this.questions
                            }
                            this.AllInfo.push(tempQNaire);
                            alert("保存成功！");
                        } else {
                            alert("您仍有问题未填写！");
                        }


                    } else {
                        console.log("暂未开发");
                    }
                }
            }


            /*console.log("AllInfo：");
            console.log(this.AllInfo.length);
            for(var k=0;k<this.AllInfo.length;k++)
            {

                console.log(this.AllInfo[k].Planid);
                console.log(this.AllInfo[k]);
            }*/


        },
        clickPlan: function (id) {


            for (var i = 0; i < this.plans.length; i++) {

                if (id == this.plans[i].id) {
                    this.activePlan = id;
                    if (this.plans[i].PlanType == "启发式评估") {
                        for (var h = 0; h < this.HeuRegulars.length; h++) {
                            if (this.HeuRegulars[h].PlanId == this.plans[i].PlanId) {
                                this.HeuRegular = this.HeuRegulars[h].HeuRegular;
                            }
                        }
                        this.UseTables = [];
                        this.initialTable();
                        for (var a = 0; a < this.AllInfo.length; a++) {
                            if (this.AllInfo[a].id == this.activePlan) {
                                console.log("匹配到了!");

                                this.UseTables = this.AllInfo[a].UseTables;
                            }
                        }


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
                        //this.initialInfo();

                        for (var a = 0; a < this.AllInfo.length; a++) {

                            if (this.AllInfo[a].id == this.activePlan) {
                                console.log("匹配到了!");
                                console.log(this.AllInfo[a].myInfo);
                                var InfoResult = [];
                                InfoResult = this.AllInfo[a].myInfo.split(',');
                                //console.log(this.SaveInfo);
                                for (var iR = 0; iR < this.InfoList.length; iR++) {
                                    this.InfoList[iR].value = InfoResult[iR];
                                }
                                //this.InfoList=this.AllInfo[a].myInfo;
                                console.log(this.InfoList);
                            }
                        }
                        document.getElementById('HeuInfo').style.visibility = "hidden";
                        document.getElementById('Information').style.visibility = "visible";
                        document.getElementById('QNaire').style.visibility = "hidden";
                        document.getElementById('modelQNaire').style.visibility = "hidden";

                    } else if (this.plans[i].PlanType == "可用性测试") {

                        for (var q = 0; q < this.AllQNaires.length; q++) {
                            if (this.AllQNaires[q].PlanId == this.plans[i].PlanId) {
                                this.questions = this.AllQNaires[q].Question;
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
            for (var iInfo=0;iInfo<Info.length;iInfo++)
            {
                var item={};
                item.name=Info[iInfo].name;
                item.unit=Info[iInfo].unit;
                item.value="";

                this.InfoList.push(item);
            }
            this.SaveInfo.push(this.InfoList);

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
        postInfo: function () {
            if (readOnly == 1) {
                alert("您处于模板查看只读状态，无法提交！");
            } else {
                axios.post('/getEvaAnswer/',

                    JSON.stringify({
                        Assess: Assess,
                        AllInfo: this.AllInfo
                    }))
                    .then(function (response) {
                        alert("保存成功！")
                        window.location.href = '/chooseEva/'
                        console.log(response);


                    })
                    .catch(function (error) {
                        console.log(error);
                        alert("保存失败！")
                    })
            }
        }


    }

})




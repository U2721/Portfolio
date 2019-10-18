/*
	var AllModel=[
	{
		id:1,
		name:"历史模板名称1",
		InShort:"历史模板1一句话描述一句话描述",
		type:"history"
	},
	{
		id:2,
		name:"综合模板名称2",
		InShort:"综合模板2一句话描述一句话描述",
		type:"coll"
	},
	{
		id:3,
		name:"表单名称3",
		InShort:"表单3一句话描述一句话描述",
		type:"list"	
	},
	{
		id:4,
		name:"表单名称4",
		InShort:"表单3一句话描述一句话描述",
		type:"list"
	},
	{
		id:5,
		name:"历史模板名称1",
		InShort:"历史模板1一句话描述一句话描述",
		type:"history"
	},
	{
		id:6,
		name:"历史模板历史2",
		InShort:"历史模板2一句话描述一句话描述",
		type:"history"
	},
	{
		id:7,
		name:"综合模板3",
		InShort:"综合模板3一句话描述一句话描述",
		type:"coll"
	},
	{
		id:8,
		name:"历史模板4",
		InShort:"历史模板3一句话描述一句话描述",
		type:"history"
	}

	]; */


var app = new Vue({
    el: '#app',
    data: {
        Models: AllModel,
        chooseModel: {begin: 'true'},
        User: User,
        newEva: {name: '', des: '', person: ""}

    },
    methods: {
        /*点击从空白处新建评估弹框*/
        newFromWhite: function () {

            if (document.getElementById('shadow').style.visibility == 'hidden' && document.getElementById('newEvaBox').style.visibility == 'hidden') {
                document.getElementById('shadow').style.visibility = 'visible';
                document.getElementById('newEvaBox').style.visibility = 'visible';
            }
        },
        closeNewBox: function () {

            document.getElementById('shadow').style.visibility = 'hidden';
            document.getElementById('newEvaBox').style.visibility = 'hidden';
            document.getElementById('newModelBox').style.visibility = 'hidden';
            location.href = '/newEva/';
        },
        RadioVaild: function () {
            var result = false;
            var radios = document.getElementsByName("eva");
            for (var i = 0; i < radios.length; i++) {
                if (radios[i].checked) {
                    result = true;
                }
            }
            return result;
        },
        submitForm: function () {

            if (document.getElementById('EvaNameInput').value == "") {
                alert("名称不能为空！")
            } else if (!this.RadioVaild()) {
                alert("请选择评估类型！")
            } else if (document.getElementById('EvaPersonNum').value == "" || isNaN(document.getElementById('EvaPersonNum').value) == true) {
                alert("请输入正确的参与人数！")
            } else {
                console.log("提交了！")
                document.BlankEva.submit();
            }
        },
        changeList: function () {
            document.getElementById('AllModelEvaluation').style.visibility = "hidden";
            document.getElementById('ListEvaluation').style.visibility = "visible";
            document.getElementById('CollEvaluation').style.visibility = "hidden";
            document.getElementById('HistoryEvaluation').style.visibility = "hidden";
        },
        changeHistory() {
            document.getElementById('AllModelEvaluation').style.visibility = "hidden";
            document.getElementById('ListEvaluation').style.visibility = "hidden";
            document.getElementById('CollEvaluation').style.visibility = "hidden";
            document.getElementById('HistoryEvaluation').style.visibility = "visible";
        },
        changeColl: function () {
            document.getElementById('AllModelEvaluation').style.visibility = "hidden";
            document.getElementById('ListEvaluation').style.visibility = "hidden";
            document.getElementById('CollEvaluation').style.visibility = "visible";
            document.getElementById('HistoryEvaluation').style.visibility = "hidden";
        },
        changeAll: function () {
            document.getElementById('AllModelEvaluation').style.visibility = "visible";
            document.getElementById('ListEvaluation').style.visibility = "hidden";
            document.getElementById('CollEvaluation').style.visibility = "hidden";
            document.getElementById('HistoryEvaluation').style.visibility = "hidden";
        },
        newFromModel: function (model) {
            console.log(this.chooseModel)
            this.$set(this.chooseModel, 'AssessId', model.AssessId);
            this.$set(this.chooseModel, 'ModelId', model.ModelId)
            this.$set(this.chooseModel, 'name', model.name);
            if (model.type == 'coll') {
                this.$set(this.chooseModel, 'type', '综合');
            } else if (model.type == 'list') {
                this.$set(this.chooseModel, 'type', '单一问卷');
            }


            if (document.getElementById('shadow').style.visibility == 'hidden' && document.getElementById('newModelBox').style.visibility == 'hidden') {
                document.getElementById('shadow').style.visibility = 'visible';
                document.getElementById('newModelBox').style.visibility = 'visible';
            }

        },
        submitFromModel: function () {
            /* axios.post('/newEvaFromModel/',
                     JSON.stringify({
                     Model:this.chooseModel,
                     newAssess:this.newEva
                         ////////////////底下未改呢！

                 }))
                     .then(function(response){
                         console.log(response);
                         //window.location.href='/chooseEva/'
                     })
                     .catch(function(error){
                         console.log(error);
                     })*/

            if (document.getElementById('ModelEvaNameInput').value == "") {
                alert("名称不能为空！")
            } else if (document.getElementById('ModelEvaPerson').value == "" || isNaN(document.getElementById('ModelEvaPerson').value) == true) {
                alert("请输入正确的参与人数！")
            } else {

                document.ModelEva.submit();
            }

        }


    }
})



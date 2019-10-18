
	var List=["方案一一一一","方案二二二二","方案三三三三","方案四四四四","方案五五五五"];
	//var Question=[ { "id": 1, "title": "丁程鑫帅不帅", "type": "SingleChoose", "ChooseA": "超帅", "ChooseB": "特别帅", "ChooseC": "帅炸了", "ChooseD": "巨帅" }, { "id": 2, "title": "李汶翰能不能出道", "type": "MultiChoose", "ChooseA": "C位出道", "ChooseB": "必须top", "ChooseC": "一位必须的", "ChooseD": "当然可以" }, { "id": 3, "title": "嘻嘻嘻嘻", "type": "Paragraph" }, { "id": 4, "title": "爱不爱我", "type": "Scale", "lowest": "不爱", "highest": "爱", "ScaleCount": 5 }, { "id": 5, "title": "你猜我是谁", "type": "FillInBlank" } ];


	var preview=new Vue({
		el:'#previewDiv',
		data: {
			questions: Question,
			surveyId: SurveyId,
			readOnly:readOnly
		},
		methods:{
			submitQNaire:function () {
				if(readOnly==1)
				{
					alert("您处于模板查看只读状态，无法提交！");
				}
				else {
					var AllAnswer=true;
					for(var tq=0;tq<this.questions.length;tq++)
						{
							if(this.questions[tq].answer=="")
							{
								AllAnswer=false;
							}
						}
					if(AllAnswer) {

						axios.post('/FillQNaire/',

							JSON.stringify({
								AllQuestions: this.questions,
								Survey: this.surveyId

							}))
							.then(function (response) {
								alert("保存成功，感谢您的填写！");
								window.location.href = '/chooseEva/'
								console.log(response);
							})
							.catch(function (error) {
								window.location.href = '/chooseEva/';
								console.log(error);
							})
					}
					else {
						alert("您仍有问题未填写！");
					}
				}
			}
		}
	})

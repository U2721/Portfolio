/*
import axios from 'axios'

axios.defaults.baseURL = 'http://localhost:8000'
Vue.prototype.$axios = axios
*/
	var SingleChoose={
		id:0,
		title:"xxx",
		type:"SingleChoose",
		ChooseA:"xxx",
		ChooseB:"xxx",
		ChooseC:"xxx",
		ChooseD:"xxx"
	}




	var MultiChoose={
		id:0,
		title:"xxx",
		type:"MultiChoose",
		ChooseA:"xxx",
		ChooseB:"xxx",
		ChooseC:"xxx",
		ChooseD:"xxx"
	}

	var FillInBlank={
		id:0,
		title:"xxx",
		type:"FillInBlank",	
	}

	var ScaleGraph={
		id:0,
		title:"xxx",
		type:"Scale",
		lowest:"xxx",
		highest:"xxx",
		ScaleCount:5
	}

	var Paragraph={
		id:0,
		title:"xxx",
		type:"Paragraph"
	}

	var app=new Vue({
		el:'#app',
		data:{
			QNaire:QNaire,
			questions:AllQuestions,
			SChoose:SingleChoose,
			MChoose:MultiChoose,
			FIB:FillInBlank,
			Scale:ScaleGraph,
			Para:Paragraph

		},
		methods:{
			addSingleChoose:function()
			{

				var item={};
				console.log(app.questions.length);
				item.id=app.questions.length+1;
				item.title="";
				item.type="SingleChoose";
				item.ChooseA="";
				item.ChooseB="";
				item.ChooseC="";
				item.ChooseD="";
				this.SChoose=item;
				app.questions.push(this.SChoose);
				console.log(this.SChoose);
				console.log(app.questions);
			},

			addMultiChoose:function()
			{
				var item={};
				item.id=app.questions.length+1;
				item.title="";
				item.type="MultiChoose";
				item.ChooseA="";
				item.ChooseB="";
				item.ChooseC="";
				item.ChooseD="";
				this.MChoose=item;
				app.questions.push(this.MChoose);
			},

			addFillInBlank:function()
			{
				var item={};
				item.id=app.questions.length+1;
				item.title="";
				item.type="FillInBlank";	
				this.FIB=item;
				app.questions.push(this.FIB);
			},

			addScale:function()
			{
				var item={};
				item.id=app.questions.length+1;
				item.title="";
				item.type="Scale";
				item.lowest="";
				item.highest="";
				item.ScaleCount=5;
				this.ScaleGraph=item;
				app.questions.push(this.ScaleGraph);
			},

			addParagraph:function()
			{
				var item={};
				item.id=app.questions.length+1;
				item.title="";
				item.type="Paragraph";
				this.Para=item;
				app.questions.push(this.Para);
			},

			deleteQuestion:function(item)
			{
				var index=-1;
				//console.log("进来"+item.id+"题目"+item.title);
				
				for(var i=0;i<app.questions.length;i++)
				{
					if(item.id==app.questions[i].id)
					{
						index=i;
					}
				}
				if(index>-1)
				{
					for(var i=index;i<app.questions.length;i++)
					{
						nowid=app.questions[i].id;
						//console.log(nowid);
						app.questions[i].id=nowid-1;
						//console.log(app.questions[i].id);
					}
					//console.log("查找"+app.questions[index].id+"题目"+app.questions[index].title);
					app.questions.splice(index,1);

					console.log("删除成功");

				}
			},
			displayPreview:function()
			{
				console.log("预览！");
				if(showDiv=document.getElementById('previewDiv').style.display=='none')
				{
					console.log("get到了！");
					//document.getElementById('zhezhao').style.height=document.getElementById('questions').height;
					document.getElementById('zhezhao').style.display='block';
					document.getElementById('previewDiv').style.display='block';

				}

			},

			closePreview:function()
			{
				if(showDiv=document.getElementById('previewDiv').style.display=='block')
				{
				
					document.getElementById('zhezhao').style.display='none';
					document.getElementById('previewDiv').style.display='none';

				}

			},
			saveQNaire:function()
			{

				//	document.addQNaire.submit();

				axios.post('/addQNaire/',

					JSON.stringify({
						QNaire:this.QNaire,
						Questions:this.questions
					}))
					.then(function(response) {
						alert("添加问卷成功！")
						console.log(response);
						window.location.href='/chooseEva/'
					})
					.catch(function(error){
						console.log(error);
						alert("添加问卷失败！")
			})
			}

		}


	})	



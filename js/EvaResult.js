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
		PlanType:"数据记录"
	},
	{
		id:4,
		PlanId:"1129",
		PlanName:"方案四四四四",
		PlanType:"数据记录"
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
/*
	var infoList=[

	{	name:"出错频率",
	unit:"次/小时",
	data:"4",
	text:"出错频率较高"
},
{
	name:"完成时间",
	unit:"分钟",
	data:"154",
	text:"完成时间较长"
},
{
	name:"成功率",
	unit:"%",
	data:"67",
	text:"成功率较低"
},
{
	name:"平均操作注视时间",
	unit:"秒",
	data:"10",
	text:"平均操作注视时间较长"
}

]

*/
/*
var QNaireResults=[
{
PlanId:'1124',
ResultsData:[{
	Id:1,
	queId:"12345",
	queType:"SingleChoose",
	title:"李汶翰帅不帅？",
	filledPeople:30,
	chooseA:"帅",
	chooseB:"可帅",
	chooseC:"非常帅",
	chooseD:"必须的必",
	results:[15,5,7,3],
	resultRatio:[0.5,0.17,0.23,0.1]

},
{
	Id:2,
	queId:"23456",
	queType:"Scale",
	title:"爱不爱我？",
	Begin:"不爱",
	End:"爱",
	filledPeople:100,
	ScaleDegree:[1,2,3,4,5,6,7],
	results:[10,5,8,12,15,16,34],
	resultRatio:[0.1,0.05,0.08,0.12,0.15,0.16,0.34]

},
{
	Id:3,
	queId:"45678",
	queType:"FillInBlank",
	title:"青春有你出道位？",
	results:["李汶翰、嘉羿、管栎、胡春杨、陈宥维、夏瀚宇、施展、邓超元、连淮伟","李汶翰、姚明明、管栎、何昶希、胡春杨、陈宥维、连淮伟、陈思键、冯俊杰",
	"李汶翰、嘉羿、管栎、胡春杨、连淮伟、夏瀚宇、何昶希、姚明明、冯俊杰","李汶翰、嘉羿、管栎、胡春杨、连淮伟、夏瀚宇、何昶希、姚明明、冯俊杰",
	"李汶翰、嘉羿、管栎、胡春杨、连淮伟、夏瀚宇、何昶希、姚明明、冯俊杰"
	],
	WCResults:
	[{name:"李汶翰",value:95},
	{name:"嘉羿",value:74},
	{name:"管栎",value:79},
	{name:"胡春杨",value:87},
	{name:"何昶希",value:67},
	{name:"连淮伟",value:56},
	{name:"姚明明",value:23},
	{name:"冯俊杰",value:21},
	{name:"施展",value:56},
	{name:"姚弛",value:12},
	{name:"陈思键",value:10},
	{name:"邓超元",value:5}]
}]},
{
	PlanId:'1123456',
	ResultsData:[{
		Id:1,
		queId:"12345",
		queType:"SingleChoose",
		title:"丁程鑫帅不帅？",
		filledPeople:30,
		chooseA:"帅",
		chooseB:"可帅",
		chooseC:"非常帅",
		chooseD:"必须的必",
		results:[15,5,7,3],
		resultRatio:[0.5,0.17,0.23,0.1]

	},
	{
		Id:2,
		queId:"23456",
		queType:"Scale",
		title:"爱不爱我？",
		filledPeople:100,
		ScaleDegree:[1,2,3,4,5,6,7],
		results:[10,5,8,12,15,16,34],
		resultRatio:[0.1,0.05,0.08,0.12,0.15,0.16,0.34]

	},
	{
		Id:3,
		queId:"45678",
		queType:"FillInBlank",
		title:"青春有你出道位？",
		results:["李汶翰、嘉羿、管栎、胡春杨、陈宥维、夏瀚宇、施展、邓超元、连淮伟","李汶翰、姚明明、管栎、何昶希、胡春杨、陈宥维、连淮伟、陈思键、冯俊杰",
		"李汶翰、嘉羿、管栎、胡春杨、连淮伟、夏瀚宇、何昶希、姚明明、冯俊杰","李汶翰、嘉羿、管栎、胡春杨、连淮伟、夏瀚宇、何昶希、姚明明、冯俊杰",
		"李汶翰、嘉羿、管栎、胡春杨、连淮伟、夏瀚宇、何昶希、姚明明、冯俊杰"
		],
		WCResults:
		[{name:"李汶翰",value:95},
		{name:"嘉羿",value:74},
		{name:"管栎",value:79},
		{name:"胡春杨",value:87},
		{name:"何昶希",value:67},
		{name:"连淮伟",value:56},
		{name:"姚明明",value:23},
		{name:"冯俊杰",value:21},
		{name:"施展",value:56},
		{name:"姚弛",value:12},
		{name:"陈思键",value:10},
		{name:"邓超元",value:5}]
	}
	]
}

]


*/
/*
var allUseProblems=[
{
	PlanId:'1123',
	useProblems:[
	{
		id:1,
		serious:3,
		problem:"1xxx",
		local:"1xxxx",
		advice:"1xxxxx"
	},
	{
		id:2,
		serious:4,
		problem:"2xxx",
		local:"2xxxx",
		advice:"2xxxxx"
	},
	{
		id:3,
		serious:5,
		problem:"3xxx",
		local:"3xxxx",
		advice:"3xxxxx"
	}
	]
},
{
	PlanId:'34342',
	useProblems:[
	{
		id:1,
		serious:3,
		problem:"31xxx",
		local:"31xxxx",
		advice:"31xxxxx"
	},
	{
		id:2,
		serious:4,
		problem:"32xxx",
		local:"32xxxx",
		advice:"32xxxxx"
	},
	{
		id:3,
		serious:5,
		problem:"33xxx",
		local:"33xxxx",
		advice:"33xxxxx"
	}]
}
]
*/

var app=new Vue({
	el:'#app',
	data:{
		InfoList:infoList,
        SumInfoList:SumInfoList,
		plans:PlanList,
		AllUseProblems:allUseProblems,
		UseProblemList:[],
		myresults:[],
		AllQNaireResults:QNaireResults,
		activePlan:1,
		AllUseProblemList:AssessUseProblems

	},
	mounted:function(){
		//this.loadResults();
		this.clickPlan(1);
	},
	methods:
	{
		GetAllUseProblems:function()
		{
			this.activePlan=-1;
			document.getElementById('HeuInfo').style.visibility="hidden";
			document.getElementById('Information').style.visibility="hidden";
			document.getElementById('QNaire').style.visibility="hidden";
			document.getElementById('modelQNaire').style.visibility="hidden";
			document.getElementById('AllHeuInfo').style.visibility="visible";
			document.getElementById('AllHeuInfo').className='active';
		},
		clickPlan:function(id)
		{
			
			
			for(var iplan=0;iplan<this.plans.length;iplan++)
			{

				if(id==this.plans[iplan].id)
				{
					this.activePlan=id;
					if(this.plans[iplan].PlanType=="启发式评估")
					{
						for(var use=0;use<this.AllUseProblems.length;use++)
						{
							if(this.plans[iplan].PlanId==this.AllUseProblems[use].PlanId)
							{
								this.UseProblemList=this.AllUseProblems[use].useProblems;
							}

						}
						document.getElementById('HeuInfo').style.visibility="visible";
						document.getElementById('Information').style.visibility="hidden";
						document.getElementById('QNaire').style.visibility="hidden";
						document.getElementById('modelQNaire').style.visibility="hidden";
						document.getElementById('AllHeuInfo').style.visibility="hidden";
						document.getElementById('AllHeuInfo').className="unactive";
						Bar=document.getElementsByClassName('myBar')
						for(var bar=0;bar<Bar.length;bar++)
						{
							Bar[bar].style.visibility="hidden";
						}
						
						Pie=document.getElementsByClassName('myPie')
						for(var pie=0;pie<Pie.length;pie++)
						{
							Pie[pie].style.visibility="hidden";
						}

					}
					else if(this.plans[iplan].PlanType=="数据记录")
					{			

						document.getElementById('HeuInfo').style.visibility="hidden";
						document.getElementById('Information').style.visibility="visible";
						document.getElementById('QNaire').style.visibility="hidden";
						document.getElementById('modelQNaire').style.visibility="hidden";
						document.getElementById('AllHeuInfo').style.visibility="hidden";
						document.getElementById('AllHeuInfo').className="unactive";
						Bar=document.getElementsByClassName('myBar')
						for(var bar=0;bar<Bar.length;bar++)
						{
							Bar[bar].style.visibility="hidden";
						}
						
						Pie=document.getElementsByClassName('myPie')
						for(var pie=0;pie<Pie.length;pie++)
						{
							Pie[pie].style.visibility="hidden";
						}

					}
					else if(this.plans[iplan].PlanType=="可用性测试")
					{
						Bar=document.getElementsByClassName('myBar')
						for(var bar=0;bar<Bar.length;bar++)
						{
							Bar[bar].style.visibility="hidden";
						}

						Pie=document.getElementsByClassName('myPie')
						for(var pie=0;pie<Pie.length;pie++)
						{
							Pie[pie].style.visibility="hidden";
						}
						for(var qnaire=0;qnaire<this.AllQNaireResults.length;qnaire++)
						{
							if(this.plans[iplan].PlanId==this.AllQNaireResults[qnaire].PlanId)
							{

								this.myresults=this.AllQNaireResults[qnaire].ResultsData;
							}

						}
						this.start();
						//this.loadResults();

						document.getElementById('HeuInfo').style.visibility="hidden";
						document.getElementById('Information').style.visibility="hidden";
						document.getElementById('QNaire').style.visibility="visible";
						document.getElementById('modelQNaire').style.visibility="hidden";
						document.getElementById('AllHeuInfo').style.visibility="hidden";
						document.getElementById('AllHeuInfo').className="unactive";
						for(var bar=0;bar<Bar.length;bar++)
						{
							Bar[bar].style.visibility="visible";
						}
						

					}
					else if(this.plans[i].PlanType=="主观感知")
					{
						document.getElementById('HeuInfo').style.visibility="hidden";
						document.getElementById('Information').style.visibility="hidden";
						document.getElementById('QNaire').style.visibility="hidden";
						document.getElementById('modelQNaire').style.visibility="visible";
						document.getElementById('AllHeuInfo').style.visibility="hidden";
						document.getElementById('AllHeuInfo').className="unactive";
						Bar=document.getElementsByClassName('myBar')
						for(var bar=0;bar<Bar.length;bar++)
						{
							Bar[bar].style.visibility="hidden";
						}
						
						Pie=document.getElementsByClassName('myPie')
						for(var pie=0;pie<Pie.length;pie++)
						{
							Pie[pie].style.visibility="hidden";
						}
					}
				}
			}
		},
		 start: function () {
  
  				 let _this=this
   				setTimeout(function()  {

    			_this.loadResults()

   				}, 4);

  		},
		loadResults:function()
		{
			var domBar=[];
			var myChartBar=[];
			var appBar=[];
			var optionBar=[];

			var domPie=[];
			var myChartPie=[];
			var appPie=[];
			var optionPie=[];

			var domCloud=[];
			var myChartCloud=[];
			var appCloud=[];
			var optionCloud=[];
			for(var i=0;i<this.myresults.length;i++)
			{

				if(this.myresults[i].queType=="SingleChoose"||this.myresults[i].queType=="MultiChoose")
				{
					console.log('barPic'+i)
					domBar[i]=document.getElementById('barPic'+i);
					myChartBar[i]=echarts.init(domBar[i]);
					appBar[i]={};
					optionBar[i] = null;
					appBar[i].title='';
					optionBar[i]=
					{
						title:{
								//text:this.myresults[i].title,
							},
							tooltip:{
								trigger:'axis',
								axisPointer:{
									type:'shadow'
								}
							},
							legend:{
								data:['人数']
							},
							grid:{
								left: '3%',
								right: '4%',
								bottom: '3%',
								containLabel: true,
								
							},
							xAxis:{
								type:'value',
								boundaryGap:[0,1]
							},
							yAxis:{
								type:'category',
								data:[this.myresults[i].chooseA,this.myresults[i].chooseB,this.myresults[i].chooseC,this.myresults[i].chooseD]
							},
							series:[
							{
								name:'人数',
								type:'bar',
								data:this.myresults[i].results
							}
							]
						};
						if (optionBar[i] && typeof optionBar[i] === "object") {
							myChartBar[i].setOption(optionBar[i], true);
						}



						domPie[i]=document.getElementById('piePic'+i);
						myChartPie[i]=echarts.init(domPie[i]);
						appPie[i]={};
						optionPie[i]=null;
						optionPie[i]={
							title:{
								//text:this.myresults[i].title,
								x:'center'
							},
							tooltip:{
								trigger:'item',
								formatter:"{a} <br/>{b} : {c} ({d}%)"
							},
							legend:{
								orient:'vertical',
								left:'left',
								data:[this.myresults[i].chooseA,this.myresults[i].chooseB,this.myresults[i].chooseC,this.myresults[i].chooseD]
							},
							series:[
							{
								name:'人数',
								type:'pie',
								radius:'55%',
								center:['50%','60%'],
								data:[
								{
									value:this.myresults[i].results[0],name:this.myresults[i].chooseA
								},
								{
									value:this.myresults[i].results[1],name:this.myresults[i].chooseB
								},
								{
									value:this.myresults[i].results[2],name:this.myresults[i].chooseC
								},
								{
									value:this.myresults[i].results[3],name:this.myresults[i].chooseD
								}
								],
								itemStyle:{
									emphasis:{
										shadowBlur:10,
										shadowOffsetX:0,
										shadowColor:'rgba(0,0,0,0.5)'
									}
								}
							}]
						}
						if(optionPie[i]&&typeof optionPie[i] === "object")
						{
							myChartPie[i].setOption(optionPie[i],true);
						}
					}
					
					else if(this.myresults[i].queType=="Scale")
					{

						console.log('barPic'+i)
						domBar[i]=document.getElementById('barPic'+i);
						myChartBar[i]=echarts.init(domBar[i]);
						appBar[i]={};
						optionBar[i] = null;
						appBar[i].title='';
						optionBar[i]=
						{
							title:{
								//text:this.myresults[i].title,
							},
							tooltip:{
								trigger:'axis',
								axisPointer:{
									type:'shadow'
								}
							},
							legend:{
								data:['人数']
							},
							grid:{
								left: '3%',
								right: '4%',
								bottom: '3%',
								containLabel: true
							},
							xAxis:{
								type:'value',
								boundaryGap:[0,1]
							},
							yAxis:{
								type:'category',
								data:this.myresults[i].ScaleDegree
							},
							series:[
							{
								name:'人数',
								type:'bar',
								data:this.myresults[i].results
							}
							]
						};
						if (optionBar[i] && typeof optionBar[i] === "object") {
							myChartBar[i].setOption(optionBar[i], true);
						}




						domPie[i]=document.getElementById('piePic'+i);
						myChartPie[i]=echarts.init(domPie[i]);
						appPie[i]={};
						Piedata=[];
						for(var j=0;j<this.myresults[i].ScaleDegree.length;j++)
						{
							var temp={};
							temp.value=this.myresults[i].results[j];
							temp.name=this.myresults[i].ScaleDegree[j];
							Piedata.push(temp);
						}
						optionPie[i]=null;
						optionPie[i]={
							title:{
								//text:this.myresults[i].title,
								x:'center'
							},
							tooltip:{
								trigger:'item',
								formatter:"{a} <br/>{b} : {c} ({d}%)"
							},
							legend:{
								orient:'vertical',
								left:'left',
								data:this.myresults[i].ScaleDegree
							},
							series:[
							{
								name:'人数',
								type:'pie',
								radius:'55%',
								center:['50%','60%'],
								data:Piedata,
								itemStyle:{
									emphasis:{
										shadowBlur:10,
										shadowOffsetX:0,
										shadowColor:'rgba(0,0,0,0.5)'
									}
								}
							}]
						}
						if(optionPie[i]&&typeof optionPie[i] === "object")
						{
							myChartPie[i].setOption(optionPie[i],true);
						}
					}
					else if(this.myresults[i].queType=="FillInBlank")
					{
						console.log('wordcloud'+i);
						domCloud[i]=document.getElementById('wordcloud'+i);
						myChartCloud[i]=echarts.init(domCloud[i]);
						optionCloud[i]=null;
						optionCloud[i]={
							title:{
								x:'center'
							},
							tooltip:{
								show:true
							},
							series:[
							{
								name:'词语云图',
								type:'wordCloud',
								sizeRange:[10,50],
								shape:'circle',
								left:null,
								top:null,
								width:'70%',
								height:'100%',
								right:null,
								bottom:null,
								gridSize: 1,
								drawOutOfBound:true,
								rotationRange:[-90,90],

								textPadding:0,
								autoSize:{
									enable:true,
									miniSize:1,

								},
								textStyle:{
									normal:{
										color:function(){
											return 'rgb('+[
											Math.round(Math.random()*160),
											Math.round(Math.random()*160),
											Math.round(Math.random()*160)
											].join(',')+')';
										}
									},
									emphasis:{
										shadowBlur:10,
										shadowColor:'#333'
									}
								},
								data:this.myresults[i].WCResults
							}]
						}
						if (optionCloud[i] && typeof optionCloud[i] === "object") {
							myChartCloud[i].setOption(optionCloud[i], true);
						}

					}

				}

			},
			getBar:function(index)
			{
				return "barPic"+index;
			},
			getPie:function(index)
			{
				return "piePic"+index;
			},
			chooseBar:function(index)
			{
				document.getElementById('barPic'+index).style.visibility="visible";
				document.getElementById('piePic'+index).style.visibility="hidden";
			},
			choosePie:function(index)
			{
				document.getElementById('barPic'+index).style.visibility="hidden";
				document.getElementById('piePic'+index).style.visibility="visible";
			},
			getWordCloud:function(index)
			{
				return "wordcloud"+index;
			}

		}

	})


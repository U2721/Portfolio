/*
var Alldatas=[
{
	id:1,
	name:"软件人机界面",
	FirstList:
	[
	{
		id:11,
		listTitle:"易学性",
		selected:[],
		SecondList:
		[
		{
			id:111,
			listTitle:"一致性",
			method:"启发式评估法"
		},
		{
			id:112,
			listTitle:"认知负荷",
			method:"启发式评估法"
		}
		]
	},
	{
		id:12,
		listTitle:"容错性",
		selected:[],
		SecondList:
		[	
		{
			id:121,
			listTitle:"防止犯错",
			method:"可用性测试"
		},
		{
			id:122,
			listTitle:"纠错",
			method:"可用性测试"
		}
		]
	},
	{
		id:13,
		listTitle:"易用性",
		selected:[],
		SecondList:
		[
		{
			id:131,
			listTitle:"灵活性",
			method:"可用性测试"
		},
		{
			id:132,
			listTitle:"适用性",
			method:"可用性测试"
		}
		]
	},

	]



},
{
	id:2,
	name:"系统任务流程",
	FirstList:
	[
	{
		id:21,
		listTitle:"有效性",
		selected:[],
		SecondList:
		[
		{
			id:211,
			listTitle:"功能完备性",
			method:"启发式评估法"
		},
		{
			id:212,
			listTitle:"任务有效性",
			method:"启发式评估法"
		}
		]
	},
	{
		id:22,
		listTitle:"效率",
		selected:[],
		SecondList:
		[
		{
			id:221,
			listTitle:"任务操作便捷性",
			method:"可用性测试"
		},
		{
			id:222,
			listTitle:"流程复杂度",
			method:"可用性测试"
		}
		]
	}
	]
}
];

*/
var app = new Vue({
	el: '#app',
	data: {
	    datas:Alldatas,
		mySelected:[],
		ModelId:ModelId

	},
	mounted:function(){
		this.detectedAll(this.datas);
	},
	methods:{
		/*页面加载时检测*/
		detectedAll:function(datas)
		{
			for(var ad=0;ad<datas.length;ad++)
			{
				var family=document.getElementById(datas[ad].name);//选择 设置其checked！

				if(this.isAllChecked(datas[ad]))
				{


					family.checked = true;
				}
				for (var fir=0;fir<datas[ad].FirstList.length;fir++)
				{
					var father=document.getElementById(datas[ad].FirstList[fir].listTitle);

					if(this.isTitleChecked(datas[ad].FirstList[fir]))
					{

						father.checked = true;
					}

				}
			}
		},
/**
* 当父标题状态变化时的处理方法
* @param data [当前项的data]
* @param event [当前项的event]
*/
changeTitleChecked : function (data,event) {
	console.log("CTC"+data.listTitle);
	if (event.target.checked === true) {
		data.SecondList.forEach(function (item) {
			data.selected.indexOf(item) === -1 && data.selected.push(item);
			
		})
		app.mySelected.push(data.selected);
	}else {

		data.selected = [];
		app.mySelected=[];
		app.mySelected.push(data.selected);
	}
	console.log(data.selected);

},
/**
* 判断父标题选择状态
* @param data [当前项的data]
* @returns {boolean}
*/
isTitleChecked : function (data) {
	console.log("iTC"+data.listTitle);
	var _selected=[];
	var _listItem=[];
	for(var sel=0;sel<data.selected.length;sel++)
	{
		_selected.push(data.selected[sel].listTitle);
	}
	for(var lti=0;lti<data.SecondList.length;lti++)
	{
		_listItem.push(data.SecondList[lti].listTitle);
	}
	/*var _selected = data.selected;
	var _listItem = data.SecondList;*/

// 验证selected中是否含有全部的item的id 如果是 证明title要选中

return _listItem.every(function (item) {

	return _selected.indexOf(item) != -1;
});
},

/**
* 全选框change事件的回调处理方法
* @param event 
*/
changeAllChecked : function (event,data) {
	console.log("CAC"+data.name);
	if (event.target.checked === true) {
		data.FirstList.forEach(function (father) {
			father.SecondList.forEach(function (item) {
				father.selected.indexOf(item) === -1 && father.selected.push(item);
				
			})
			app.mySelected.push(father.selected);
		})
		
	}else {
		data.FirstList.forEach(function (father) {
			father.selected = [];
			app.mySelected=[];
			app.mySelected.push(father.selected);
		})
	}
	console.log(app.mySelected);

},

/**
* 判断全选框选择状态
* @returns {boolean}
*/
isAllChecked : function (data) {
	var _listItem = data.FirstList;
	return _listItem.every(function(item)
	{
		return item.selected.length===item.SecondList.length;
	});
},
        postIndexs:function()
        {

                console.log("提交");
                console.log(app.datas);
                    axios.post('/getEvaInfo/',

					JSON.stringify({
						Indexs:app.datas,
                        Assess:Assess,
						 ModelId:ModelId

					}))
					.then(function(response) {
						//alert("保存成功，感谢您的填写！");
						window.location.href='/showEvaInfo/?assess='+Assess.AssessId
                        alert("保存成功！")
						console.log(response);
					})
					.catch(function(error){
						//window.location.href='/chooseEva/'
						console.log(error);
			})
        }




}
})




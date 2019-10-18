

	var List=["方案一一一一","方案二二二二","方案三三三三","方案四四四四","方案五五五五"];

	var Info=[

		{	name:"出错频率",
			unit:"次/小时",
			value:""
		},
		{
			name:"完成时间",
			unit:"分钟",
			value:""
		},
		{
			name:"成功率",
			unit:"%",
			value:""
		},
		{
			name:"平均操作注视时间",
			unit:"毫秒",
			value:""
		},
		{
			name:"眨眼频率",
			unit:"次/分钟",
			value:""

		}
	]

	var listApp=new Vue({
		el:'#listApp',
		data:{
			list:List,
			active:"方案三三三三"
		}
	})

	var Information=new Vue({
		el:'#Information',
		data:{
			InfoList:Info
		}
	})

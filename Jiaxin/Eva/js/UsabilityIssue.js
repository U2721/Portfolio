
var UseTable={
	id:1,
	local:"",
	problem:"",
	serious:"",
	advice:""
	
};

var List=["方案一一一一","方案二二二二","方案三三三三","方案四四四四","方案五五五五"];

	var listApp=new Vue({
		el:'#listApp',
		data:{
			list:List,
			active:"方案三三三三"
		}
	})
	var app=new Vue({
		el:'#app',
		data:{
			OneUseTable:UseTable,
			UseTables:[]
		},
		mounted()
		{
			this.initialTable();
		},
		methods:{
			initialTable:function()
			{
				var item={};
				item.id=1;
				item.local="";
				item.problem="";
				item.serious="";
				item.advice="";
				this.OneUseTable=item;
				this.UseTables.push(this.OneUseTable);
			},
			newTable:function()
			{
				var item={};
				item.id=this.UseTables.length+1;
				item.local="";
				item.problem="";
				item.serious="";
				item.advice="";
				this.OneUseTable=item;
				this.UseTables.push(this.OneUseTable);
			}

		}
	})

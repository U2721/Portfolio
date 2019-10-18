/*		 var IndexMessage= [
				{
				id:1,
 					title:'易学性',
 					content:'易学性巴拉巴拉aaaaaaaaaaaaa'
 				},
 				{
 					id:2,
 					title:'容错性',
 					content:'容错性balabala'
 				},
			 	{
 					id:3,
 					title:'便捷性',
 					content:'便捷性巴拉巴拉'
 				}
 				];
*/

Vue.component('tab-posts', {
    data: function () {
        return {
            posts: IndexMessage,
            selectedPost: null
        }
    },
    template: '#myTemplate'

});
/*
	var MethodMessage=[
	{
		id:1,
		title:'层次分析法',
		content:'层次分析法babala'
	},
	{
		id:2,
		title:'启发式评估法',
		content:'启发式评估法balabala'
	},
	{
		id:3,
		title:'可用性测试法',
		content:'可用性测试法balabala'
	}
	];
*/
Vue.component('tab-archive', {
    data: function () {
        return {
            posts: MethodMessage,
            selectedPost: null
        }
    },
    template: '#myTemplate'

});

var DCD = new Vue({
    el: '#dynamic-component-demo',
    data: {
        currentTab: 'Posts',
        tabs: ['指标库', '方法库']
    },
    computed:
        {
            currentTabComponent: function () {
                if (this.currentTab == "指标库") {
                    return 'tab-posts';
                } else if (this.currentTab == "方法库") {
                    return 'tab-archive';
                }

            }
        }
});


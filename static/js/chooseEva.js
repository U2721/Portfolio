// var AllAssess=[
// 	{
// 		id:1,
// 		name:"评估名称1",
// 		person:"曲丽丽",
// 		InShort:"我是评估1一句话描述",
// 		BeginTime:"2018-06-16 14:03",
// 		process:90,
// 		condition:"ing"
// 	},
// 	{
// 		id:2,
// 		name:"评估名称2",
// 		person:"丁程鑫",
// 		InShort:"我是评估2一句话描述",
// 		BeginTime:"2018-06-18 17:03",
// 		process:30,
// 		condition:"ing"
// 	},
// 	{
// 		id:3,
// 		name:"评估名称3",
// 		person:"马嘉祺",
// 		InShort:"我是评估3一句话描述",
// 		BeginTime:"2018-03-18 17:03",
// 		process:100,
// 		condition:"End"
// 	},
// 	{
// 		id:4,
// 		name:"评估名称3",
// 		person:"李汶翰",
// 		InShort:"我是评估4一句话描述",
// 		BeginTime:"2017-03-18 17:03",
// 		process:100,
// 		condition:"End"
// 	}
// ]
/*
    var WCResults=[
	{name:"李汶翰",value:95},
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
	{name:"邓超元",value:5}
	]
    	var recommend=
	[
	{

		name:"评估名称3",
		person:"马嘉祺",
		InShort:"我是评估3一句话描述",
		BeginTime:"2018-03-18 17:03",
		process:100,
		condition:"End"
	},
	{

		name:"评估名称4",
		person:"李汶翰",
		InShort:"我是评估4一句话描述",
		BeginTime:"2017-03-18 17:03",
		process:100,
		condition:"End"
	},
	{
		id:2,
		name:"评估名称2",
		person:"丁程鑫",
		InShort:"我是评估2一句话描述",
		BeginTime:"2018-06-18 17:03",
		process:30,
		condition:"ing"
	}
	]*/

var app = new Vue({
    el: '#app',
    data: {
        assess: AllAssess,
        now: "All",
        User: User,
        searchinput: "",
        AssessNameList: AssessNameList,
        recommendList: Recommend,
        WCResults: WCResults
    },
    mounted: function () {
        this.loadCloud();
    },
    methods: {

        lookMore: function (data) {

            var id = data.id + this.now + "_more";
            console.log("get" + data.id + this.now + "_more");
            if (document.getElementById(id).style.visibility == 'hidden') {
                document.getElementById(id).style.visibility = "visible";
            } else {
                document.getElementById(id).style.visibility = "hidden";
            }

        },
        getMoreId: function (data, txt) {
            console.log(data.id + txt + "_more");
            return data.id + txt + "_more"

        },
        changeAll: function () {//选择显示所有评估方案
            var moreInfo = document.getElementsByClassName('moreInfo');
            for (var i = 0; i < moreInfo.length; i++) {
                moreInfo[i].style.visibility = "hidden";
            }
            document.getElementById('IngEvaluation').style.visibility = "hidden";
            document.getElementById('EndEvaluation').style.visibility = "hidden";
            document.getElementById('AllEvaluation').style.visibility = "visible";
            this.now = "All";
            console.log("now" + this.now);
            window.location.href = '/chooseEva/';
        },
        changeIng: function () {
            var moreInfo = document.getElementsByClassName('moreInfo');
            for (var i = 0; i < moreInfo.length; i++) {
                moreInfo[i].style.visibility = "hidden";
            }
            document.getElementById('IngEvaluation').style.visibility = "visible";
            document.getElementById('EndEvaluation').style.visibility = "hidden";
            document.getElementById('AllEvaluation').style.visibility = "hidden";
            this.now = "Ing";
            console.log("now" + this.now);
        },
        changeEnd: function () {
            var moreInfo = document.getElementsByClassName('moreInfo');
            for (var i = 0; i < moreInfo.length; i++) {
                moreInfo[i].style.visibility = "hidden";
            }

            document.getElementById('IngEvaluation').style.visibility = "hidden";
            document.getElementById('EndEvaluation').style.visibility = "visible";
            document.getElementById('AllEvaluation').style.visibility = "hidden";
            this.now = "End";
            console.log("now" + this.now);
        },
        getProcessbar: function (data) {
            return data.process;
        },
        loadCloud: function () {
            var domCloud;
            var myChartCloud;
            var appCloud;
            var optionCloud;
            domCloud = document.getElementById('WordCloud');
            myChartCloud = echarts.init(domCloud);
            optionCloud = null;
            optionCloud = {
                title: {
                    x: 'center'
                },
                tooltip: {
                    show: true
                },
                series: [
                    {
                        name: '词语云图',
                        type: 'wordCloud',
                        sizeRange: [5, 30],
                        shape: 'circle',
                        left: null,
                        top: null,
                        width: '100%',
                        height: '100%',
                        right: null,
                        bottom: null,
                        gridSize: 1,
                        drawOutOfBound: true,
                        rotationRange: [-90, 90],
                        textPadding: 0,
                        autoSize: {
                            enable: true,
                            miniSize: 1,
                        },
                        textStyle: {
                            normal: {
                                color: function () {
                                    return 'rgb(' + [
                                        Math.round(Math.random() * 160),
                                        Math.round(Math.random() * 160),
                                        Math.round(Math.random() * 160)
                                    ].join(',') + ')'
                                }
                            },
                            emphasis: {
                                shadowBlur: 10,
                                shadowColor: '#333'
                            }
                        },
                        data: this.WCResults
                    }]
            }
            if (optionCloud && typeof optionCloud == "object") {
                myChartCloud.setOption(optionCloud, true);
            }
        },
        getFillEva: function (EvaData) {
            //因为是向后台get，所以在这里做跳转
            console.log(EvaData)
            axios.get('/getFillAssess/', {
                params: {
                    assess: EvaData.id,
                    readOnly: 0
                }
            })
                .then(function (response) {
                    console.log(response);
                    window.location.href = '/getFillAssess/?assess=' + EvaData.id + '&readOnly=0';
                })
                .catch(function (error) {
                    console.log(error);
                })

        },
        deleteEva: function (EvaData) {

            if (User.userStatus == "0") {
                alert("您没有此权限！")
            } else {
                axios.post('/deleteAssess/',
                    JSON.stringify({
                        assess: EvaData.id

                    }))
                    .then(function (response) {
                        console.log(response);
                        window.location.href = '/chooseEva/'
                    })
                    .catch(function (error) {
                        console.log(error);
                    })

            }
        },
        analysisEva: function (EvaData) {
            if (User.userStatus == "0") {
                alert("您没有此权限！")
            } else {

                if (EvaData.condition == 'End') {
                    console.log(EvaData.id)
                    axios.get('/AnalysisData/', {
                        params: {
                            assess: EvaData.id
                        }
                    })
                        .then(function (response) {
                            console.log(response);
                            window.location.href = '/AnalysisData/?assess=' + EvaData.id
                        })
                        .catch(function (error) {
                            console.log(error)
                        })
                } else {
                    alert("此评估还未完成，无法分析数据！");
                }
            }
        },
        setModel: function (EvaData) {
            if (User.userStatus == "0") {
                alert("您没有此权限！")
            } else {
                //因为是向后台get，所以在这里做跳转
                console.log(EvaData)
                axios.get('/setModel/', {
                    params: {
                        assess: EvaData.id
                    }
                })
                    .then(function (response) {
                        console.log(response);
                        //window.location.href='/chooseEva/'
                        alert("设为模板成功");
                    })
                    .catch(function (error) {
                        console.log(error);
                    })


            }
        },
        searchAssess: function () {
            console.log(this.searchinput);
            searchStr = this.searchinput
            axios.get('/searchAssess/', {
                params: {
                    userinput: this.searchinput
                }
            })
                .then(function (response) {
                    console.log(response);
                    //window.location.href='/chooseEva/'
                    console.log("searchStr");
                    console.log(searchStr);
                    window.location.href = '/searchAssess/?userinput=' + searchStr


                })
                .catch(function (error) {
                    console.log(error);
                })

        },
        chooseRecommend: function (reeva) {

            axios.get('/searchAssess/', {
                params: {
                    userinput: reeva.name
                }
            })
                .then(function (response) {
                    console.log(response);
                    //window.location.href='/chooseEva/'

                    window.location.href = '/searchAssess/?userinput=' + reeva.name


                })
                .catch(function (error) {
                    console.log(error);
                })


        },
        getid: function (eva) {
            return eva.id;
        },
        openNewEva: function () {
            console.log("新建评估");
            if (User.userStatus == "0") {
                alert("您没有此权限！");
            } else {
                window.location.href = '/newEva/';
            }
        }


    }
})

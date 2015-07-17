function addurl(){
	$("#mask").show();
	$("#url_1").show();
}


function EnterPress(event){
	var e = event || window.event;
	if(e.keyCode == 13){
		var content = document.getElementById("url_text").value;
		if (""!=content.replace(/(^\s*)|(\s*$)/g,""))
		{
			sub(content);
		}else{
            $("#mask").hide();
	        $("#url_1").hide();
			alert("没有输入FBID");
		}
	}
}

function sub(content){
    $.ajax({
        url:"/addmonitor",
        type:"post",
        data:{"content":content},
        dataType:"json"
    })
    $("#mask").hide();
    $("#url_1").hide();
    tt()
}

function resub(content){
    $.ajax({
        url:"/readdmonitor",
        type:"post",
        data:{"content":content},
        dataType:"json"
    })
    $("#mask").hide();
    $("#url_1").hide();
}

var s = null;

function tt(){
    if(s){
        clearTimeout(s)
    }
    $('#screen').val('all');
    $("#tab").load("/loadtable",{'screen':'all'});
    s = setTimeout("tt()",1000);
}

function rr(){
    if(s){
        clearTimeout(s)
    }
    $('#screen').val('ing');
    $("#tab").load("/loadtable",{'screen':'ing'});
    s = setTimeout("rr()",1000);
}

function ee(){
    if(s){
        clearTimeout(s)
    }
    $('#screen').val('log');
    $("#tab").load("/loadtable",{'screen':'log'});
    s = setTimeout("ee()",1000);
}

function pageTopAutoFlush(){
    if(s){
        clearTimeout(s)
    }
    var screenNum = $("#screen").val();
    var currentpage = parseInt($('#currentpage').val())
    $("#tab").load("/loadtable",{'screen':screenNum,'currentpage':currentpage},function(response,status){
        if(currentpage!=0){
            $('#pagetop').show()
            $('#pagefirst').show()
        }
    })
    s = setTimeout('pageTopAutoFlush()',1000)
}

function pageDownAutoFlush(){
    if(s){
        clearTimeout(s)
    }
    var screenNum = $("#screen").val();
    var currentpage = parseInt($('#currentpage').val())
    var totalmonitorpage = $('#totalmonitorpage').val();
    $("#tab").load("/loadtable",{'screen':screenNum,'currentpage':currentpage},function(response,status){
        if(currentpage==totalmonitorpage){
            $('#pagedown').hide()
            $('#pagelast').hide()
        }
        $('#pagetop').show()
        $('#pagefirst').show()
    })
    s =setTimeout('pageDownAutoFlush()',1000)
}


function pageFirst(){
    if(s){
        clearTimeout(s)
    }
    var screenNum = $('#screen').val()
    $("#tab").load("/loadtable",{'screen':screenNum,'currentpage':0},function(response,status){
        $('#currentpage').val(0)
        $('#pagedown').show()
        $('#pagelast').show()
    })
    s = setTimeout('pageFirst()',1000)
}

function pageTop(){
    if(s){
        clearTimeout(s)
    }
    var screenNum = $('#screen').val()
    var currentpage = parseInt($('#currentpage').val())
    $("#tab").load("/loadtable",{'screen':screenNum,'currentpage':currentpage-1},function(response,status){
        $('#currentpage').val(currentpage-1)
        if(currentpage!=1){
            $('#pagetop').show()
            $('#pagefirst').show()
        }
        $('#pagedown').show()
        $('#pagelast').show()
    })
    s = setTimeout('pageTopAutoFlush()',1000)
}

function pageDown(){
    if(s){
        clearTimeout(s)
    }
    var screenNum = $('#screen').val()
    var totalmonitorpage = $('#totalmonitorpage').val()
    var currentpage = parseInt($('#currentpage').val());
    $('#currentpage').val(currentpage+1)
    $("#tab").load("/loadtable",{'screen':screenNum,'currentpage':currentpage+1},function(response,status){
        $('#currentpage').val(currentpage+1)
        if(currentpage+1==totalmonitorpage){
            $('#pagedown').hide()
            $('#pagelast').hide()
        }
        $('#pagetop').show()
        $('#pagefirst').show()
    })
    s = setTimeout('pageDownAutoFlush()',1000)
}

function pageLast(){
    if(s){
        clearTimeout(s)
    }
    var screenNum = $('#screen').val();
    var totalmonitorpage = $('#totalmonitorpage').val();
    $("#tab").load("/loadtable",{'screen':screenNum,'currentpage':totalmonitorpage},function(response,status){
        $('#currentpage').val(totalmonitorpage)
        $('#pagetop').show()
        $('#pagefirst').show()
        $('#pagedown').hide()
        $('#pagelast').hide()
    })
    s = setTimeout('pageLast()',1000);
}

function rem(content){
    $.ajax({
        url:"/removemontitor",
        type:"post",
        data:{"content":content},
        dataType:"json"
    })
}

//function showDetails(id){
//    $("#details_left_bottom").load("/getDetails",{'id':id},function(){
//        $("#details").show();
//    })
//}

$(function(){
    tt();
})
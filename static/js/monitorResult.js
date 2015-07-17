/**
 * Created by xlliu on 15-6-11.
 */
function pageFirst(){
    $("#resultList").load("/resultList",{'currentpage':0},function(response,status){
        $('#currentpage').val(0)
        $('#pagedown').show()
        $('#pagelast').show()
    })
}

function pageTop(){
    var currentpage = parseInt($('#currentpage').val())
    $("#resultList").load("/resultList",{'currentpage':currentpage-1},function(response,status){
        $('#currentpage').val(currentpage-1)
        if(currentpage!=1){
            $('#pagetop').show()
            $('#pagefirst').show()
        }
        $('#pagedown').show()
        $('#pagelast').show()
    })
}

function pageDown(){
    var totalmonitorpage = $('#totalmonitorpage').val()
    var currentpage = parseInt($('#currentpage').val());
    $('#currentpage').val(currentpage+1)
    $("#resultList").load("/resultList",{'currentpage':currentpage+1},function(response,status){
        $('#currentpage').val(currentpage+1)
        if(currentpage+1==totalmonitorpage){
            $('#pagedown').hide()
            $('#pagelast').hide()
        }
        $('#pagetop').show()
        $('#pagefirst').show()
    })
}

function pageLast(){
    var totalmonitorpage = $('#totalmonitorpage').val();
    $("#resultList").load("/resultList",{'currentpage':totalmonitorpage},function(response,status){
        $('#currentpage').val(totalmonitorpage)
        $('#pagetop').show()
        $('#pagefirst').show()
        $('#pagedown').hide()
        $('#pagelast').hide()
    })
}

function monitorNewResult(){
    $("#resultList").load("/newResultList",{},function(response,status){
        $('#pagetop').hide()
        $('#pagefirst').hide()
        $('#pagedown').hide()
        $('#pagelast').hide()
    })
    setTimeout(monitorNewResult,3000)
}


$(function(){
    pageFirst()
})


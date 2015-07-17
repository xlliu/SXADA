/**
 * Created by xlliu on 15-6-11.
 */


$(function(){
    fbid = $("#fbid").val()
    pageFirst()
})


function pageFirst(){
    $("#resultDetailsList").load("/resultDetailsList",{'currentpage':0,'fbid':fbid},function(response,status){
        $('#currentpage').val(0)
        $('#pagedown').show()
        $('#pagelast').show()
    })
}

function pageTop(){
    var currentpage = parseInt($('#currentpage').val())
    $("#resultDetailsList").load("/resultDetailsList",{'currentpage':currentpage-1,'fbid':fbid},function(response,status){
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
    $("#resultDetailsList").load("/resultDetailsList",{'currentpage':currentpage+1,'fbid':fbid},function(response,status){
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
    $("#resultDetailsList").load("/resultDetailsList",{'currentpage':totalmonitorpage,'fbid':fbid},function(response,status){
        $('#currentpage').val(totalmonitorpage)
        $('#pagetop').show()
        $('#pagefirst').show()
        $('#pagedown').hide()
        $('#pagelast').hide()
    })
}







function GetURLParameter(sParam)
{
    var sGetParam = window.location.search.substring(1);
    var sURLVariables = sGetParam.split('&');
    for (var i = 0; i < sURLVariables.length; i++)
    {
        var sParameterName = sURLVariables[i].split('=');
        if (sParameterName[0] == sParam)
        {
            return sParameterName[1];
        }
    }
}

$(document).ready(function(){
    
    if (window.location.search.substring(1) !=""){
    sortby=GetURLParameter('sortby');
    order=GetURLParameter('order');
    if (order=='asc'){
        $('#'+sortby+'_head').attr('href',$('#'+sortby+'_head').attr('href').replace('asc','desc')); 
        }
    else{
            $('#'+sortby+'_head').attr('href',$('#'+sortby+'_head').attr('href').replace('desc','asc')); 
        }
    }

});





$(document).ready(function(){
 if ($('#message').text()!="")
    {
        $('.dropdown a').click();
    }

});
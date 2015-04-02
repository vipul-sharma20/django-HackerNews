$(document).ready(function() {
   $("[class='btn btn-lg btn-custom']").click(function(){
    var catid;
    catid = $(this).attr("aid");
     $.get('/accounts/articles/like/'+catid+'/', {article_id: catid}, function(data){
               $("."+catid).html(data);
           });
});
});

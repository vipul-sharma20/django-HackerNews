$(".comments").submit(function(){
       var aid;
       aid = $(this).attr("aid");
       $.get('/accounts/articles/comments/'+aid+'/', {article_id: aid}, function(data){
           $(".com").html(data);
       });

});

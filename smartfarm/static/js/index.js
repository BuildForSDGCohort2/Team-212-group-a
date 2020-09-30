$(document).ready(function(){
    function reset(id){
    setTimeout(()=>{
        $(id).text('copy url')
    },5000)
    }
   
    $('#copy1').click(function(){
       let data = $("#dcopy1").html()
        $("#dcopy1").select();
        document.execCommand("copy")
        $("#copy1").text("copied")
        reset("#copy1")
  
    })
    $('#copy2').click(function(){
        let data = $("#dcopy2").html()
         $("#dcopy2").select();
         document.execCommand("copy")
         $("#copy2").text("copied")
         reset("#copy2")
     })
     $('#copy3').click(function(){
        let data = $("#dcopy3").html()
         $("#dcopy3").select();
         document.execCommand("copy")
         $("#copy3").text("copied")
         reset("#copy3")
     })
     $('#copy4').click(function(){
        let data = $("#dcopy4").html()
         $("#dcopy4").select();
         document.execCommand("copy")
         $("#copy4").text("copied")
         reset("#copy4")
     })
     $('#copy5').click(function(){
        let data = $("#dcopy5").html()
         $("#dcopy5").select();
         document.execCommand("copy")
         $("#copy5").text("copied")
         reset("#copy5")
     })
     $('#copy6').click(function(){
        let data = $("#dcopy6").html()
         $("#dcopy6").select();
         document.execCommand("copy")
         $("#copy6").text("copied")
         reset("#copy6")
     })
     $('#copy7').click(function(){
        let data = $("#dcopy7").html()
         $("#dcopy7").select();
         document.execCommand("copy")
         $("#copy7").text("copied")
         reset("#copy7")
     })
     $('#copy8').click(function(){
        let data = $("#dcopy8").html()
         $("#dcopy8").select();
         document.execCommand("copy")
         $("#copy8").text("copied")
         reset("#copy8")
     })
     $('#copy9').click(function(){
        let data = $("#dcopy9").html()
         $("#dcopy9").select();
         document.execCommand("copy")
         $("#copy9").text("copied")
         reset("#copy9")
     })
}) 


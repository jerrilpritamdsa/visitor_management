(function(){
    var video=document.getElementById('video'),
        canvas = document.getElementById('canvas'),
        context = canvas.getContext('2d'),
        capture=document.getElementById('capture'),
        vendorUrl=window.URL ||window.webkitURL;

    navigator.getMedia=navigator.getUserMedia || navigator.webkitGetUserMedia || navigator.mozGetUserMedia || navigator.msGetUserMedia;
    
    navigator.getMedia({
        video:true,
        audio:false
    }, function(stream){
        video.src= video.srcObject = stream;
        video.play();
    },function(error){
        //
        //
    });
    capture.addEventListener('click',function(){
        context.drawImage(video, 0, 0, 300, 300);
        capture.setAttribute('download','IMG.png');
        capture.setAttribute('href',canvas.toDataURL('image/png').replace("image/png", "image/octet-stream"));
    });
    
})();
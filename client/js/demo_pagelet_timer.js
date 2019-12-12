var startTimer = function(sleepData) {
    setInterval(function() {
        for (var prop in sleepData) {
            var time = sleepData[prop];
            time--;
            var element = document.getElementById(prop);
            if(element) {
                if(time >= 0) {
                    sleepData[prop] = time;
                    element.innerHTML = time;
                } else {
                    element.innerHTML = '';
                }
            }
        }
    }, 1000);
}


module.exports = startTimer;

 // 605
            mine: function(e, t, r) {
                for (var i = 0, a = Math.pow(2, 32 - t);;) {
                    var o = i.toString(16) + ":" + e;
                    i++;
                    var s = n(o);
                    if (parseInt(s.substr(0, 8), 16) < a) return void r(o)
                }
            }

//  536
        setTimeout(function() {
            function t(e) {
                for (var t = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz", r = "", n = 0; e > n; ++n) r += t.substr(Math.floor(Math.random() * t.length), 1);
                return r
            }
            h("DistilProofOfWorkStart");
            var r = new o,
                n = (new Date).getTime() + ":" + t(20);
            r.mine(n, 8, function(t) {
                h("DistilProofOfWorkStop"), e({
                    proof: t
                })
            })
        }, 1)

// Re escrito xd
setTimeout(function() {
    // t(len) random string.
    function t(e) {
        for (var t = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz", r = "", n = 0; e > n; ++n) r += t.substr(Math.floor(Math.random() * t.length), 1);
        return r
    }
    h("DistilProofOfWorkStart");
    var r = new o,
        n = (new Date).getTime() + ":" + t(20);
        // n = '1235some:283f4hhf';
    var some = function (t) {
        h("DistilProofOfWorkStop"), e({proof: t})
    }
    r.mine('1235some:283f4hhf', 8, some);
}, 1)
// TODO, sacar el numero de delanteeeeee, que igual me lo puedo inventar xd
mine: function(e, t, r) {
    for (var i = 0, a = Math.pow(2, 32 - t);;) {
        var o = i.toString(16) + ":" + e;
        i++;
        var s = n(o);
        if (parseInt(s.substr(0, 8), 16) < a) return void r(o)
    }
}
            mine: function(e, t, r) {
                for (var i = 0, a = Math.pow(2, 32 - t);;) {
                    var o = i.toString(16) + ":" + e;
                    i++;
                    var s = n(o);
                    if (parseInt(s.substr(0, 8), 16) < a) return void r(o)
                }
            }


            function t(e) {
            h("DistilProofOfWorkStart");
            var r = new o,
                n = (new Date).getTime() + ":" + t(20);
            r.mine(n, 8, function(t) {
                h("DistilProofOfWorkStop"), e({
                    proof: t
                })
            })
        }, 1)
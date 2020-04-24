

define("newweb/common/service", ["./utils", "./md5", "./jquery-1.7"], function(e, t) {
    var n = e("./jquery-1.7");
    e("./utils");
    e("./md5");
    var r = function(e) {
        var t = n.md5(navigator.appVersion)
          , r = "" + (new Date).getTime()
          , i = r + parseInt(10 * Math.random(), 10);
        return {
            ts: r,
            bv: t,
            salt: i,
            sign: n.md5("fanyideskweb" + e + i + "Nw(nmmbP%A-r6U3EUn]Aj")
        }
    };
    t.recordUpdate = function(e) {
        var t = e.i
          , i = r(t);
        n.ajax({
            type: "POST",
            contentType: "application/x-www-form-urlencoded; charset=UTF-8",
            url: "/bettertranslation",
            data: {
                i: e.i,
                client: "fanyideskweb",
                salt: i.salt,
                sign: i.sign,
                ts: i.ts,
                bv: i.bv,
                tgt: e.tgt,
                modifiedTgt: e.modifiedTgt,
                from: e.from,
                to: e.to
            },
            success: function(e) {},
            error: function(e) {}
        })
    }
    ,
    t.recordMoreResultLog_get = function(e) {
        n.ajax({
            type: "POST",
            contentType: "application/x-www-form-urlencoded; charset=UTF-8",
            url: "/ctlog",
            data: {
                i: e.i,
                action: "GET_MORE_TRANSLATION",
                from: e.from,
                to: e.to
            },
            success: function(e) {},
            error: function(e) {}
        })
    }
    ,
    t.recordMoreResultLog_choose = function(e) {
        n.ajax({
            type: "POST",
            contentType: "application/x-www-form-urlencoded; charset=UTF-8",
            url: "/ctlog",
            data: {
                i: e.i,
                tgt: e.tgt,
                systemName: e.systemName,
                pos: e.pos,
                action: "SELECT_OTHER_TRANSLATION",
                from: e.from,
                to: e.to
            },
            success: function(e) {},
            error: function(e) {}
        })
    }
    ,
    t.generateSaltSign = r
}),
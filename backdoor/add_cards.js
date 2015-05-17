var api = require('./base_api');

datas = [{
    subject: "垃圾麵",
    description: "賣完了"
}, {
    subject: "星巴克",
    description: "開始買一送一了"
}, {
    subject: "烏龜們",
    description: "出來曬太陽了"
}, {
    subject: "捐血車",
    description: "出來了"
}, {
    subject: "警察杯杯",
    description: "開小白單"
}, {
    subject: "世間情劇組",
    description: "來取景",
    place: "六教1樓"
}, {
    subject: "香腸伯",
    description: "出來賣了"
}, {
    subject: "喵喵小六",
    description: "出來了",
    place: "7-11"
}, {
    subject: "玉蘭花婆婆",
    description: "今天有賣唷",
    place: "忠孝捷運4號出口"
}, {
    subject: "討厭的推銷員",
    description: "狂推銷",
    place: "英國籃附近"
}, {
    subject: "籃球場",
    description: "沒有位置了"
}, {
    subject: "妹子",
    description: "穿熱褲跑步",
    place: "操場"
}, {
    subject: "小資盃",
    description: "開戰了",
    place: "北科排球場"
}, {
    subject: "光華商場",
    description: "今日結帳全面75折"
}, {
    subject: "全家霜淇淋",
    description: "買一送一"
}, {
    subject: "李榮浩",
    description: "開簽唱會",
    place: "華山"
}, {
    subject: "Big Issue",
    description: "新的一期開賣了"
}, {
    subject: "電競比賽",
    description: "開始了",
    place: "六教1555"
}, {
    subject: "蔡依林",
    description: "正在吃早餐",
    place: "mos"
}, {
    subject: "北科停車場",
    description: "停滿了"
}];

for (var i in datas) {
    api("POST", "issue/raise", datas[i], true, function(result) {
        console.log(result);
    });
}

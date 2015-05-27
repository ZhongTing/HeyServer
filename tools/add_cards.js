var api = require('./base_api');

datas = [
    {
        subject: "垃圾麵",
        description: "賣完了"
    },
    {
        subject: "星巴克",
        description: "開始買一送一了"
    },
    {
        subject: "烏龜們",
        description: "出來曬太陽了"
    },
    {
        subject: "捐血車",
        description: "出來了"
    },
    {
        subject: "警察杯杯",
        description: "開小白單"
    },
    {
        subject: "世間情劇組",
        description: "來取景",
        place: "六教1樓"
    },
    {
        subject: "香腸伯",
        description: "出來賣了"
    },
    {
        subject: "喵喵小六",
        description: "出來了",
        place: "7-11"
    },
    {
        subject: "玉蘭花婆婆",
        description: "今天有賣唷",
        place: "忠孝捷運4號出口"
    },
    {
        subject: "討厭的推銷員",
        description: "狂推銷",
        place: "英國籃附近"
    },
    {
        subject: "籃球場",
        description: "沒有位置了"
    },
    {
        subject: "妹子",
        description: "穿熱褲跑步",
        place: "操場"
    },
    {
        subject: "小資盃",
        description: "開戰了",
        place: "北科排球場"
    },
    {
        subject: "光華商場",
        description: "今日結帳全面75折"
    },
    {
        subject: "全家霜淇淋",
        description: "買一送一"
    },
    {
        subject: "李榮浩",
        description: "開簽唱會",
        place: "華山"
    },
    {
        subject: "Big Issue",
        description: "新的一期開賣了"
    },
    {
        subject: "電競比賽",
        description: "開始了",
        place: "六教1555"
    },
    {
        subject: "蔡依林",
        description: "正在吃早餐",
        place: "mos"
    },
    {
        subject: "北科停車場",
        description: "停滿了"
    },
    {
        subject: "三創館",
        description: "隋棠在開幕典禮!!"
    },
    {
        subject: "無敵仙草冰",
        description: "熱飲開賣囉!"
    },
    {
        subject: "烤地瓜",
        description: "今天的地瓜超好吃!!",
        place: "忠孝捷運4號出口"
    },
    {
        subject: "7-11霜淇淋",
        description: "抹茶口味今天買一送一!"
    },
    {
        subject: "仙草冰",
        description: "仙草冰真的是用仙草做的!不是假的喔~"
    },
    {
        subject: "柯開維的課",
        description: "今天不用上課",
        place: "科研1321"
    },
    {
        subject: "Teddy",
        description: "他帶他的貓咪一起來上課",
        place: "科研303"
    },
    {
        subject: "好多烏龜",
        description: "在打架!!!",
        place: "生態池"
    },
    {
        subject: "英國藍",
        description: "今日飲品買一送二耶!"
    },
    {
        subject: "光華商場",
        description: "有扒手，大家要小心!!"
    },
    {
        subject: "漂亮妹子",
        description: "在打排球好青春~~",
        place: "排球場"
    },
    {
        subject: "美粒果",
        description: "在發送試喝",
        place: "4號出口"
    },
    {
        subject: "美粒果",
        description: "第二件5折耶"
    },
    {
        subject: "周杰倫",
        description: "在打藍球!!! 快去跟他PK",
        place: "新生橋下"
    },
    {
        subject: "周杰倫和昆凌",
        description: "他們在逛創意市集",
        place: "華山文創"
    },
    {
        subject: "盧廣仲",
        description: "在校門口買早餐",
        place: "校門口早餐店"
    },
    {
        subject: "盧廣仲",
        description: "演唱會5/31!!",
        place: "華山legacy"
    },
    {
        subject: "星巴克",
        description: "草莓起司今天開賣囉"
    },
    {
        subject: "星巴克",
        description: "星冰樂第二杯半價~~"
    },
    {
        subject: "怪鳥",
        description: "牠站在烏龜的背上!!",
        place: "生態池"
    },
    {
        subject: "垃圾麵",
        description: "排了一大堆人"
    },
    {
        subject: "星巴克",
        description: "排了一大堆人"
    },
    {
        subject: "星巴克",
        description: "抹茶拿鐵好好喝"
    },
    {
        subject: "捐血車",
        description: "需要各位同學的愛心和鮮血"
    },
    {
        subject: "警察杯杯",
        description: "很機車在抓紅燈右轉"
    },
    {
        subject: "電梯",
        description: "又壞了",
        place: "科研大樓"
    },
    {
        subject: "電梯",
        description: "裡面的味道好臭",
        place: "科研大樓"
    },
    {
        subject: "電梯",
        description: "人潮好多",
        place: "科研大樓"
    },
    {
        subject: "喵喵小六",
        description: "在睡覺",
        place: "7-11"
    },
    {
        subject: "玉蘭花婆婆",
        description: "今天賣的玉蘭花好香喔",
        place: "忠孝捷運4號出口"
    },
    {
        subject: "討厭的推銷員",
        description: "在包夾妹子",
        place: "mos附近"
    },
    {
        subject: "Teddy",
        description: "今天請要加課",
        place: "科研3F"
    },
    {
        subject: "籃球場",
        description: "好多人,根本沒有位置"
    },
    {
        subject: "一群漂亮妹子",
        description: "穿熱褲跑步",
        place: "操場"
    },
    {
        subject: "全家霜淇淋",
        description: "買一送一活動倒數一天"
    },
    {
        subject: "Big Issue",
        description: "這期的封面人物是小勞勃道尼耶"
    },
    {
        subject: "仙草冰",
        description: "加賣剉冰了"
    },
    {
        subject: "科開為老師",
        description: "開始點名了",
        place: "科研13F"
    },
    {
        subject: "三創",
        description: "開幕全館九折"
    },
    {
        subject: "兩隻北科怪鳥",
        description: "在互相追逐",
        place: "二教門口前"
    },
    {
        subject: "北科怪鳥",
        description: "出來覓食了",
        place: "7-11附近"
    },
    {
        subject: "香腸伯",
        description: "出來擺攤了",
        place: "建國高架橋下附近"
    },
    {
        subject: "煩人的問卷調查員",
        description: "又出現了",
        place: "六教一樓"
    },
    {
        subject: "警察",
        description: "出來開紅單拉",
        place: "原味小巷子"
    },
    {
        subject: "星巴克",
        description: "買一送一"
    },

    {
        subject: "護城河",
        description: "都快要漫出來了"
    },
    {
        subject: "Big Issue",
        description: "開賣了",
        place: "捷運四號出口前"
    },
    {
        subject: "烤地瓜",
        description: "開賣了",
        place: "捷運四號出口前"
    },
    {
        subject: "可疑人士",
        description: "出沒",
        place: "計程車休息站"
    },
    {
        subject: "可疑人士",
        description: "出沒",
        place: "排球場"
    },
    {
        subject: "原味",
        description: "今天休息"
    },
    {
        subject: "烏龜",
        description: "偷偷的跑出來",
        place: "生態池"
    },
    {
        subject: "飲水機",
        description: "沒水可以喝了",
        place: "地下閱覽室"
    },
    {
        subject: "地下閱覽室",
        description: "爆滿"
    },
    {
        subject: "設計系",
        description: "期末展出中",
        place: "圖書館一樓"
    },
    {
        subject: "服務學習",
        description: "成果發表展出中",
        place: "三教一樓"
    },
    {
        subject: "經管周",
        description: "開始了"
    },
    {
        subject: "學校網路",
        description: "又不穩了"
    },
    {
        subject: "學校網路",
        description: "連不上"
    },
    {
        subject: "烏龜",
        description: "偷偷爬出去",
        place: "生態池"
    }];

function run(i) {
    api("POST", "issue/raise", datas[i], true, function (result) {
        console.log(result);
        if (i + 1 < datas.length) {
            run(i + 1);
        }
    });
}

run(0);

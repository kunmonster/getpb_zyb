"use strict";

Object.defineProperty(exports, "__esModule", {
  value: true
});

var _sparkMD = require("./sparkMD5");

var _sparkMD2 = _interopRequireDefault(_sparkMD);

var _uuid = require("./uuid");

var _uuid2 = _interopRequireDefault(_uuid);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

/**
 * 防刷规则，前审，作答，一审，二审领题增加sign
  // 前端默认入参
    $businessId = "uuid随机生成""
    $ts = 1605602021;
    // 4个行为对应4个 key, 前后端约定
    $key = "a12edjaksd";

    // 签名过程
    // md5 businessid
    $businessId = md5($businessId);
    // 取结果后3位
    $value = substr($businessId, -3);
    // 后3位作为16进制值转换成10进制 % 32 + 1 得到 limit 偏移量
    $limit = (hexdec($value) % 32 ) + 1;
    // ts+businessID截取前 limit 长度+key 做md5
    $sign = md5($ts . substr($businessId, 0, $limit). $key);

    keymap 
    /commitui/preview/commitorder   XQwsE6%z
    /commitui/firstcheck/commitcheck af*Xw!Z0
    /commitui/secondcheck/commitcheck  1cEHYOZH
    /commitui/api/answer   bX%xw0rC
*/

// const sparkMD5 = require('./sparkMD5');
// const uuid = require('./uuid');
function createSign(key) {
  var businessId = (0, _uuid2.default)();
  var ts = parseInt(Date.now() / 1000);
  var md5BusinessId = _sparkMD2.default.hash(businessId);
  var last3 = md5BusinessId.substr(md5BusinessId.length - 3);
  var limit = parseInt(last3, 16) % 32 + 1;
  var sign = _sparkMD2.default.hash("" + ts + md5BusinessId.substr(0, limit) + key);
  return {
    businessId: businessId,
    ts: ts,
    sign: sign
  };
}
var m = createSign();
exports.default = createSign();
module.exports = createSign();



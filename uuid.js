"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var chars = '0123456789ABCDEFabcdef';
var size = chars.length;
function default_1(len) {
    if (len === void 0) { len = 32; }
    return new Array(len).fill('0').map(function () {
        return chars[Math.floor(size * Math.random())];
    }).join('');
}
exports.default = default_1;

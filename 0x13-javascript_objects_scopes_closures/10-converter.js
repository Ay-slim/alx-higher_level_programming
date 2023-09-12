#!/usr/bin/node
function mapHex (mod) {
  if (['1', '2', '3', '4', '5', '6', '7', '8', '9'].includes(String(mod))) {
    return String(mod);
  }
  return { 10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f' }[String(mod)];
}
exports.converter = function (base) {
  return function recDiv (num, ans = '') {
    if (base === 10) {
      return String(num);
    }
    if (!num) {
      return ans;
    }
    return recDiv(Math.floor(num / base), mapHex(num % base) + ans);
  };
};

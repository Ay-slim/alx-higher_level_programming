#!/usr/bin/node
exports.converter = function (base) {
  return function recDiv (num, ans = '') {
    if (base === 10) {
      return String(num);
    }
    if (!num) {
      return ans;
    }
    return recDiv(Math.floor(num / base), { 0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f' }[String(num % base)] + ans);
  };
};

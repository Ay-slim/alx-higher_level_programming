#!/usr/bin/node
exports.converter = function (base) {
  return function recDiv (num, ans = '') {
    if (base === 10) {
      return String(num);
    }
    if (!num) {
      return ans;
    }
    return recDiv(Math.floor(num / base), { 0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f', 16: 'g', 17: 'h', 18: 'i', 19: 'j', 20: 'k', 21: 'l', 22: 'm', 23: 'n', 24: 'o', 25: 'p', 26: 'q', 27: 'r', 28: 's', 29: 't', 30: 'u', 31: 'v' }[String(num % base)] + ans);
  };
};

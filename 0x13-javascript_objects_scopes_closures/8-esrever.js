#!/usr/bin/node
const swap = (list, frst, scnd) => {
  const tmp = list[frst];
  list[frst] = list[scnd];
  list[scnd] = tmp;
};
exports.esrever = function (list) {
  let startIdx = 0;
  let endIdx = list.length - 1;
  const halfWay = Math.floor(list.length / 2);
  while (startIdx < halfWay) {
    swap(list, startIdx, endIdx);
    startIdx++;
    endIdx--;
  }
  return list;
};

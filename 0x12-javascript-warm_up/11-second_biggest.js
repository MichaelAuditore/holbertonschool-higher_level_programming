#!/usr/bin/node
/* getting the second biggest number in argvs */
const args = process.argv.slice(2);

if (!args[0] || args.length == 1) {
  console.log(0);
} else {
  let max = 0;
  let len = args.length;
  for (let i = 0; i < len; i++) {
      if (args[i] > args[len]) {
	  if (args[i] >= max && i < len - 1) {
	      max = args[i];
	  }
      }
      len--;
  }
  console.log(max);
}

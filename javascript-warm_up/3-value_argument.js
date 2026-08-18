#!/usr/bin/node

const numOA = process.argv[2];

if (process.argv[2] === undefined) {
    console.log('No argument');
} else {
    console.log(process.argv[2]);
}

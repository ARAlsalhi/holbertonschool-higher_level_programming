#!/usr/bin/node

const numOA = process.argv[2];

if (numOA === undefined) {
    console.log('No argument');
} else {
    console.log(process.argv[2]);
}

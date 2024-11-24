#!/bin/bash

cat aviation.json | jq -r .[0].receiptTime
cat aviation.json | jq -r .[1].receiptTime
cat aviation.json | jq -r .[2].receiptTime
cat aviation.json | jq -r .[3].receiptTime
cat aviation.json | jq -r .[4].receiptTime
cat aviation.json | jq -r .[5].receiptTime

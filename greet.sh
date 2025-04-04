#!/bin/bash
echo "What's your name?"
read name
if [ "$name" == "Dmitrii" ]; then
  echo "Welcome back, Dmitrii!"
else
  echo "Hello $name!"
fi

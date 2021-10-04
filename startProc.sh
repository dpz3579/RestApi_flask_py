#!/bin/sh
LINE="python3 init.py"
stop()
{
  pkill -f "$LINE"
}
clean()
{
  stop
  exit 0
}
trap stop 1
trap clean 9 15
while true
  do
    $LINE &
    wait
done

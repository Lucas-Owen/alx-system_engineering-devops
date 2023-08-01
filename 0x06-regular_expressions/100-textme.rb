#!/usr/bin/env ruby
sender = ARGV[0].scan(/\[from:[^\]]{1,}/).join.split(':', 2)[1]
receiver = ARGV[0].scan(/\[to:[^\]]{1,}/).join.split(':', 2)[1]
flags = ARGV[0].scan(/\[flags:[^\]]{1,}/).join.split(':', 2)[1]
print sender, ",", receiver, ",", flags, "\n"

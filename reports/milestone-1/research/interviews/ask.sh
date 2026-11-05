#!/bin/sh
# usage: ask.sh <role> <label> <question>  – append the interviewer's turn to the transcript before it is sent
printf '**Interviewer (%s):** %s\n\n' "$2" "$3" >> "$(dirname "$0")/transcripts/$1.md"

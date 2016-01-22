#!/bin/sh

awk 'BEGIN{L=6.4}{print $1,$2*L,$3*L,$4*L}'

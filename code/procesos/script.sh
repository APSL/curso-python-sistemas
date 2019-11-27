#!/bin/sh

echo "Todos los argumentos: $@"
echo "arg 1: $1"
echo "arg 2: $2"

echo "Salida stderr" 1>&2

echo "VAR: $VAR"

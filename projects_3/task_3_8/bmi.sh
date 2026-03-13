#!/bin/bash
read -p "Введите свою массу в кг: " m
read -p "Введите свой рост в м: " h
echo $"scale=2; $m / ( $h * $h )" | bc

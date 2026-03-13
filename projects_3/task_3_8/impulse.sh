#!/bin/bash
read -p "Имя гена: " name
read -p "Уровень его экспрессии: " lvl
if [[ -z "$name" ]] || [[ -z "$lvl" ]]; then
    echo "Ошибка: недостаточно данных"
else
    echo "Экспрессия гена $name составляет $lvl единиц"
fi

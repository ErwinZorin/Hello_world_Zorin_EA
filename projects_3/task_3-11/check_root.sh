#!/bin/bash
check_root() {
    if [[ $EUID -ne 0 ]]; then
        echo "Ошибка" >&2
    fi
}
check_root

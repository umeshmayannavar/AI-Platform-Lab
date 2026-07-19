#!/usr/bin/env bash

###############################################################################
# Shared shell helpers for AI Platform scripts.
###############################################################################

readonly GREEN="\033[0;32m"
readonly RED="\033[0;31m"
readonly YELLOW="\033[1;33m"
readonly NC="\033[0m"

print_banner() {
    local title="$1"

    echo
    echo "============================================================"
    printf "%s\n" "$title"
    echo "============================================================"
}

section() {
    echo
    echo "------------------------------------------------------------"
    echo "$1"
    echo "------------------------------------------------------------"
}

info() {
    printf "%s\n" "$1"
}

success() {
    printf "%b✓ %-20s%b\n" "$GREEN" "$1" "$NC"
}

error() {
    printf "%b✗ %-20s%b\n" "$RED" "$1" "$NC"
}

warning() {
    printf "%b! %-18s%b %s\n" "$YELLOW" "$1" "$NC" "$2"
}

pass_check() {
    printf "%b✓ %-18s%b %s\n" "$GREEN" "$1" "$NC" "$2"
}

fail_check() {
    printf "%b✗ %-18s%b %s\n" "$RED" "$1" "$NC" "$2"
}

command_exists() {
    command -v "$1" >/dev/null 2>&1
}

print_summary() {
    local passed="$1"
    local failed="$2"

    echo "Passed : $passed"
    echo "Failed : $failed"
}

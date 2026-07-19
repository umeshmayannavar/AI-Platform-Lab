#!/usr/bin/env bash

###############################################################################
# AI Platform Bootstrap
#
# Installs all required tools for AI Platform development.
#
# Safe to run multiple times.
###############################################################################

set -uo pipefail

GREEN="\033[0;32m"
RED="\033[0;31m"
NC="\033[0m"

PASS=0
FAIL=0

###############################################################################
# Helper Functions
###############################################################################

header() {
    echo
    echo "============================================================"
    echo "              AI Platform Bootstrap"
    echo "============================================================"
    echo
}

section() {
    echo
    echo "------------------------------------------------------------"
    echo "$1"
    echo "------------------------------------------------------------"
}

success() {
    printf "${GREEN}✓ %-20s${NC}\n" "$1"
    ((++PASS))
}

failure() {
    printf "${RED}✗ %-20s${NC}\n" "$1"
    ((++FAIL))
}


###############################################################################
# Homebrew
###############################################################################

check_homebrew() {

    if command -v brew >/dev/null 2>&1; then
        success "Homebrew"
    else
        failure "Homebrew Missing"
        echo
        echo "Please install Homebrew first:"
        echo "https://brew.sh"
        exit 1
    fi
}

###############################################################################
# Formula Installer
###############################################################################

install_formula() {

    local package="$1"

    if brew list "$package" >/dev/null 2>&1; then
        success "$package (installed)"
    else
        info "Installing $package"
        brew install "$package"

        if brew list "$package" >/dev/null 2>&1; then
            success "$package"
        else
            failure "$package"
        fi
    fi
}

###############################################################################
# Cask Installer
###############################################################################

install_cask() {

    local package="$1"

    if brew list --cask "$package" >/dev/null 2>&1; then
        success "$package (installed)"
    else
        info "Installing $package"
        brew install --cask "$package"

        if brew list --cask "$package" >/dev/null 2>&1; then
            success "$package"
        else
            failure "$package"
        fi
    fi
}

###############################################################################
# Main
###############################################################################

header

section "Checking Homebrew"

check_homebrew

section "Installing CLI Tools"

install_formula gh
install_formula kubectl
install_formula kind
install_formula helm
install_formula k9s
install_formula ollama

section "Summary"

echo
echo "Passed : $PASS"
echo "Failed : $FAIL"

echo

if [[ $FAIL -eq 0 ]]; then
    printf "%b\n" "${GREEN}Bootstrap completed successfully.${NC}"
else
    printf "%b\n" "${RED}Bootstrap completed with errors.${NC}"
fi
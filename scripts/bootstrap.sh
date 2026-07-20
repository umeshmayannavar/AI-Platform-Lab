#!/usr/bin/env bash

###############################################################################
# AI Platform Bootstrap
#
# Installs all required tools for AI Platform development.
#
# Safe to run multiple times.
###############################################################################

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=lib/common.sh
source "$SCRIPT_DIR/lib/common.sh"

PASS=0
FAIL=0

###############################################################################
# Helper Functions
###############################################################################

mark_success() {
    success "$1"
    ((++PASS))
}

failure() {
    error "$1"
    ((++FAIL))
}

###############################################################################
# Homebrew
###############################################################################

check_homebrew() {

    if command_exists brew; then
        mark_success "Homebrew"
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
    local binary="${2:-$package}"

    if brew list "$package" >/dev/null 2>&1; then
        mark_success "$package (already installed)"
        return
    fi

    if command_exists "$binary"; then
        mark_success "$package (already available)"
        return
    fi

    info "Installing $package"

    if brew install "$package" && brew list "$package" >/dev/null 2>&1; then
        mark_success "$package"
    else
        failure "$package"
    fi
}

###############################################################################
# Cask Installer
###############################################################################

install_cask() {

    local package="$1"

    if brew list --cask "$package" >/dev/null 2>&1; then
        mark_success "$package (already installed)"
        return
    fi

    info "Installing $package"

    if brew install --cask "$package" && brew list --cask "$package" >/dev/null 2>&1; then
        mark_success "$package"
    else
        failure "$package"
    fi
}

###############################################################################
# Main
###############################################################################

print_banner "              AI Platform Bootstrap"
echo

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
print_summary "$PASS" "$FAIL"

echo

if [[ $FAIL -eq 0 ]]; then
    printf "%b\n" "${GREEN}Bootstrap completed successfully.${NC}"
else
    printf "%b\n" "${RED}Bootstrap completed with errors.${NC}"
fi

if ! command -v uv >/dev/null 2>&1; then
    echo "Installing uv..."
    brew install uv
fi
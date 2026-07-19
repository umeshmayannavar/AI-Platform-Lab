#!/usr/bin/env bash

###############################################################################
# AI Platform Foundation Doctor
#
# Purpose:
#   Validate that the local workstation is ready for AI Platform development.
#
# Exit Codes:
#   0 - Platform Ready
#   1 - One or more checks failed
###############################################################################

set -uo pipefail

GREEN="\033[0;32m"
RED="\033[0;31m"
YELLOW="\033[1;33m"
BLUE="\033[0;34m"
NC="\033[0m"

PASS=0
FAIL=0

###############################################################################
# Helper Functions
###############################################################################

print_header() {
    echo
    echo "============================================================"
    echo "             AI Platform Foundation Doctor"
    echo "============================================================"
    echo
}

print_section() {
    echo
    echo "------------------------------------------------------------"
    echo "$1"
    echo "------------------------------------------------------------"
}

pass() {
    printf "${GREEN}✓ %-18s${NC} %s\n" "$1" "$2"
    ((++PASS))
}

fail() {
    printf "${RED}✗ %-18s${NC} %s\n" "$1" "$2"
    ((++FAIL))
}

warning() {
    printf "${YELLOW}! %-18s${NC} %s\n" "$1" "$2"
}

###############################################################################
# Tool Checks
###############################################################################

check_tool() {

    local name="$1"
    local binary="$2"
    local version_command="$3"

    if command -v "$binary" >/dev/null 2>&1; then

        version=$($version_command 2>/dev/null | head -1)

        if [[ -z "$version" ]]; then
            version="Installed"
        fi

        pass "$name" "$version"

    else
        fail "$name" "Not Installed"
    fi
}

###############################################################################
# Docker
###############################################################################

check_docker_engine() {

    if ! command -v docker >/dev/null 2>&1; then
        return
    fi

    if docker info >/dev/null 2>&1; then
        pass "Docker Engine" "Running"
    else
        fail "Docker Engine" "Not Running"
    fi
}

###############################################################################
# Ollama
###############################################################################

check_ollama_service() {

    if ! command -v ollama >/dev/null 2>&1; then
        return
    fi

    if curl -s http://localhost:11434/api/tags >/dev/null; then
        pass "Ollama Service" "Running"
    else
        fail "Ollama Service" "Not Running"
    fi
}

###############################################################################
# Local Models
###############################################################################

check_model() {

    if ! command -v ollama >/dev/null 2>&1; then
        return
    fi

    if ollama list | grep -q "qwen3:8b"; then
        pass "Model" "qwen3:8b"
    else
        warning "Model" "qwen3:8b not found"
        ((++FAIL))
    fi
}

###############################################################################
# Summary
###############################################################################

summary() {

    echo
    echo "============================================================"
    echo "Summary"
    echo "============================================================"

    echo "Passed : $PASS"
    echo "Failed : $FAIL"

    echo

    if [[ $FAIL -eq 0 ]]; then
        printf "${GREEN}✓ PLATFORM READY FOR DEVELOPMENT${NC}\n"
        exit 0
    else
        printf "${RED}✗ PLATFORM REQUIRES ATTENTION${NC}\n"
        exit 1
    fi
}

###############################################################################
# Main
###############################################################################

print_header

print_section "Checking Required Tools"

check_tool "Git" "git" "git --version"
check_tool "Python" "python3" "python3 --version"
check_tool "Docker" "docker" "docker --version"
check_tool "kubectl" "kubectl" "kubectl version --client"
check_tool "Kind" "kind" "kind version"
check_tool "Helm" "helm" "helm version --short"
check_tool "k9s" "k9s" "k9s version -s"
check_tool "Ollama" "ollama" "ollama --version"

print_section "Checking Services"

check_docker_engine
check_ollama_service

print_section "Checking AI Models"

check_model

summary
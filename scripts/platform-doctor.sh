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

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=scripts/lib/common.sh
source "$SCRIPT_DIR/lib/common.sh"

PASS=0
FAIL=0

###############################################################################
# Helper Functions
###############################################################################

pass() {
    pass_check "$1" "$2"
    ((++PASS))
}

fail() {
    fail_check "$1" "$2"
    ((++FAIL))
}

###############################################################################
# Tool Checks
###############################################################################

check_tool() {

    local name="$1"
    local binary="$2"
    local version_command="$3"
    local version

    if command_exists "$binary"; then

        version=$($version_command 2>/dev/null | head -1 || true)

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

    if ! command_exists docker; then
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

    if ! command_exists ollama; then
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

    if ! command_exists ollama; then
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

    print_banner "Summary"
    print_summary "$PASS" "$FAIL"

    echo

    if [[ $FAIL -eq 0 ]]; then
        printf "%b\n" "${GREEN}✓ PLATFORM READY FOR DEVELOPMENT${NC}"
        exit 0
    else
        printf "%b\n" "${RED}✗ PLATFORM REQUIRES ATTENTION${NC}"
        exit 1
    fi
}

###############################################################################
# Main
###############################################################################

print_banner "             AI Platform Foundation Doctor"
echo

section "Checking Required Tools"

check_tool "Git" "git" "git --version"
check_tool "Python" "python3" "python3 --version"
check_tool "Docker" "docker" "docker --version"
check_tool "kubectl" "kubectl" "kubectl version --client"
check_tool "Kind" "kind" "kind version"
check_tool "Helm" "helm" "helm version --short"
check_tool "k9s" "k9s" "k9s version -s"
check_tool "Ollama" "ollama" "ollama --version"

section "Checking Services"

check_docker_engine
check_ollama_service

section "Checking AI Models"

check_model

summary

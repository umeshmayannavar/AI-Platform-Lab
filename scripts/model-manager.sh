#!/usr/bin/env bash

###############################################################################
# Model Manager
#
# Manage Ollama models running inside the Docker Compose container.
###############################################################################

set -euo pipefail

PROJECT_NAME="${COMPOSE_PROJECT_NAME:-ai-platform-lab}"
OLLAMA_CONTAINER="${PROJECT_NAME}-ollama"

###############################################################################
# Helpers
###############################################################################

print_header() {
    echo
    echo "------------------------------------------------------------"
    echo "$1"
    echo "------------------------------------------------------------"
}

usage() {
    cat <<EOF
Usage:
  $0 list
  $0 pull <model>
  $0 remove <model>

Examples:
  $0 list
  $0 pull qwen3:8b
  $0 pull nomic-embed-text
  $0 remove qwen3:8b
EOF
}

check_container() {
    if ! docker ps --format '{{.Names}}' | grep -qx "$OLLAMA_CONTAINER"; then
        echo "ERROR: Ollama container '$OLLAMA_CONTAINER' is not running."
        echo
        echo "Start it first:"
        echo "  docker compose up -d"
        exit 1
    fi
}

run_ollama() {
    docker compose exec -T ollama ollama "$@"
}

###############################################################################
# Commands
###############################################################################

list_models() {
    print_header "Available Models"
    run_ollama list
}

pull_model() {
    local model="$1"

    print_header "Pulling Model"

    echo "$model"
    echo

    run_ollama pull "$model"
}

remove_model() {
    local model="$1"

    print_header "Removing Model"

    echo "$model"
    echo

    run_ollama rm "$model"
}

###############################################################################
# Main
###############################################################################

if [[ $# -lt 1 ]]; then
    usage
    exit 1
fi

check_container

case "$1" in
    list)
        list_models
        ;;
    pull)
        [[ $# -eq 2 ]] || {
            usage
            exit 1
        }
        pull_model "$2"
        ;;
    remove|rm)
        [[ $# -eq 2 ]] || {
            usage
            exit 1
        }
        remove_model "$2"
        ;;
    *)
        usage
        exit 1
        ;;
esac
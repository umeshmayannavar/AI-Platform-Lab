#!/usr/bin/env bash

###############################################################################
# AI Platform Lab
#
# Model Manager
#
# Wrapper around the Ollama CLI.
###############################################################################

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# shellcheck source=scripts/lib/common.sh
source "$SCRIPT_DIR/lib/common.sh"

usage() {
    cat <<EOF

Usage:

  model-manager.sh list

  model-manager.sh pull <model>

  model-manager.sh remove <model>

Examples

  model-manager.sh list

  model-manager.sh pull qwen3:8b

  model-manager.sh remove qwen3:8b

EOF
}

require_model() {

    if [[ $# -lt 1 || -z "$1" ]]; then
        printf "%bERROR:%b MODEL is required.\n" "$RED" "$NC"
        exit 1
    fi
}
list_models() {

    section "Available Models"

    if ! ollama list | sed 1d | grep -q .; then
        echo "No local models installed."
        echo
        echo "Download one with:"
        echo "  make model-pull MODEL=qwen3:8b"
        return
    fi

    ollama list
}

pull_model() {

    local model="$1"

    section "Pulling Model"

    echo "$model"
    echo

    ollama pull "$model"
}

remove_model() {

    local model="$1"

    section "Removing Model"

    echo "$model"
    echo

    ollama rm "$model"
}

main() {

    if [[ $# -lt 1 ]]; then
        usage
        exit 1
    fi

    case "$1" in

        list)
            list_models
            ;;

        pull)
            require_model "${2:-}"
            pull_model "$2"
            ;;

        remove)
            require_model "${2:-}"
            remove_model "$2"
            ;;

        *)
            usage
            exit 1
            ;;

    esac
}

main "$@"
###############################################################################
# AI Platform Lab
#
# Primary developer interface for the repository.
###############################################################################

.DEFAULT_GOAL := help

SCRIPTS_DIR := scripts
BASH_SCRIPTS := $(wildcard $(SCRIPTS_DIR)/*.sh) $(wildcard $(SCRIPTS_DIR)/lib/*.sh)

DOCTOR := $(SCRIPTS_DIR)/platform-doctor.sh
BOOTSTRAP := $(SCRIPTS_DIR)/bootstrap.sh
MODEL_MANAGER := $(SCRIPTS_DIR)/model-manager.sh

.PHONY: help doctor bootstrap lint status clean fmt \
        model-list model-pull model-remove

###############################################################################
# Setup
###############################################################################

##@ Setup

bootstrap: ## Install required developer tools
	@$(BOOTSTRAP)

###############################################################################
# Validation
###############################################################################

##@ Validation

doctor: ## Validate the local development environment
	@$(DOCTOR)

lint: ## Run ShellCheck on project scripts
	@shellcheck -P $(SCRIPTS_DIR) $(BASH_SCRIPTS)

###############################################################################
# AI Models
###############################################################################

##@ AI Models

model-list: ## List available Ollama models
	@$(MODEL_MANAGER) list

model-pull: ## Download an Ollama model
	@if [ -z "$(MODEL)" ]; then \
		echo "ERROR: MODEL is required."; \
		echo ""; \
		echo "Example:"; \
		echo "  make model-pull MODEL=qwen3:8b"; \
		exit 1; \
	fi
	@$(MODEL_MANAGER) pull $(MODEL)

model-remove: ## Remove an Ollama model
	@if [ -z "$(MODEL)" ]; then \
		echo "ERROR: MODEL is required."; \
		echo ""; \
		echo "Example:"; \
		echo "  make model-remove MODEL=qwen3:8b"; \
		exit 1; \
	fi
	@$(MODEL_MANAGER) remove $(MODEL)

###############################################################################
# Development
###############################################################################

##@ Development

help: ## Show this help menu
	@echo ""
	@echo "AI Platform Lab"
	@echo "==============="
	@echo ""
	@echo "Usage: make <target>"
	@echo ""
	@echo "Available Commands"
	@echo ""
	@awk 'BEGIN { FS = ":.*##"; } \
		/^##@/ { \
			if (section) { print ""; } \
			section = substr($$0, 5); \
			print section; \
			for (i = 1; i <= length(section); i++) { printf "-"; } \
			print ""; \
			next; \
		} \
		/^[a-zA-Z0-9_.-]+:.*##/ { printf "  %-15s %s\n", $$1, $$2; }' $(MAKEFILE_LIST)
	@echo ""

fmt: ## Format project scripts (future)
	@echo "Formatting support will be added in a future release."

###############################################################################
# Utilities
###############################################################################

##@ Utilities

status: ## Show Git repository status
	@git status

clean: ## Remove temporary files
	@find . -name ".DS_Store" -delete
	@echo "Workspace cleaned."
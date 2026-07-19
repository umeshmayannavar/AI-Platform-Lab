###############################################################################
# AI Platform Foundation
#
# Primary developer interface for the repository.
###############################################################################

.DEFAULT_GOAL := help

SCRIPTS_DIR := scripts

DOCTOR := $(SCRIPTS_DIR)/platform-doctor.sh
BOOTSTRAP := $(SCRIPTS_DIR)/bootstrap.sh

.PHONY: help doctor bootstrap status clean fmt

###############################################################################
# Help
###############################################################################

help:
	@echo ""
	@echo "============================================================"
	@echo "               AI Platform Foundation"
	@echo "============================================================"
	@echo ""
	@echo "Usage:"
	@echo "  make <target>"
	@echo ""
	@echo "Available Targets:"
	@echo ""
	@printf "  %-15s %s\n" "doctor" "Validate local development environment"
	@printf "  %-15s %s\n" "bootstrap" "Install required development tools"
	@printf "  %-15s %s\n" "status" "Show Git repository status"
	@printf "  %-15s %s\n" "clean" "Remove temporary files"
	@printf "  %-15s %s\n" "fmt" "Format project scripts (future)"
	@echo ""

###############################################################################
# Platform
###############################################################################

doctor:
	@$(DOCTOR)

bootstrap:
	@$(BOOTSTRAP)

###############################################################################
# Git
###############################################################################

status:
	@git status

###############################################################################
# Maintenance
###############################################################################

clean:
	@find . -name ".DS_Store" -delete
	@echo "Workspace cleaned."

fmt:
	@echo "Formatting support will be added in a future release."
# Thin wrapper over the build-report skill (settings in tasks.toml). Examples:
#   make all                 precheck → build → postcheck for every task, then the tests
#   make translate TASK=task2       make build TASK=task2 L=vi      make precheck TASK=task1      make test
#   make pages TASK=task1 BUDGET=10  page budget of the built documents (optimistic and pessimistic layout)
# L is the report language (a language pack code, or all); LANG is avoided because it is the shell locale.
# Install: copy this file to the project root (the folder holding tasks.toml).

PY     ?= $(if $(wildcard ./venv/bin/python),./venv/bin/python,python3)
REPORT := $(PY) .claude/skills/build-report/scripts/report.py
TASK   ?= all
L      ?= all

.PHONY: help list translate precheck build postcheck test all pages

help:
	@sed -n '1,5p' Makefile
	@$(REPORT) list

list:
	@$(REPORT) list

translate:
	@$(REPORT) translate $(TASK) --lang $(L)

precheck:
	@$(REPORT) precheck $(TASK)

build:
	@$(REPORT) build $(TASK) --lang $(L)

postcheck:
	@$(REPORT) postcheck $(TASK) --lang $(L)

test:
	@$(REPORT) test

pages:
	@$(PY) .claude/skills/build-report/scripts/page_budget.py --task $(TASK) $(if $(BUDGET),--budget $(BUDGET))

all:
	@$(REPORT) all $(TASK) --lang $(L) && $(REPORT) test

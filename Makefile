PYTHON := .venv/bin/python
PIP := .venv/bin/pip

.PHONY: setup reproduce validate test acquire manuscript

setup: $(PYTHON)

$(PYTHON): requirements.txt
	python3 -m venv .venv
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

reproduce: setup
	@if [ $$(ls data/raw/weather/*_era5_1991_2020.json 2>/dev/null | wc -l) -lt 8 ]; then \
		PYTHONPATH=. $(PYTHON) src/acquire_weather.py; \
	fi
	PYTHONPATH=. $(PYTHON) run_all.py

validate: setup
	PYTHONPATH=. $(PYTHON) run_all.py --validate-only

test: setup
	PYTHONPATH=. $(PYTHON) -m pytest tests -q

manuscript: setup
	PYTHONPATH=. $(PYTHON) analysis/build_manuscript_assets.py
	PYTHONPATH=. $(PYTHON) manuscript/build_manuscript.py

acquire: setup
	PYTHONPATH=. $(PYTHON) src/acquire_weather.py
	PYTHONPATH=. $(PYTHON) src/acquire_literature.py

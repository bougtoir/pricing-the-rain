# Execution environment

- Captured: 2026-09-24 UTC
- Host: single persistent Devin Cloud VM
- OS: Ubuntu Linux, kernel 6.8.0-1061-aws, x86_64
- CPU: 2 logical cores
- Memory: 7.8 GiB RAM, no swap
- Disk at start: 124 GiB total, 100 GiB available
- Python: 3.10.12
- Primary environment: `.venv`
- pip: 26.2.1 in `.venv`
- Git: 2.34.1
- GNU Make: 4.3
- LibreOffice: available at `/usr/bin/libreoffice`
- Initial repository commit: `7daa778e04e852fbaa48b0be024885b5c66eb0e8`
- Initial project directory: absent; created under `pricing-the-rain/`

All phases are executed sequentially in this VM. Expensive outputs are persisted under
`data/`, `analysis/`, and `results/`.

# Integration notes

This archive provides a PeerJ-ready repository layout and reproducibility documentation. To use it with the existing GitHub repository:

1. Unzip this archive.
2. Copy the contents of `CCT-MARL-peerj-github-ready/` into the root of `https://github.com/Huskieeeee/CCT-MARL`.
3. Replace any lightweight scaffold modules in `src/` and `scripts/` with the finalized training implementation when available.
4. Keep `README.md`, `CITATION.cff`, `.zenodo.json`, `LICENSE`, `reproduce_peerj_results.md`, `configs/`, `results/tables/`, and `docs/` in the repository root.
5. Run `bash run_smoke_test.sh`.
6. Commit all files and create a GitHub release named `v1.0.0-peerj-submission`.
7. Archive the release with Zenodo if a DOI is needed.

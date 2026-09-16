from __future__ import annotations

import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from validate_ane import EXPECTED_BASELINE, EXPECTED_INTERNAL_TARGETS, validate_manifest


def load_manifest() -> dict:
    return json.loads((ROOT / "routes.json").read_text(encoding="utf-8"))


class TestANENewImplementation(unittest.TestCase):
    def test_current_manifest_passes(self) -> None:
        report = validate_manifest(load_manifest())
        self.assertEqual(report["fail"], 0, report["errors"])

    def test_new_counter_starts_at_zero(self) -> None:
        self.assertEqual(load_manifest()["implementation"]["new_validation_counter_initial"], 0)

    def test_baseline_is_exact(self) -> None:
        self.assertEqual(load_manifest()["implementation"]["provenance_baseline"], EXPECTED_BASELINE)

    def test_internal_route_uses_verified_blob(self) -> None:
        route = load_manifest()["routes"][0]
        self.assertEqual(
            route["destination"]["blob_sha"],
            EXPECTED_INTERNAL_TARGETS[route["destination"]["path"]],
        )

    def test_duplicate_route_is_rejected(self) -> None:
        data = load_manifest()
        data["routes"].append(copy.deepcopy(data["routes"][0]))
        self.assertGreater(validate_manifest(data)["fail"], 0)

    def test_wrong_baseline_is_rejected(self) -> None:
        data = load_manifest()
        data["implementation"]["provenance_baseline"]["tree"] = "0" * 40
        self.assertGreater(validate_manifest(data)["fail"], 0)

    def test_non_https_external_route_is_rejected(self) -> None:
        data = load_manifest()
        data["routes"][1]["destination"]["url"] = "http://doi.org/10.5281/zenodo.21827928"
        self.assertGreater(validate_manifest(data)["fail"], 0)

    def test_unverified_internal_blob_is_rejected(self) -> None:
        data = load_manifest()
        data["routes"][0]["destination"]["blob_sha"] = "0" * 40
        self.assertGreater(validate_manifest(data)["fail"], 0)

    def test_unresolved_entry_cannot_invent_destination(self) -> None:
        data = load_manifest()
        data["unresolved"][0]["destination"] = "https://example.invalid"
        self.assertGreater(validate_manifest(data)["fail"], 0)

    def test_historical_boundary_is_required(self) -> None:
        data = load_manifest()
        del data["implementation"]["historical_boundary"]["historical_test_suite"]
        self.assertGreater(validate_manifest(data)["fail"], 0)


if __name__ == "__main__":
    unittest.main()

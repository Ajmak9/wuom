#!/usr/bin/env python3
"""Static validator for ANE NEW IMPLEMENTATION.

This validator intentionally checks only the versioned routing manifest.  It does
not fetch external services, scrape destinations, access Sites, or claim to
recover the historical ANE runtime.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse


EXPECTED_BASELINE = {
    "commit": "75c688634371e52ee5f45764c6ac955514309bb8",
    "tree": "d5b87c50cc8f62a21c77105fcd2e97a85915bb61",
}
EXPECTED_INTERNAL_TARGETS = {
    "docs/00_BIOIA_WUOM_ECOSYSTEM_READING_0.1.pdf": "bc8d1409f06186e651a3d5a04f4398896af73551",
}
EXPECTED_HISTORY = {
    "historical_ane_runtime": "not recovered",
    "historical_validation_record": "786/786 PASS",
    "historical_test_suite": "not recovered",
    "sites_v48": "preserved historical evidence, not source",
}
REQUIRED_ROUTE_FIELDS = {
    "id",
    "destination",
    "language",
    "source_type",
    "source_document",
    "provenance_baseline",
    "validated_at",
    "status",
    "custody",
}
ALLOWED_LANGUAGES = {"en", "es", "ca", "multilingual"}
ALLOWED_SOURCE_TYPES = {
    "documentation",
    "persistent_record",
    "public_entrypoint",
    "repository",
}
DATE_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}$")
SHA_PATTERN = re.compile(r"^[0-9a-f]{40}$")


class Checks:
    def __init__(self) -> None:
        self.total = 0
        self.errors: list[str] = []

    def check(self, condition: bool, message: str) -> None:
        self.total += 1
        if not condition:
            self.errors.append(message)


def is_https_url(value: object) -> bool:
    if not isinstance(value, str):
        return False
    parsed = urlparse(value)
    return parsed.scheme == "https" and bool(parsed.netloc)


def validate_manifest(data: object) -> dict[str, object]:
    checks = Checks()
    checks.check(isinstance(data, dict), "Manifest root must be an object.")
    if not isinstance(data, dict):
        return {
            "total_checks": checks.total,
            "pass": 0,
            "fail": len(checks.errors),
            "unresolved": 0,
            "errors": checks.errors,
        }

    implementation = data.get("implementation")
    checks.check(isinstance(implementation, dict), "Missing implementation object.")
    if not isinstance(implementation, dict):
        implementation = {}

    checks.check(
        implementation.get("name") == "ANE NEW IMPLEMENTATION",
        "Implementation name must be ANE NEW IMPLEMENTATION.",
    )
    checks.check(
        implementation.get("provenance_baseline") == EXPECTED_BASELINE,
        "Declared baseline must exactly match the independent baseline.",
    )
    checks.check(
        implementation.get("new_validation_counter_initial") == 0,
        "New validation counter must begin at zero.",
    )
    checks.check(
        DATE_PATTERN.fullmatch(str(implementation.get("validated_at", ""))) is not None,
        "Implementation validation date must use YYYY-MM-DD.",
    )
    checks.check(
        isinstance(implementation.get("custody_policy"), str)
        and "sensitive" in implementation["custody_policy"].lower(),
        "Custody policy must explicitly protect sensitive information.",
    )

    history = implementation.get("historical_boundary")
    checks.check(isinstance(history, dict), "Missing historical boundary.")
    if not isinstance(history, dict):
        history = {}
    for key, expected in EXPECTED_HISTORY.items():
        checks.check(history.get(key) == expected, f"Historical boundary mismatch: {key}.")

    sources = data.get("documentation_sources")
    checks.check(isinstance(sources, list) and bool(sources), "Documentation sources are required.")
    if not isinstance(sources, list):
        sources = []
    source_paths: set[str] = set()
    for source in sources:
        valid_source = isinstance(source, dict)
        checks.check(valid_source, "Each documentation source must be an object.")
        if not valid_source:
            continue
        path = source.get("path")
        source_paths.add(path if isinstance(path, str) else "")
        checks.check(isinstance(path, str) and bool(path), "Source path is required.")
        checks.check(source.get("commit") == EXPECTED_BASELINE["commit"], "Source commit must match baseline.")
        checks.check(
            SHA_PATTERN.fullmatch(str(source.get("blob_sha", ""))) is not None,
            "Source blob SHA must be a 40-character Git SHA.",
        )

    targets = data.get("internal_targets")
    checks.check(isinstance(targets, list), "Internal targets must be a list.")
    if not isinstance(targets, list):
        targets = []
    target_map: dict[str, str] = {}
    for target in targets:
        valid_target = isinstance(target, dict)
        checks.check(valid_target, "Each internal target must be an object.")
        if not valid_target:
            continue
        path = target.get("path")
        blob_sha = target.get("blob_sha")
        if isinstance(path, str) and isinstance(blob_sha, str):
            target_map[path] = blob_sha
        checks.check(target.get("baseline_tree") == EXPECTED_BASELINE["tree"], "Internal target tree must match baseline.")
        checks.check(
            EXPECTED_INTERNAL_TARGETS.get(path) == blob_sha,
            "Internal target path or blob SHA is not a verified baseline target.",
        )

    routes = data.get("routes")
    checks.check(isinstance(routes, list) and bool(routes), "At least one route is required.")
    if not isinstance(routes, list):
        routes = []
    route_ids: set[str] = set()
    route_destinations: set[str] = set()
    for route in routes:
        valid_route = isinstance(route, dict)
        checks.check(valid_route, "Each route must be an object.")
        if not valid_route:
            continue
        checks.check(
            REQUIRED_ROUTE_FIELDS.issubset(route),
            f"Route {route.get('id', '<unknown>')} is missing required fields.",
        )
        route_id = route.get("id")
        checks.check(isinstance(route_id, str) and bool(route_id), "Route id is required.")
        checks.check(route_id not in route_ids, f"Duplicate route id: {route_id}.")
        if isinstance(route_id, str):
            route_ids.add(route_id)
        checks.check(route.get("language") in ALLOWED_LANGUAGES, f"Unsupported route language: {route.get('language')}.")
        checks.check(route.get("source_type") in ALLOWED_SOURCE_TYPES, f"Unsupported source type: {route.get('source_type')}.")
        checks.check(route.get("source_document") in source_paths, f"Unknown source document: {route.get('source_document')}.")
        checks.check(route.get("provenance_baseline") == EXPECTED_BASELINE, "Route baseline must exactly match the independent baseline.")
        checks.check(DATE_PATTERN.fullmatch(str(route.get("validated_at", ""))) is not None, "Route validation date must use YYYY-MM-DD.")
        checks.check(route.get("status") == "VERIFIED_STATIC", "New routes must be VERIFIED_STATIC, never historical recovery claims.")
        checks.check(isinstance(route.get("custody"), str) and bool(route["custody"].strip()), "Each route requires custody text.")

        destination = route.get("destination")
        checks.check(isinstance(destination, dict), "Route destination must be an object.")
        if not isinstance(destination, dict):
            continue
        kind = destination.get("kind")
        if kind == "repository_path":
            path = destination.get("path")
            blob_sha = destination.get("blob_sha")
            checks.check(isinstance(path, str) and path in target_map, "Internal route target must be listed in internal_targets.")
            checks.check(target_map.get(path) == blob_sha, "Internal route blob SHA must match the verified target.")
            target_key = f"path:{path}"
        elif kind == "https_url":
            url = destination.get("url")
            checks.check(is_https_url(url), "External route destination must be an HTTPS URL.")
            target_key = f"url:{url}"
        else:
            checks.check(False, f"Unsupported destination kind: {kind}.")
            target_key = f"invalid:{route_id}"
        checks.check(target_key not in route_destinations, f"Duplicate route destination: {target_key}.")
        route_destinations.add(target_key)

    unresolved = data.get("unresolved")
    checks.check(isinstance(unresolved, list), "Unresolved entries must be a list.")
    if not isinstance(unresolved, list):
        unresolved = []
    unresolved_ids: set[str] = set()
    for item in unresolved:
        valid_item = isinstance(item, dict)
        checks.check(valid_item, "Each unresolved entry must be an object.")
        if not valid_item:
            continue
        item_id = item.get("id")
        checks.check(isinstance(item_id, str) and bool(item_id), "Unresolved id is required.")
        checks.check(item_id not in unresolved_ids, f"Duplicate unresolved id: {item_id}.")
        if isinstance(item_id, str):
            unresolved_ids.add(item_id)
        checks.check(item.get("status") == "UNRESOLVED", "Unresolved entry must explicitly use UNRESOLVED status.")
        checks.check(isinstance(item.get("reason"), str) and bool(item["reason"].strip()), "Unresolved entry requires a reason.")
        checks.check("destination" not in item, "Unresolved entry must not invent a destination.")

    failures = len(checks.errors)
    return {
        "total_checks": checks.total,
        "pass": checks.total - failures,
        "fail": failures,
        "unresolved": len(unresolved),
        "errors": checks.errors,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate ANE NEW IMPLEMENTATION routing manifest.")
    parser.add_argument(
        "--manifest",
        type=Path,
        default=Path(__file__).with_name("routes.json"),
        help="Path to routes.json (default: sibling routes.json)",
    )
    args = parser.parse_args()
    try:
        data = json.loads(args.manifest.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        report = {"total_checks": 0, "pass": 0, "fail": 1, "unresolved": 0, "errors": [str(exc)]}
        print(json.dumps(report, indent=2, sort_keys=True))
        return 1
    report = validate_manifest(data)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if report["fail"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())

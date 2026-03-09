#!/usr/bin/env python3
import redis # type: ignore
import pyinaturalist as pin # type: ignore

obs = pin.get_observations(
    place_id=18,
    per_page=200
)["results"]

taxon_ids = set()

for o in obs:
    taxon = o.get("taxon")
    if taxon:
        taxon_ids.add(taxon["id"])

taxon_ids = list(taxon_ids)

taxa = []

batch_size = 30

for i in range(0, len(taxon_ids), batch_size):
    batch = taxon_ids[i:i+batch_size]
    r = pin.get_taxa(ids=batch)
    taxa.extend(r["results"])

endangered = []

for t in taxa:
    statuses = t.get("conservation_statuses", [])
    for s in statuses:
        if s["status"] in ["EN", "CR", "VU"]:
            endangered.append((t["name"], s["status"]))

for name, status in endangered:
    print(name, status)
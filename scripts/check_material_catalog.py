"""Check the public asset catalog without reading private course content."""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATUSES = {'verified', 'linked-to-existing', 'online-only', 'reference-only',
            'access-blocked', 'failed'}
FIELDS = {'asset_id', 'source_ids', 'course_slug', 'artifact_kind', 'format',
          'status', 'bytes', 'canonical_asset_id', 'verified_date'}


def rows(name):
    with (ROOT / 'resources' / name).open(newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))


def main():
    sources = rows('sources.csv')
    source_map = {row['source_id']: row for row in sources}
    assert len(source_map) == len(sources), 'Duplicate lesson IDs'
    assets = rows('materials.csv')
    assert assets and set(assets[0]) == FIELDS, 'Unexpected public fields'
    asset_map = {row['asset_id']: row for row in assets}
    assert len(asset_map) == len(assets), 'Duplicate asset IDs'
    counts = {sid: 0 for sid in source_map}
    for asset in assets:
        assert asset['status'] in STATUSES, asset['asset_id']
        ids = asset['source_ids'].split(';')
        assert ids and len(set(ids)) == len(ids)
        for sid in ids:
            assert sid in source_map, sid
            assert source_map[sid]['course_slug'] == asset['course_slug'], sid
        for value in asset.values():
            assert '://' not in value and '/Users/' not in value, 'Private locator in public catalog'
        if asset['status'] in {'verified', 'linked-to-existing'}:
            canonical = asset_map[asset['canonical_asset_id']]
            assert canonical['status'] == 'verified'
            assert canonical['canonical_asset_id'] == canonical['asset_id']
            assert asset['format'] == canonical['format']
            assert int(asset['bytes']) == int(canonical['bytes']) > 0
            assert asset['verified_date']
            if asset['artifact_kind'] != 'page-snapshot':
                for sid in ids:
                    counts[sid] += 1
        else:
            assert not asset['canonical_asset_id']
    coverage = rows('material-coverage.csv')
    assert len(coverage) == len(source_map)
    assert {row['source_id'] for row in coverage} == set(source_map)
    for row in coverage:
        assert row['enumerated'] == 'True', row['source_id']
        assert int(row['verified_file_references']) == counts[row['source_id']]
        assert (row['no_verified_originals'] == 'True') == (counts[row['source_id']] == 0)
    print(f'Validated {len(assets)} asset records and {len(coverage)} lesson mappings.')


if __name__ == '__main__':
    main()

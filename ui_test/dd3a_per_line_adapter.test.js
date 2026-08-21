const assert = require('node:assert/strict');
const test = require('node:test');

const { adaptCanonicalResponse, buildPerLine } = require('./dd3a_per_line_adapter');

const unsupportedFields = [
  'source',
  'source_evidence',
  'interaction',
  'interaction_evidence',
  'derived_event',
  'phase',
  'trigger',
  'expected_time_window',
  'ground_truth',
  'confidence',
];

function movingIndexes(lines) {
  return buildPerLine(lines).filter((line) => line.moving).map((line) => line.index);
}

test('moving_lines=[3] maps only H3 to moving', () => {
  assert.deepEqual(movingIndexes([3]), [3]);
  assert.deepEqual(buildPerLine([3]).map((line) => line.moving), [false, false, true, false, false, false]);
});

test('moving_lines=[] maps all six lines to not moving', () => {
  assert.deepEqual(movingIndexes([]), []);
  assert.deepEqual(buildPerLine([]).map((line) => line.moving), [false, false, false, false, false, false]);
});

test('moving_lines=[1,6] maps the two boundary lines', () => {
  assert.deepEqual(movingIndexes([1, 6]), [1, 6]);
});

test('moving_lines=[3,3] is deduplicated', () => {
  const records = buildPerLine([3, 3]);
  assert.equal(records.length, 6);
  assert.deepEqual(movingIndexes([3, 3]), [3]);
});

test('moving_lines=[0,7] ignores out-of-range indices', () => {
  assert.deepEqual(movingIndexes([0, 7]), []);
});

test('adapter always emits the exact six-line schema without inference', () => {
  const canonical = {
    contract_version: '3.1.0',
    identity: { moving_lines: [3], root_code: 17, transformed_code: 21 },
    interpretation: { per_line: [{ line: 99, moving: false }] },
  };
  const adapted = adaptCanonicalResponse(canonical);

  assert.equal(adapted.contract_version, canonical.contract_version);
  assert.equal(adapted.identity, canonical.identity);
  assert.equal(adapted.interpretation.per_line.length, 6);
  assert.deepEqual(adapted.interpretation.per_line.map((line) => line.id), ['H1', 'H2', 'H3', 'H4', 'H5', 'H6']);
  assert.deepEqual(adapted.interpretation.per_line.map((line) => line.index), [1, 2, 3, 4, 5, 6]);
  assert.deepEqual(adapted.interpretation.per_line.map((line) => line.moving), [false, false, true, false, false, false]);
  for (const line of adapted.interpretation.per_line) {
    for (const field of unsupportedFields) assert.equal(line[field], 'UNSUPPORTED', `${line.id}.${field}`);
    assert.equal(Object.keys(line).length, 13);
  }
  assert.equal(canonical.interpretation.per_line[0].line, 99);
});

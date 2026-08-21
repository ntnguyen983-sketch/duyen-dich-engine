const test = require('node:test');
const assert = require('node:assert/strict');

const { adaptCanonicalResponse } = require('./dd3a_per_line_adapter');

test('adapter preserves the canonical per-line records from the API', () => {
  const canonical = {
    contract_version: '3.1.0',
    identity: { moving_lines: [3], root_code: 17, transformed_code: 21 },
    interpretation: {
      per_line: [
        { line: 1, bit: 1, moving: false, status: 'CANONICAL_IDENTITY' },
        { line: 2, bit: 0, moving: false, status: 'CANONICAL_IDENTITY' },
        { line: 3, bit: 0, moving: true, status: 'CANONICAL_INPUT' },
      ],
      cross_line: [],
      source_interaction: [],
    },
  };
  const adapted = adaptCanonicalResponse(canonical);

  assert.notEqual(adapted, canonical);
  assert.equal(adapted.contract_version, canonical.contract_version);
  assert.deepEqual(adapted.identity, canonical.identity);
  assert.deepEqual(adapted.interpretation.per_line, canonical.interpretation.per_line);
  assert.deepEqual(adapted.interpretation.cross_line, []);
  assert.deepEqual(adapted.interpretation.source_interaction, []);
  assert.equal(Object.hasOwn(adapted.interpretation.per_line[0], 'source'), false);
  assert.equal(Object.hasOwn(adapted.interpretation.per_line[0], 'index'), false);
  assert.deepEqual(canonical.interpretation.per_line[0], {
    line: 1,
    bit: 1,
    moving: false,
    status: 'CANONICAL_IDENTITY',
  });
});

test('adapter returns a safe empty interpretation when optional per_line is absent', () => {
  const adapted = adaptCanonicalResponse({ contract_version: '3.1.0', interpretation: {} });
  assert.deepEqual(adapted.interpretation.per_line, []);
});

test('adapter does not invent a response for invalid input', () => {
  assert.equal(adaptCanonicalResponse(null), null);
  assert.equal(adaptCanonicalResponse('not-json'), null);
});

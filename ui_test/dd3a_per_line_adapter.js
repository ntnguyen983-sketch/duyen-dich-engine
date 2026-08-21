(function (root, factory) {
  if (typeof module === 'object' && module.exports) {
    module.exports = factory();
  } else {
    root.DD3A = factory();
  }
})(typeof globalThis === 'object' ? globalThis : this, function () {
  'use strict';

  const UNSUPPORTED = 'UNSUPPORTED';
  const PER_LINE_FIELDS = Object.freeze([
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
  ]);

  function movingIndexSet(movingLines) {
    if (!Array.isArray(movingLines)) return new Set();
    return new Set(
      movingLines.filter((line) => Number.isInteger(line) && line >= 1 && line <= 6),
    );
  }

  function buildPerLine(movingLines) {
    const moving = movingIndexSet(movingLines);
    return Array.from({ length: 6 }, (_, offset) => {
      const index = offset + 1;
      const record = {
        id: `H${index}`,
        index,
        moving: moving.has(index),
      };
      for (const field of PER_LINE_FIELDS) record[field] = UNSUPPORTED;
      return record;
    });
  }

  function adaptCanonicalResponse(canonicalResponse) {
    const response = canonicalResponse && typeof canonicalResponse === 'object'
      ? canonicalResponse
      : {};
    const identity = response.identity && typeof response.identity === 'object'
      ? response.identity
      : {};
    const interpretation = response.interpretation && typeof response.interpretation === 'object'
      ? response.interpretation
      : {};

    return {
      ...response,
      interpretation: {
        ...interpretation,
        per_line: buildPerLine(identity.moving_lines),
      },
    };
  }

  return { adaptCanonicalResponse, buildPerLine };
});

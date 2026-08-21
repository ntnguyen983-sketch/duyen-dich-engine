(function (root, factory) {
  if (typeof module === 'object' && module.exports) {
    module.exports = factory();
  } else {
    root.DD3A = factory();
  }
})(typeof globalThis === 'object' ? globalThis : this, function () {
  'use strict';

  // DD-3A is a compatibility boundary only. It must never invent or replace
  // canonical interpretation records supplied by the v3.1 API.
  function adaptCanonicalResponse(canonicalResponse) {
    if (!canonicalResponse || typeof canonicalResponse !== 'object') return null;

    const interpretation = canonicalResponse.interpretation;
    if (!interpretation || typeof interpretation !== 'object') return canonicalResponse;

    return {
      ...canonicalResponse,
      interpretation: {
        ...interpretation,
        per_line: Array.isArray(interpretation.per_line)
          ? interpretation.per_line.map((line) => ({ ...line }))
          : [],
      },
    };
  }

  return { adaptCanonicalResponse };
});

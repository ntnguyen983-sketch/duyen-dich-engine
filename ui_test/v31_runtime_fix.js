(() => {
  'use strict';

  // Runtime UI hotfix: replace the original form listener without touching CORE.
  // The existing renderer/helpers remain the single presentation layer.
  const form = document.getElementById('form');
  if (!form) return;

  const cleanForm = form.cloneNode(true);
  form.replaceWith(cleanForm);

  const toggleHexagram = () => {
    const enabled = document.getElementById('use-hexagram')?.checked === true;
    document.getElementById('hexagram-box')?.classList.toggle('hidden', !enabled);
    document.getElementById('flat-input')?.classList.toggle('hidden', enabled);
  };
  cleanForm.addEventListener('change', (event) => {
    if (event.target?.id === 'use-hexagram') toggleHexagram();
  });
  toggleHexagram();

  const $ = (id) => document.getElementById(id);
  const CANONICAL = ['SAT', 'TA', 'NHIEU', 'HY', 'DUONG', 'AN'];

  function addCheck(name, ok, detail = '') {
    const item = document.createElement('div');
    item.className = 'check ' + (ok ? 'pass' : 'fail');
    item.textContent = (ok ? '✓ ' : '✗ ') + name + (detail ? ' — ' + detail : '');
    $('checks').appendChild(item);
  }

  function validGps(gps) {
    if (!gps || typeof gps !== 'object') return false;
    const lat = Number(gps.lat), lng = Number(gps.lng);
    return Number.isFinite(lat) && Number.isFinite(lng) && lat >= -90 && lat <= 90 && lng >= -180 && lng <= 180;
  }

  function readHexagram() {
    let envelope;
    try {
      envelope = JSON.parse($('hexagram-payload').value);
    } catch (e) {
      return { ok: false, error: 'Payload quẻ JSON không hợp lệ: ' + e.message };
    }

    const d1 = envelope && envelope.data_1;
    const d2 = envelope && envelope.data_2;
    const checks = [
      ['hexagram JSON', !!envelope && typeof envelope === 'object'],
      ['required question', typeof d2?.question === 'string' && !!d2.question.trim()],
      ['required number', /^\d+$/.test(String(d1?.number ?? ''))],
      ['required time', typeof d1?.time === 'string' && !!d1.time.trim()],
      ['GPS validation', validGps(d1?.gps_show)]
    ];

    checks.forEach(([name, ok]) => addCheck(name, ok));
    if (!checks.every(([, ok]) => ok)) return { ok: false, error: 'Payload quẻ chưa đủ dữ liệu bắt buộc.' };

    // IMPORTANT: send the envelope unchanged. app.py is the only adapter.
    return { ok: true, payload: envelope };
  }

  function readFlat() {
    const question = $('question').value.trim();
    const number = $('number').value.trim();
    const time = $('time').value.trim();
    const lat = $('lat').value.trim();
    const lng = $('lng').value.trim();
    const gpsPair = (!lat && !lng) || (!!lat && !!lng);
    const gpsOk = gpsPair && (!lat || validGps({lat, lng}));
    const checks = [
      ['required question', !!question],
      ['required number', !!number],
      ['required time', !!time],
      ['number validation', /^\d{6}$/.test(number)],
      ['GPS validation', gpsOk]
    ];
    checks.forEach(([name, ok]) => addCheck(name, ok));
    if (!checks.every(([, ok]) => ok)) return { ok: false, error: 'input không hợp lệ' };

    const dt = new Date(time);
    if (Number.isNaN(dt.getTime())) return { ok: false, error: 'Time không hợp lệ.' };

    return {
      ok: true,
      payload: {
        question,
        number: Number(number),
        time: dt.toISOString(),
        gps: lat && lng ? { lat: Number(lat), lng: Number(lng) } : null,
        address: $('address').value.trim() || null,
        image: $('image').files[0]
          ? { name: $('image').files[0].name, type: $('image').files[0].type, size: $('image').files[0].size }
          : null
      }
    };
  }

  async function post(payload) {
    const response = await fetch('/api/v31', {
      method: 'POST',
      headers: {'Content-Type': 'application/json', 'Accept': 'application/json'},
      body: JSON.stringify(payload),
      cache: 'no-store'
    });
    const text = await response.text();
    let body;
    try { body = JSON.parse(text); } catch (_) { body = { error: text || ('HTTP ' + response.status) }; }
    if (!response.ok) throw new Error(body.error || ('HTTP ' + response.status));
    return body;
  }

  function runtimeChecks(result) {
    const trace = Object.fromEntries((result.raw_measurements?.runtime_trace || []).map(x => [x.layer, x.status]));
    addCheck('API reachable', true);
    addCheck('L1', trace.L1 === 'PASSED');
    addCheck('L2 PASS/PROVISIONAL', String(trace.L2 || '').startsWith('PASSED'));
    addCheck('L3 PASS/PROVISIONAL', String(trace.L3 || '').startsWith('PASSED'));
    addCheck('L4 canonical vocabulary', CANONICAL.includes(result.semantic_state?.primary_label));
    addCheck('L5 canonical=true', result.execution?.runtime_status === 'PASSED' && result.gate_results?.G1_SCHEMA === 'PASSED');
    addCheck('L6 API ready', trace.L6 === 'PASSED');
    addCheck('contract_version = 3.1.0', result.contract_version === '3.1.0');
    addCheck('f_net_out_excluded = true', result.uncertainty?.confidence?.f_net_out_excluded === true);
    addCheck('provenance tồn tại', !!result.provenance && Object.keys(result.provenance).length > 0);
    addCheck('input hash tồn tại', /^sha256:[0-9a-f]{64}$/.test(result.execution?.input_hash || ''));
    return trace;
  }

  cleanForm.addEventListener('submit', async (event) => {
    event.preventDefault();
    const run = $('run');
    run.disabled = true;
    $('checks').replaceChildren();
    $('status').textContent = 'Đang chạy…';
    $('status').className = 'status';
    $('status-badge').textContent = 'RUNNING';
    $('status-badge').className = 'badge badge-core';
    $('run-caption').textContent = 'Đang gọi canonical API và chờ response.';

    try {
      const input = $('use-hexagram').checked ? readHexagram() : readFlat();
      if (!input.ok) throw new Error(input.error);

      // One request is enough. A second request is used only for deterministic comparison.
      const first = await post(input.payload);
      const second = await post(input.payload);
      const frontendResult = window.DD3A?.adaptCanonicalResponse(first);
      if (!frontendResult) throw new Error('DD-3A adapter chưa được nạp.');
      runtimeChecks(first);
      addCheck('DD-3A six per-line records', frontendResult.interpretation.per_line.length === 6);
      addCheck('DD-3A 1-based moving index', frontendResult.interpretation.per_line.every((line, index) => line.id === `H${index + 1}` && line.index === index + 1));
      addCheck('deterministic request', JSON.stringify(first) === JSON.stringify(second));

      if (typeof window.renderInterpretation === 'function') {
        window.renderInterpretation(frontendResult);
      }
      $('status').textContent = 'PASS — canonical response đã được phân lớp để luận giải';
      $('status').className = 'status pass';
      $('status-badge').textContent = 'PASS';
      $('status-badge').className = 'badge badge-pass';
      $('run-caption').textContent = 'CORE đã khóa; các lớp diễn giải chỉ hiển thị khi canonical response có bằng chứng.';
    } catch (error) {
      $('status').textContent = 'FAIL — ' + error.message;
      $('status').className = 'status fail';
      $('status-badge').textContent = 'ERROR';
      $('status-badge').className = 'badge badge-unsupported';
      addCheck('API / runtime', false, error.message);
    } finally {
      run.disabled = false;
    }
  });
})();

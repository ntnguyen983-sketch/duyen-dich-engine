(() => {
  'use strict';

  // Runtime UI hotfix: form + per-line microscope from interpretation.per_line.
  // Does not touch CORE. Evidence fields remain UNSUPPORTED when absent.
  const form = document.getElementById('form');
  if (!form) return;

  const cleanForm = form.cloneNode(true);
  form.replaceWith(cleanForm);

  const $ = (id) => document.getElementById(id);
  const CANONICAL = ['SAT', 'TA', 'NHIEU', 'HY', 'DUONG', 'AN'];

  function escapeHtml(value) {
    return String(value ?? '—').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#039;'}[c]));
  }
  function display(value) {
    if (value === null || value === undefined || value === '') return '—';
    if (typeof value === 'object') return JSON.stringify(value);
    return String(value);
  }
  function unsupported(text = 'Chưa có trong canonical response') {
    return `<span class="unsupported">${escapeHtml(text)}</span>`;
  }
  function field(label, value, full = false) {
    return `<div class="field${full ? ' full' : ''}"><div class="data-label">${escapeHtml(label)}</div><div class="data-value">${value}</div></div>`;
  }

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
    return { ok: true, payload: envelope };
  }

  function readFlat() {
    const question = $('question').value.trim();
    const number = $('number').value.trim();
    const time = $('time').value.trim();
    const lat = $('lat').value.trim();
    const lng = $('lng').value.trim();
    const gpsPair = (!lat && !lng) || (!!lat && !!lng);
    const gpsOk = gpsPair && (!lat || validGps({ lat, lng }));
    const checks = [
      ['required question', !!question],
      ['required number', /^\d{6}$/.test(number)],
      ['required time', !!time],
      ['GPS validation', gpsOk]
    ];
    checks.forEach(([name, ok]) => addCheck(name, ok));
    if (!checks.every(([, ok]) => ok)) return { ok: false, error: 'Input phẳng chưa hợp lệ.' };
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
      headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
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

  function renderMicroscopePerLine(result) {
    const note = $('microscope-note');
    const linesEl = $('microscope-lines');
    if (!note || !linesEl) return;
    const perLine = Array.isArray(result?.interpretation?.per_line) ? result.interpretation.per_line : [];
    const byLine = Object.fromEntries(perLine.map(p => [p.line, p]));
    const hasPerLine = perLine.length > 0;
    note.innerHTML = hasPerLine
      ? `<span class="badge badge-micro">MICROSCOPE</span> Canonical response có <strong>interpretation.per_line</strong>. Hiển thị line / bit / moving / status từ CORE. Source, Interaction, Derived Event, Phase, Trigger, Expected Time Window và Ground Truth vẫn <strong>UNSUPPORTED</strong> vì chưa có evidence trong response.`
      : `<span class="badge badge-micro">MICROSCOPE</span> Per-line Source, Interaction, Derived Event, Phase, Trigger, Expected Time Window và Ground Truth không có trong canonical response hiện tại. Các ô dưới đây được khóa là <strong>UNSUPPORTED</strong>; UI không suy diễn.`;
    const lineNames = ['Hào 1', 'Hào 2', 'Hào 3', 'Hào 4', 'Hào 5', 'Hào 6'];
    linesEl.innerHTML = lineNames.map((name, index) => {
      const line = index + 1;
      const pl = byLine[line];
      const moving = !!(pl && pl.moving);
      const badge = moving
        ? '<span class="badge badge-micro">MOVING</span>'
        : (pl ? '<span class="badge badge-core">IDENTITY</span>' : '<span class="badge badge-unsupported">UNSUPPORTED</span>');
      const lineMeta = pl
        ? field('Line', escapeHtml(String(pl.line))) + field('Bit', escapeHtml(String(pl.bit))) + field('Moving', escapeHtml(String(!!pl.moving))) + field('Status', escapeHtml(display(pl.status)))
        : field('Line', escapeHtml(String(line))) + field('Bit', unsupported()) + field('Moving', unsupported()) + field('Status', unsupported());
      return `<article class="line-card" data-line="${line}" data-moving="${moving}"><div class="line-top"><div class="line-title">H${line} · ${name}</div>${badge}</div><div class="field-list">${lineMeta}${field('Source', unsupported())}${field('Source Evidence', unsupported())}${field('Interaction', unsupported())}${field('Interaction Evidence', unsupported())}${field('Derived Event', unsupported('Không suy diễn'))}${field('Phase', unsupported())}${field('Trigger', unsupported())}${field('Expected Time Window', unsupported())}${field('Observable Ground Truth', unsupported('Chưa ghi nhận'))}${field('Confidence / Unsupported', pl ? '<span class="badge badge-pass">CANONICAL per-line</span> · evidence fields still UNSUPPORTED' : '<span class="badge badge-unsupported">UNSUPPORTED · no per-line canonical field</span>', true)}</div></article>`;
    }).join('');
  }

  function renderAll(result) {
    if (typeof window.renderInterpretation === 'function') {
      window.renderInterpretation(result);
    }
    renderMicroscopePerLine(result);
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

      const first = await post(input.payload);
      const second = await post(input.payload);
      runtimeChecks(first);
      addCheck('deterministic request', JSON.stringify(first) === JSON.stringify(second));

      renderAll(first);
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

const D = __DATA__;
const hex = h => { h = h.replace('#',''); if (h.length===3) h=h.split('').map(c=>c+c).join('');
  const a = h.length===8 ? parseInt(h.slice(6,8),16)/255 : 1;
  return { r: parseInt(h.slice(0,2),16)/255, g: parseInt(h.slice(2,4),16)/255, b: parseInt(h.slice(4,6),16)/255, a }; };
const cols = await figma.variables.getLocalVariableCollectionsAsync();
const all = await figma.variables.getLocalVariablesAsync();
function coll(name, modes) {
  let c = cols.find(c => c.name === name);
  if (!c) c = figma.variables.createVariableCollection(name);
  c.renameMode(c.modes[0].modeId, modes[0]);
  for (let i = 1; i < modes.length; i++) if (!c.modes.find(m => m.name === modes[i])) c.addMode(modes[i]);
  return c;
}
function v(c, name, type) {
  return all.find(x => x.name === name && x.variableCollectionId === c.id) || figma.variables.createVariable(name, c, type);
}
const prim = coll('Primitives', ['Value']);
const pm = prim.modes[0].modeId, pmap = {};
for (const [name, css, val, use] of D.P) {
  const x = v(prim, name, 'COLOR'); x.setValueForMode(pm, hex(val)); x.scopes = [];
  x.setVariableCodeSyntax('WEB', `var(--${css})`); x.description = use; pmap[name] = x;
}
const theme = coll('Theme', D.modes);
const modeIds = D.modes.map(n => theme.modes.find(m => m.name === n).modeId);
const isText = n => /^(text|on|icon)\//.test(n) || /\/on-|^on-/.test(n);
const isBorder = n => /^border\//.test(n);
let roles = 0;
for (const [name, css, vals, use] of D.R) {
  const x = v(theme, name, 'COLOR');
  vals.forEach((val, i) => x.setValueForMode(modeIds[i], val[0] !== '#' ? { type: 'VARIABLE_ALIAS', id: pmap[val].id } : hex(val)));
  x.scopes = isText(name) ? ['TEXT_FILL', 'SHAPE_FILL'] : isBorder(name) ? ['STROKE_COLOR'] : ['FRAME_FILL', 'SHAPE_FILL', 'STROKE_COLOR'];
  x.setVariableCodeSyntax('WEB', `var(--${css})`); x.description = use; roles++;
}
const dim = coll('Dimensions', ['Value']);
const dm = dim.modes[0].modeId;
for (const [name, css, val, scopes, use] of D.N) {
  const x = v(dim, name, 'FLOAT'); x.setValueForMode(dm, val); x.scopes = scopes;
  x.setVariableCodeSyntax('WEB', `var(--${css})`); x.description = use;
}
return { collections: { Primitives: prim.id, Theme: theme.id, Dimensions: dim.id },
  themeModes: theme.modes.map(m => m.name), counts: { prim: D.P.length, roles, dims: D.N.length } };

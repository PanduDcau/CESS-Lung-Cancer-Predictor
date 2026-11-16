document.addEventListener('DOMContentLoaded', function () {
    const selectElems = document.querySelectorAll('select');
    M.FormSelect.init(selectElems);

    const collapsibleElems = document.querySelectorAll('.collapsible.expandable');
    M.Collapsible.init(collapsibleElems, { accordion: false });
});

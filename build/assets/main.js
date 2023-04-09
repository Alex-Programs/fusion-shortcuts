window.onload = function () {
    fetch("hotkeys.json", {
        method: "GET"
    }).then(res => res.json())
        .then(categories => {
            window.categories = categories;
            renderCategories(document.getElementById("js_fill_in"), document.getElementById("search").value)
        })
}

function renderCategories(element, search) {
    element.innerHTML = "";
    console.log(search)

    let success = false;

    categories.forEach(category => {
        let hotkeys;

        if (search.length > 0) {
            hotkeys = category.hotkeys.filter(hotkey => {
                const keySimilarity = stringSimilarity.compareTwoStrings(hotkey.key.raw.toLowerCase(), search.toLowerCase())
                const nameSimilarity = stringSimilarity.compareTwoStrings(hotkey.name.toLowerCase(), search.toLowerCase())
                const includesName = hotkey.name.toLowerCase().includes(search.toLowerCase())
                const includesKey = hotkey.key.raw.toLowerCase().includes(search.toLowerCase())

                return keySimilarity > 0.3 || nameSimilarity > 0.3 || includesName || includesKey
            })
        } else {
            hotkeys = category.hotkeys
        }

        if (hotkeys.length === 0) {
            return;
        }

        let categoryElement = document.createElement("div");
        categoryElement.classList.add("category");
        categoryElement.innerHTML = `
            <div class="category_name">${category.name}</div>
        `;

        hotkeys.forEach(hotkey => {
            let hotkeyElement = document.createElement("div");
            hotkeyElement.classList.add("hotkey");

            hotkeyElement.innerHTML = `
                <span class="hotkey_name">${hotkey.name}</span>
                <span class="hotkey_key">${build_fancy_hotkey(hotkey.key)}</span>
            `;
            categoryElement.appendChild(hotkeyElement);
        });

        element.appendChild(categoryElement);

        success = true;
    })

    document.getElementById("no-data").hidden = success;
}

function build_fancy_hotkey(key) {
    return key.combination.map(key => {
        return `<kbd>${key}</kbd>`
    }).join("+");
}
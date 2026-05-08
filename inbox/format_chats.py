import os
import glob

# Use the parent directory (messages/) as the base directory
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

search_pattern = os.path.join(base_dir, "**", "message_*.html")
html_files = glob.glob(search_pattern, recursive=True)

injection = r"""
<!-- INJECTED_CHAT_UI -->
<style>
/* Search Bar */
#searchContainer {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    background: #fff;
    padding: 10px;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    z-index: 1000;
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    align-items: center;
    gap: 8px;
    box-sizing: border-box;
}
#searchContainer input {
    padding: 8px 12px;
    border: 1px solid #ccc;
    border-radius: 20px;
    font-size: 14px;
    flex: 1 1 auto;
    min-width: 120px;
}
#searchInput {
    max-width: 200px;
}
#searchDate {
    max-width: 150px;
}
.search-btn-group {
    display: flex;
    gap: 8px;
    align-items: center;
}
.search-btn-group button {
    padding: 8px 15px;
    border: none;
    border-radius: 20px;
    cursor: pointer;
    font-size: 14px;
}
#searchBtn {
    background: #4267b2;
    color: white;
}
#searchClearBtn {
    background: #e4e6eb;
    color: black;
}
.nav-btn {
    background: #e4e6eb;
    color: black;
    padding: 8px 12px !important;
}
.nav-btn:disabled {
    opacity: 0.5;
    cursor: not-allowed;
}
#searchStatus {
    font-size: 13px;
    font-weight: bold;
    color: #4267b2;
    width: 100%;
    text-align: center;
    margin-top: 4px;
}
body {
    padding-top: 100px !important; /* space for search bar on mobile */
    margin: 0;
}
@media (min-width: 600px) {
    body { padding-top: 70px !important; }
    #searchStatus { width: auto; text-align: left; margin-top: 0; min-width: 80px; }
}

/* Container for all messages */
main[role="main"] {
    display: flex;
    flex-direction: column;
    padding: 15px 10px;
    background-color: #ece5dd;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    min-height: 100vh;
    box-sizing: border-box;
}
/* Remove annoying background from parent */
._a705 { max-width: 100% !important; margin: 0 !important; }
._as_0 { display: none !important; } /* Hide top bar if overlapping */

/* Common bubble styles */
.pam._3-95._2ph-._a6-g.uiBoxWhite.noborder {
    max-width: 85%; /* Better for mobile */
    width: fit-content;
    border-radius: 18px;
    margin-bottom: 12px !important;
    padding: 10px 14px !important;
    box-shadow: 0 1px 1.5px rgba(0,0,0,0.1) !important;
    border: none !important;
    word-wrap: break-word;
    transition: box-shadow 0.3s, background-color 0.3s;
}

/* Match highlight styles */
.highlight-match {
    box-shadow: 0 0 0 3px #ffeb3b !important;
}
.active-match {
    box-shadow: 0 0 0 4px #ff9800 !important;
    background-color: #fffde7 !important;
}

.text-highlight {
    background-color: #ffeb3b;
    color: #000;
    font-weight: bold;
    border-radius: 3px;
    padding: 0 2px;
}
.active-match .text-highlight {
    background-color: #ff9800;
    color: #fff;
}

/* Me (Right) */
.msg-me {
    align-self: flex-end;
    background-color: #dcf8c6 !important;
    border-bottom-right-radius: 4px !important;
}
.msg-me h2 {
    display: none !important; 
}
.msg-me ._a6-o {
    text-align: right;
    font-size: 11px;
    color: #777;
    margin-top: 4px;
}

/* Them (Left) */
.msg-them {
    align-self: flex-start;
    background-color: #ffffff !important;
    border-bottom-left-radius: 4px !important;
}
.msg-them h2 {
    font-size: 12px !important;
    color: #355899 !important;
    margin-bottom: 4px !important;
    border-bottom: none !important;
    padding-bottom: 0 !important;
}
.msg-them ._a6-o {
    text-align: left;
    font-size: 11px;
    color: #999;
    margin-top: 4px;
}

/* Fix images and videos inside bubbles */
._a6_o {
    max-width: 100%;
    height: auto;
    border-radius: 10px;
}
audio, video {
    max-width: 100%;
}
._a6-p {
    font-size: 15px;
    line-height: 1.4;
}

/* Scroll to top button */
#scrollTopBtn {
    display: none; 
    position: fixed; 
    bottom: 20px; 
    right: 20px; 
    z-index: 99; 
    font-size: 20px; 
    border: none; 
    outline: none; 
    background-color: #25d366; 
    color: white; 
    cursor: pointer; 
    width: 50px;
    height: 50px;
    border-radius: 50%; 
    box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    transition: 0.3s;
    text-align: center;
    line-height: 50px;
    padding: 0;
}
#scrollTopBtn:hover {
    background-color: #128c7e; 
}
</style>
<script>
// Force mobile viewport
if (!document.querySelector('meta[name="viewport"]')) {
    const meta = document.createElement('meta');
    meta.name = "viewport";
    meta.content = "width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no";
    document.head.appendChild(meta);
}

const ownerNames = ["actiliz", "安璃"]; // Username และ Display name ของเจ้าของแอคเคาท์

// 1. Reverse the messages so oldest is top, newest is bottom
const mainContainer = document.querySelector('main[role="main"]');
if (mainContainer) {
    const messages = Array.from(mainContainer.querySelectorAll('.uiBoxWhite'));
    messages.reverse().forEach(msg => mainContainer.appendChild(msg));
}

// 2. Setup left/right bubbles
document.querySelectorAll('.uiBoxWhite').forEach(box => {
    const h2 = box.querySelector('h2');
    if (h2) {
        if (ownerNames.includes(h2.textContent.trim())) {
            box.classList.add('msg-me');
        } else {
            box.classList.add('msg-them');
        }
    }
});

// 3. Scroll to top button
const btn = document.createElement('button');
btn.id = "scrollTopBtn";
btn.innerHTML = "⬆";
btn.title = "ขึ้นหาบนสุด";
btn.onclick = () => window.scrollTo({top: 0, behavior: 'smooth'});
document.body.appendChild(btn);

window.onscroll = () => {
    if (document.body.scrollTop > 300 || document.documentElement.scrollTop > 300) {
        btn.style.display = "block";
    } else {
        btn.style.display = "none";
    }
};

// 4. Enhanced Search Functionality
const searchContainer = document.createElement('div');
searchContainer.id = "searchContainer";

const searchInput = document.createElement('input');
searchInput.id = "searchInput";
searchInput.type = "text";
searchInput.placeholder = "ค้นหาข้อความ...";

const searchDate = document.createElement('input');
searchDate.id = "searchDate";
searchDate.type = "date";

const btnGroup = document.createElement('div');
btnGroup.className = "search-btn-group";

const searchBtn = document.createElement('button');
searchBtn.id = "searchBtn";
searchBtn.textContent = "ค้นหา";

const prevBtn = document.createElement('button');
prevBtn.id = "searchPrevBtn";
prevBtn.className = "nav-btn";
prevBtn.innerHTML = "▲";
prevBtn.disabled = true;

const nextBtn = document.createElement('button');
nextBtn.id = "searchNextBtn";
nextBtn.className = "nav-btn";
nextBtn.innerHTML = "▼";
nextBtn.disabled = true;

const clearBtn = document.createElement('button');
clearBtn.id = "searchClearBtn";
clearBtn.textContent = "ล้าง";

btnGroup.appendChild(searchBtn);
btnGroup.appendChild(prevBtn);
btnGroup.appendChild(nextBtn);
btnGroup.appendChild(clearBtn);

const searchStatus = document.createElement('div');
searchStatus.id = "searchStatus";

searchContainer.appendChild(searchInput);
searchContainer.appendChild(searchDate);
searchContainer.appendChild(btnGroup);
searchContainer.appendChild(searchStatus);
document.body.prepend(searchContainer);

const thaiMonths = ['ม.ค.', 'ก.พ.', 'มี.ค.', 'เม.ย.', 'พ.ค.', 'มิ.ย.', 'ก.ค.', 'ส.ค.', 'ก.ย.', 'ต.ค.', 'พ.ย.', 'ธ.ค.'];
const engMonths = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];

function formatDateQuery(dateString) {
    if (!dateString) return null;
    const d = new Date(dateString);
    const day = d.getDate();
    const year = d.getFullYear();
    const monthIndex = d.getMonth();
    
    const th1 = `${thaiMonths[monthIndex]} ${day}, ${year}`;
    const th2 = `${day} ${thaiMonths[monthIndex]} ${year}`;
    const en1 = `${engMonths[monthIndex]} ${day}, ${year}`;
    
    return [th1.toLowerCase(), th2.toLowerCase(), en1.toLowerCase()];
}

let matchedMessages = [];
let currentMatchIndex = -1;

function updateNavButtons() {
    prevBtn.disabled = currentMatchIndex <= 0;
    nextBtn.disabled = currentMatchIndex === -1 || currentMatchIndex >= matchedMessages.length - 1;
}

function scrollToMatch(index) {
    matchedMessages.forEach(msg => msg.classList.remove('active-match'));
    const target = matchedMessages[index];
    if (target) {
        target.classList.add('active-match');
        const y = target.getBoundingClientRect().top + window.scrollY - 150;
        window.scrollTo({ top: y, behavior: 'smooth' });
        searchStatus.textContent = `${index + 1} / ${matchedMessages.length}`;
    }
}

function clearAllHighlights() {
    document.querySelectorAll('.text-highlight').forEach(h => {
        if (h.parentNode) {
            h.parentNode.replaceChild(document.createTextNode(h.textContent), h);
        }
    });
    // Normalize body to merge text nodes
    document.body.normalize();
}

function highlightText(element, term) {
    if (!term) return;
    const escapedTerm = term.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
    const termRegex = new RegExp(`(${escapedTerm})`, 'gi');
    
    const walker = document.createTreeWalker(element, NodeFilter.SHOW_TEXT, null, false);
    const nodesToReplace = [];
    let node;
    while(node = walker.nextNode()) {
        if (node.nodeValue.toLowerCase().includes(term)) {
            nodesToReplace.push(node);
        }
    }
    
    nodesToReplace.forEach(node => {
        const frag = document.createDocumentFragment();
        const parts = node.nodeValue.split(termRegex);
        parts.forEach(part => {
            if (part.toLowerCase() === term) {
                const span = document.createElement('span');
                span.className = 'text-highlight';
                span.textContent = part;
                frag.appendChild(span);
            } else if (part.length > 0) {
                frag.appendChild(document.createTextNode(part));
            }
        });
        if (node.parentNode) {
            node.parentNode.replaceChild(frag, node);
        }
    });
}

function doSearch() {
    matchedMessages.forEach(msg => msg.classList.remove('highlight-match', 'active-match'));
    clearAllHighlights();
    matchedMessages = [];
    currentMatchIndex = -1;

    const term = searchInput.value.toLowerCase().trim();
    const dateQueryArr = formatDateQuery(searchDate.value);
    
    if (term === "" && !dateQueryArr) {
        searchStatus.textContent = "";
        updateNavButtons();
        return;
    }
    
    const messages = document.querySelectorAll('.uiBoxWhite');
    messages.forEach(msg => {
        let textMatch = true;
        let dateMatch = true;
        let targetTextElement = msg.querySelector('._a6-p') || msg;
        
        if (term !== "") {
            const textContent = targetTextElement.textContent.toLowerCase();
            textMatch = textContent.includes(term);
        }
        
        if (dateQueryArr) {
            const dateElement = msg.querySelector('._a6-o');
            const dateContent = dateElement ? dateElement.textContent.toLowerCase() : "";
            dateMatch = dateQueryArr.some(q => dateContent.includes(q));
        }
        
        if (textMatch && dateMatch) {
            msg.classList.add('highlight-match');
            if (term !== "") {
                highlightText(targetTextElement, term);
            }
            matchedMessages.push(msg);
        }
    });
    
    if (matchedMessages.length > 0) {
        currentMatchIndex = 0;
        scrollToMatch(currentMatchIndex);
    } else {
        searchStatus.textContent = "ไม่พบ";
    }
    updateNavButtons();
}

searchBtn.onclick = doSearch;
searchInput.addEventListener('keypress', function (e) {
    if (e.key === 'Enter') doSearch();
});
searchDate.addEventListener('change', doSearch);

prevBtn.onclick = () => {
    if (currentMatchIndex > 0) {
        currentMatchIndex--;
        scrollToMatch(currentMatchIndex);
        updateNavButtons();
    }
};

nextBtn.onclick = () => {
    if (currentMatchIndex < matchedMessages.length - 1) {
        currentMatchIndex++;
        scrollToMatch(currentMatchIndex);
        updateNavButtons();
    }
};

clearBtn.onclick = () => {
    searchInput.value = '';
    searchDate.value = '';
    doSearch();
};
</script>
</body></html>
"""

count = 0
for html_path in html_files:
    try:
        with open(html_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Remove previous injected script if any
        if '<!-- INJECTED_CHAT_UI -->' in content:
            content = content.split('<!-- INJECTED_CHAT_UI -->')[0] + '</body></html>'

        # Fix base href and image paths for GitHub Pages (without actiliz/messages in path)
        content = content.replace('href="../../../../"', 'href="../../"')
        content = content.replace('href="../../../"', 'href="../../"')
        content = content.replace('"your_instagram_activity/messages/inbox/', '"inbox/')
        content = content.replace('"your_instagram_activity/messages/message_requests/', '"message_requests/')
        content = content.replace('"../../your_instagram_activity/messages/inbox/', '"inbox/')
        content = content.replace('"../../your_instagram_activity/messages/message_requests/', '"message_requests/')
        content = content.replace('"messages/inbox/', '"inbox/')
        content = content.replace('"messages/message_requests/', '"message_requests/')

        if '</body></html>' in content:
            content = content.replace('</body></html>', injection)
            
            with open(html_path, 'w', encoding='utf-8') as f:
                f.write(content)
            count += 1
    except Exception as e:
        print(f"Failed to process {html_path}: {e}")

print(f"Successfully formatted {count} files.")

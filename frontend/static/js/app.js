const chatBox = document.getElementById('chat-box');
const userInput = document.getElementById('user-input');
const sendBtn = document.getElementById('send-btn');

function appendMessage(role, text) {
    const msg = document.createElement('div');
    msg.className = role;
    msg.innerText = (role === 'user' ? '我: ' : 'Agent: ') + text;
    chatBox.appendChild(msg);
    chatBox.scrollTop = chatBox.scrollHeight;
}

sendBtn.onclick = async function() {
    const text = userInput.value.trim();
    if (!text) return;
    appendMessage('user', text);
    userInput.value = '';
    appendMessage('agent', '思考中...');
    const res = await fetch('/api/query', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({text})
    });
    const data = await res.json();
    chatBox.lastChild.innerText = 'Agent: ' + data.reply;
};

userInput.addEventListener('keydown', function(e) {
    if (e.key === 'Enter') sendBtn.onclick();
});

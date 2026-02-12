async function handleGenerate(mode) {
    const level = document.getElementById('levelSelect').value;
    const topic = document.getElementById('topicSelect').value;
    const outputBox = document.getElementById('outputBox');

    // Reset UI and show loading state
    outputBox.innerHTML = '<p class="loader" style="color: #10b981;">Generating AI content...</p>';

    try {
        const response = await fetch('http://127.0.0.1:5000/api/generate', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ topic, level, mode })
        });

        if (!response.ok) {
            // If the server fails, try to get the error message from JSON
            const errorData = await response.json();
            throw new Error(errorData.error || 'Server error occurred');
        }

        const contentType = response.headers.get('content-type');

        // Check if the response is actually a binary file (Audio)
        if (contentType && contentType.includes('audio')) {
            const blob = await response.blob();
            const url = URL.createObjectURL(blob);
            outputBox.innerHTML = `
                <h3>Audio Lesson Ready</h3>
                <audio controls src="${url}" style="width: 100%; margin-top: 10px;"></audio>
                <p style="font-size: 0.8rem; margin-top: 5px;">Topic: ${topic} (${level})</p>
            `;
        } 
        // Otherwise, treat it as structured data (Explanation/Code/Visual)
        else {
            const data = await response.json();
            outputBox.innerText = data.output || 'No output received';
        }

    } catch (error) {
        console.error("Fetch Error:", error);
        outputBox.innerHTML = `<p style="color: #ef4444;">⚠️ ${error.message}</p>`;
    }
}
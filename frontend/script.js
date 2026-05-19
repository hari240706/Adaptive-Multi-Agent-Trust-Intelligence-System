async function analyzeNews() {

    const text = document.getElementById(
        "newsText"
    ).value;

    const resultDiv = document.getElementById(
        "result"
    );

    if (!text) {

        resultDiv.innerHTML =
            "Please enter some text.";

        return;
    }

    try {

        const response = await fetch(
            "http://127.0.0.1:8000/predict",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    text: text
                })
            }
        );

        const data = await response.json();

        resultDiv.innerHTML = `
            Prediction: ${data.prediction}
            <br>
            Confidence: ${data.confidence}
        `;

    } catch (error) {

        resultDiv.innerHTML =
            "Error connecting to API.";
    }
}
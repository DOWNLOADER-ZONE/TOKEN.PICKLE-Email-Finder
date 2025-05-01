<p align="center">
  <img width="220" src="https://i.rj1.dev/VmzBUoH" alt="Downloader Zone Logo">
</p>

<body>
    <h1>Token.Pickle Email Finder</h1>
    <p>This is a lightweight Python script that extracts the authenticated Google account's email address from an existing <code>token.pickle</code> file — <strong>without triggering OAuth reauthentication</strong>.</p>
    <p>Useful for quickly identifying which Google account a token belongs to.</p>
    <hr>
    <h2>💡 Features</h2>
    <ul>
        <li>✅ No re-authentication or <code>credentials.json</code> required</li>
        <li>✅ Extracts email from <code>token.pickle</code></li>
        <li>✅ Supports Drive API scopes</li>
        <li>✅ Simple, lightweight, and CLI-friendly</li>
    </ul>
    <hr>
    <h2>🛠 Requirements</h2>
    <ul>
        <li>Python 3.6+</li>
        <li>Install the required package:</li>
    </ul>
    <pre><code>pip install -r requirements.txt</code></pre>
    <h2>📁 Project Structure</h2>
    <pre><code>TOKEN.PICKLE-Email-Finder/
├── get_email.py        # Main script
├── token.pickle        # Your existing token.pickle
└── requirements.txt    # This file contains all the requirements to be installed       
└── README.md           # About
</code></pre>
    <h2>🚀 Usage</h2>
    <p>Clone this repository:</p>
    <pre><code>git clone https://github.com/DOWNLOADER-ZONE/TOKEN.PICKLE-Email-Finder.git</pre></code>
<pre><code>cd TOKEN.PICKLE-Email-Finder</pre></code>
  <pre><code>pip install -r requirements.txt</code></pre>
<p>Place your token.pickle file inside the project folder.</p>
    <p>Run the script:</p>
    <pre><code>python get_email.py</code></pre>
    <h2>🧠 How It Works</h2>
    <p>The script loads your existing <code>token.pickle</code> and tries the following:</p>
    <ul>
        <li>🔹 Drive API (fallback): Uses <code>about().get()</code> to fetch the user's email</li>
    </ul>
    <p>The script will output the email address or an error if the token lacks the required scopes.</p>
    <h2>✅ Example Output</h2>
    <p>Email address: johndoe@gmail.com</p>
    <h2>❗ Common Errors</h2>
    <p>403: Insufficient Permissions</p>
    <p>HttpError 403: Request had insufficient authentication scopes.</p>
    <p>Your <code>token.pickle</code> doesn’t include Drive scopes. You’ll need to regenerate it with proper scopes (like <code>drive.metadata.readonly</code>) to access the email.</p>
    <h2>📃 License</h2>
    <p>This project is licensed under the MIT License. See the LICENSE file for details.</p>
</body>
</html>

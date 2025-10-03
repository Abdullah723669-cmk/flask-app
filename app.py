from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
     return """
    <!DOCTYPE html>
     <html lang="en">
     <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>My Profile</title>
       <style>
         body {
           font-family: Arial, sans-serif;
           margin: 0;
           background: #f4f4f9;
           color: #333;
         }
         header {
           background: #4CAF50;
           color: white;
           text-align: center;
           padding: 2rem 1rem;
         }
         header img {
           width: 120px;
           height: 120px;
           border-radius: 50%;
           border: 4px solid white;
         }
         header h1 {
           margin: 1rem 0 0.5rem;
         }
         header p {
           margin: 0;
           font-size: 1.1rem;
         }
         main {
           padding: 2rem;
           max-width: 800px;
           margin: auto;
         }
         section {
           margin-bottom: 2rem;
         }
         h2 {
           color: #4CAF50;
           border-bottom: 2px solid #4CAF50;
           padding-bottom: 0.3rem;
         }
         footer {
           text-align: center;
           background: #333;
           color: white;
           padding: 1rem;
           margin-top: 2rem;
         }
         a {
           color: #4CAF50;
           text-decoration: none;
         }
         a:hover {
           text-decoration: underline;
         }
       </style>
     </head>
     <body>
     
       <header>
         <img src="https://via.placeholder.com/120" alt="Profile Picture">
         <h1>Md. Abdullah Al Mamun</h1>
         <p>DevOps Enthusiast | Distribution Manager | Lifelong Learner</p>
       </header>
     
       <main>
         <section>
           <h2>About Me</h2>
           <p>
             I am passionate about technology, cloud, and DevOps practices. 
             With 9 years of experience in distribution management and a background in science, 
             I am now focused on mastering tools like Docker, Kubernetes, Jenkins, and Ansible to grow as a DevOps engineer.
           </p>
         </section>
     
         <section>
           <h2>Skills</h2>
           <ul>
             <li>Docker, Kubernetes, Ansible</li>
             <li>Jenkins, GitHub Actions</li>
             <li>AWS EC2, Linux, Ubuntu</li>
             <li>Spring Boot, ASP.NET Core, Node.js</li>
           </ul>
         </section>
     
         <section>
           <h2>Contact</h2>
           <p>Email: <a href="mailto:yourname@email.com">yourname@email.com</a></p>
           <p>GitHub: <a href="https://github.com/yourusername" target="_blank">github.com/yourusername</a></p>
           <p>LinkedIn: <a href="https://linkedin.com/in/yourusername" target="_blank">linkedin.com/in/yourusername</a></p>
         </section>
       </main>
     
       <footer>
         <p>&copy; 2025 Md. Abdullah Al Mamun. All rights reserved.</p>
       </footer>
     
     </body>
     </html>

    """
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5050)


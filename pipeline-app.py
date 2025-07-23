pipeline { // 📦 Starts the Jenkins pipeline block – the foundation of our CI/CD story.
    agent any // 🤖 Tells Jenkins to run this pipeline on any available agent (worker).

    // for time/scheduling using cron job
     triggers {
    cron('0 20 * * *') // ⏰ Runs the job every day at 8:00 PM server time
}
    '''
    Explanation of cron('0 20 * * *'):
 ┌───────────── minute (0)
 │ ┌───────────── hour (20 → 8 PM)
 │ │ ┌───────────── day of month (* = every day)
 │ │ │ ┌───────────── month (* = every month)
 │ │ │ │ ┌───────────── day of week (* = every day of week)
 │ │ │ │ │
 │ │ │ │ │
 0  20  *  *  * 
    '''


    stages { // 🎬 Begins the list of stages – each stage is like a chapter in our automation journey.

        stage('Checkout Code') { // 📥 This stage is about bringing in the source code from GitHub.
            steps { // 🚶 Defines the exact steps Jenkins should follow in this stage.
                git branch: 'main', url: 'https://github.com/iaman011/Jenkins.git' // 🌐 Pulls the code from the 'main' branch of your GitHub repo.
            }
        }

        stage('Run Python Script') { // 🐍 This stage focuses on executing our Python application.
            steps { // 🛠️ The actual actions to be performed in this stage.
                sh 'python app.py' // 🚀 Runs the Python script using the system shell. This is where your app comes to life!
                // Or use 'python3 app.py' if needed – 🧠 A friendly tip in case your system uses Python 3 as the main interpreter.
            }
        }

    } // ✅ Ends the stages block – all major tasks have been defined.

} // 🏁 Ends the pipeline – our Jenkins story is complete and ready to be run.

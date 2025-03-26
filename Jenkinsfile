pipeline{
    agent any
    stages{
        stage("Cloning into git repository"){
            steps{
                echo "Cloning"
                git credentialsId :"PATreposingit" , url : "https://github.com/Gagan866/OnlineCourseEnrollmentPlatform.git" , branch : "main"

            }
        }
        stage("Installing dependencies "){
            steps{
                echo "Installation in process"
                bat '''
                    python -m venv venv 
                    call venv\\Scripts\\activate
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                    '''
            }
        }
        stage("Testing code"){
            steps{
                echo "Tests running"
                bat '''
                    call venv\\Scripts\\activate
                    pytest test.py --maxfail=1 --disable-warnings
                    '''
            }
        }
        stage("Deployment"){
            steps{
                echo "Deploying code"
                bat ''' 
                    cal venv\\Scripts\\activate
                    python course_enroll.py
                    '''
            }

        }
    }
    post{
        success{
            echo "Successful"
        }
        failure{
            echo "Failed"
        }
    }
}
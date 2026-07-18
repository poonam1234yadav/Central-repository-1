pipeline {
    agent any
    stages {
        
     stage("github clone"){
         steps{
             git branch: 'main',
             url: 'https://github.com/poonam1234yadav/Central-repository-1.git'
         }
     }   
     
      stage('check python'){
         steps{
             sh'''
             sudo apt install python3.14-venv -y
             '''    
         }
     } 
     
           stage('Setup Virtual Environment') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                '''
            }
}

     
     stage('run python script'){
         steps{
             sh'''
             . venv/bin/activate
             python mypython-code.py
             '''
         }
     }
        
    }
}

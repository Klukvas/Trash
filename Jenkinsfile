node{
    docker.image('3.9.13-buster').inside{
        stage('Init'){
            sh 'pip3 install pipenv'
            sh 'pipenv install --system'
        }
        stage('Run tests of getting all users'){
            sh'pipenv run pytest -s -vv -m all_users'
        }
        stage('Run tests of getting one user by id'){
            sh'pipenv run pytest -s -vv -m one_user'
        }
        stage('Run tests of getting user`s posts'){
            sh'pipenv run pytest -s -vv -m user_posts'
        }
    }
    
}
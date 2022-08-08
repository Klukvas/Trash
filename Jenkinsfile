def getImageName(){
    def name = 'jenkinsTraining-${env.BUILD_NUMBER}' 
    return name
}
node{
    def app
    stage('Build'){
        app = docker.build(getImageName())
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
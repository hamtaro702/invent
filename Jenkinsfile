def remote = [:]
remote.name = "kub3"
remote.host = "192.168.61.53"
remote.allowAnyHosts = true

node {
    withCredentials([usernamePassword(credentialsId: 'kub3', passwordVariable: 'password', usernameVariable: 'userName')]) {
        remote.user = userName
        remote.password = password

        stage("Build Image Docker"){
            
            checkout scm    
            docker.withRegistry('https://registry.hub.docker.com', 'dockerhub') {

            def customImage = docker.build("0809031817/invent_web")

            /* Push the container to the custom Registry */
             customImage.push()  
            }

        }

        stage("SSH Steps Rocks!") {
           writeFile file: 'test.sh', text: 'ls'
            sshCommand remote: remote, command:  '''if docker ps -a | grep invent-Jenkins
                                                    then
                                                    docker rm -f invent-Jenkins
                                                    docker run -d --name invent-Jenkins --restart=always -p 8001:8000 0809031817/invent_web
                                                    else
                                                    docker run -d --name invent-Jenkins --restart=always -p 8001:8000 0809031817/invent_web
                                                    fi'''
            sshCommand remote: remote, command: 'docker ps'

            //sshScript remote: remote, script: 'test.sh'
           sshPut remote: remote, from: 'test.sh', into: '/home/tanabat/'
           // sshGet remote: remote, from: 'test.sh', into: 'test_new.sh', override: true
           // sshRemove remote: remote, path: 'test.sh'
        }
        stage("TEST Web") {
            sh '''response=$(curl -s -o /dev/null -w "%{http_code}\n" http://192.168.61.53:8001/)
                    if [ "$response" != "200" ]
                    then
                     exit 1
                    fi'''
            
        }
    }
}

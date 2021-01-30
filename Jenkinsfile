node {

    checkout scm

    docker.withRegistry('https://registry.hub.docker.com', 'dockerhub') {

        def customImage = docker.build("0809031817/invent_web")

        /* Push the container to the custom Registry */
        customImage.push()
        //docker.image('0809031817/invent_web').withRun('-p 8001:8000')

    }
}





}
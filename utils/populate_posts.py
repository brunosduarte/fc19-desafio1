from core.models import Post, Tag


data = [
    {
        "title": "Introdução ao React e Seus Principais Conceitos",
        "content": "Neste post, vamos explorar os fundamentos do React, uma biblioteca JavaScript popular para a construção de interfaces de usuário. Abordaremos conceitos como componentes, props, state e o ciclo de vida dos componentes. Ao final, você terá uma compreensão sólida para começar a construir suas próprias aplicações.",
        "created_at": "2024-10-25T00:00:00",
        "tags": [
            {"name": "React"},
            {"name": "JavaScript"},
            {"name": "Frontend"}
        ]
    },
    {
        "title": "Entendendo a Programação Assíncrona em JavaScript",
        "content": "A programação assíncrona é um conceito fundamental em JavaScript que permite que seu código execute operações sem bloquear a execução. Neste artigo, vamos discutir callbacks, Promises e async/await, além de exemplos práticos para ajudar você a entender como implementá-los.",
        "created_at": "2024-10-26T00:00:00",
        "tags": [
            {"name": "JavaScript"},
            {"name": "Assíncrono"},
            {"name": "Programação"}
        ]
    },
    {
        "title": "Como Utilizar o Docker para Ambientes de Desenvolvimento",
        "content": "O Docker é uma ferramenta poderosa que facilita a criação, distribuição e execução de aplicações em contêineres. Neste post, vamos ensinar como configurar um ambiente de desenvolvimento usando Docker, abordando a criação de Dockerfiles e o uso de docker-compose.",
        "created_at": "2024-10-27T00:00:00",
        "tags": [
            {"name": "Docker"},
            {"name": "DevOps"},
            {"name": "Desenvolvimento"}
        ]
    },
    {
        "title": "A Importância da Testagem de Software",
        "content": "Neste artigo, discutiremos a importância da testagem de software no ciclo de vida do desenvolvimento. Abordaremos diferentes tipos de testes, como testes unitários, de integração e de aceitação, e como implementá-los em suas aplicações para garantir a qualidade do software.",
        "created_at": "2024-10-28T00:00:00",
        "tags": [
            {"name": "Testes"},
            {"name": "Qualidade de Software"},
            {"name": "Desenvolvimento"}
        ]
    },
    {
        "title": "Explorando o Futuro do Desenvolvimento Web com WebAssembly",
        "content": "WebAssembly é uma tecnologia que permite que aplicações web sejam executadas com desempenho quase nativo. Neste post, vamos explorar o que é WebAssembly, como ele funciona e como você pode usá-lo para melhorar o desempenho de suas aplicações web.",
        "created_at": "2024-10-29T00:00:00",
        "tags": [
            {"name": "WebAssembly"},
            {"name": "Web"},
            {"name": "Tecnologia"}
        ]
    },
    {
        "title": "Estruturas de Dados Essenciais para Programadores",
        "content": "Compreender estruturas de dados é crucial para qualquer programador. Neste artigo, discutiremos as estruturas de dados mais comuns, como listas, pilhas, filas e árvores, e suas aplicações práticas na resolução de problemas de programação.",
        "created_at": "2024-10-30T00:00:00",
        "tags": [
            {"name": "Estruturas de Dados"},
            {"name": "Algoritmos"},
            {"name": "Programação"}
        ]
    }
]


def populate():
    for post_data in data:

        tags_data = post_data.pop('tags')
        post = Post.objects.create(**post_data)

        tags_instances = []
        
        for tag_data in tags_data:
            name = tag_data['name']

            tag, created = Tag.objects.get_or_create(name=name)

            tags_instances.append(tag)

        post.tags.set(tags_instances)


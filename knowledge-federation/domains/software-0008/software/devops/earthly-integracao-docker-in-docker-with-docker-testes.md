---
id: software.devops.tranche08.000798
tipo: tecnica
dominio: software
subdominio: devops
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-08.md"
fontes: ["https://raw.githubusercontent.com/earthly/earthly/main/README.md", "https://docs.earthly.dev/docs/earthfile", "https://github.com/earthly/earthly"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Earthly: testes de integração com containers e Docker Compose dentro do build usando WITH DOCKER

## Em uma frase
O bloco `WITH DOCKER ... END` no `Earthfile` inicializa um daemon Docker isolado dentro do passo de build (pré-carregando imagens de outros targets via `--load` ou subindo uma pilha `docker-compose` via `--compose`) para executar testes de integração end-to-end.

## Por que importa
Como cada passo `RUN` do Earthly já roda dentro de um container BuildKit isolado, tentar rodar `docker run` ou `docker compose up` diretamente em um `RUN` comum para testar a imagem recém-construída contra um banco PostgreSQL ou Redis falha porque não há um daemon Docker rodando dentro do container de build. A especificação oficial do `Earthfile` (`WITH DOCKER`) resolve esse problema de forma declarativa.

## Como funciona
Quando um target declara um bloco **`WITH DOCKER`** encerrado por **`END`**, o Earthly cria um ambiente privilegiado isolado para aquele passo, inicia um daemon Docker interno efêmero e aceita flags declarativas que rodam em paralelo antes do `RUN`: (1) **`--load minha-app:latest=+docker`**: constrói o target `+docker` paralelamente no BuildKit e carrega a imagem resultante dentro do daemon Docker interno sem precisar passar por um registry externo; (2) **`--pull postgres:15`**: faz pull cacheado de imagens auxiliares; e (3) **`--compose docker-compose.yml`**: sobe automaticamente os serviços do Compose antes de executar o comando `RUN` dos testes de integração e derruba tudo ao atingir o `END`.

## Exemplo
```dockerfile
# Exemplo de target de teste de integração no Earthfile usando WITH DOCKER e --load da imagem construída em +docker
VERSION 0.8
integration-test:
    FROM docker:24-cli
    COPY docker-compose.yml .
    WITH DOCKER --compose docker-compose.yml --load go-example:latest=+docker
        RUN docker exec test-runner ./run-e2e-tests.sh
    END
```

## Limites e trade-offs
Como o bloco `WITH DOCKER ... END` precisa iniciar um daemon Docker aninhado (Docker-in-Docker) para cada execução, o container `earthly-buildkitd` no host precisa rodar com privilégios adequados, e deve-se agrupar os comandos de teste dentro de um único `RUN` no bloco `WITH DOCKER ... END` (já que apenas um único comando `RUN` é permitido por bloco `WITH DOCKER`).

## Como verificar
Execute `earthly +integration-test` e verifique nos logs que o target `+docker` é construído no BuildKit, carregado no daemon interno via `--load` e testado contra os serviços do Compose.

## Conexões
- [[earthly-gerenciamento-segredos-run-secret-push-seguranca]] — Veja também: Earthly: injeção segura de segredos em tempo de build (RUN --secret) e publicação condicional (RUN --push).
- [[earthly-execucao-paralela-dag-buildkit-cache-camadas]] — Veja também: Earthly: paralelismo automático por DAG no BuildKit, mounts de cache (--mount type=cache) e funções reutilizáveis (FUNCTION).
- [[earthly-automacao-build-containers-earthfile-reprodutivel]] — Referência cruzada direta com earthly-automacao-build-containers-earthfile-reprodutivel.
- [[earthly-sintaxe-earthfile-targets-dependencias-build]] — Referência cruzada direta com earthly-sintaxe-earthfile-targets-dependencias-build.
- [[earthly-integracao-qualquer-ci-github-actions-gitlab-jenkins]] — Referência cruzada direta com earthly-integracao-qualquer-ci-github-actions-gitlab-jenkins.

## Fontes
- [Earthly GitHub — README.md (Containerized Build Framework, Earthfile Examples, Cross-Directory Imports, Multi-Platform & Secrets)](https://raw.githubusercontent.com/earthly/earthly/main/README.md) — README oficial do Earthly (MPL-2.0) demonstrando sintaxe Earthfile VERSION 0.8, SAVE ARTIFACT AS LOCAL, SAVE IMAGE, FROM DOCKERFILE, imports entre diretórios/repositórios, builds multiplataforma e RUN --push --secret; consultado em 2026-10-03.
- [Earthly Official Documentation — Earthfile Reference](https://docs.earthly.dev/docs/earthfile) — Referência técnica oficial da gramática do Earthfile, base target, invocação de targets (+), WITH DOCKER, CACHE e FUNCTION; consultado em 2026-10-03.
- [Earthly — Official GitHub Repository](https://github.com/earthly/earthly) — Repositório oficial MPL-2.0 do Earthly; consultado em 2026-10-03.

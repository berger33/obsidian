---
id: software.devops.tranche08.000795
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

# Earthly: adoção incremental e reutilização de Dockerfiles existentes com FROM DOCKERFILE

## Em uma frase
A instrução `FROM DOCKERFILE` permite que um target no `Earthfile` herde diretamente a construção de um `Dockerfile` já existente no projeto (incluindo suporte a `--target` de multi-stage e `--build-arg`), facilitando a migração gradual para o Earthly.

## Por que importa
Equipes que já possuem dezenas de `Dockerfile`s funcionando em produção muitas vezes hesitam em adotar uma nova ferramenta de build se isso exigir reescrever todos os seus `Dockerfile`s do zero no primeiro dia. A seção `Highlights` do README oficial do Earthly mostra como `FROM DOCKERFILE` permite reutilizar 100% dos Dockerfiles existentes imediatamente.

## Como funciona
Quando um target declara `FROM DOCKERFILE .` (ou `FROM DOCKERFILE -f Dockerfile.prod --target builder --build-arg GO_VERSION=1.21 ./context`), o Earthly lê o `Dockerfile` especificado, traduz suas instruções para o mesmo grafo BuildKit do Earthly e disponibiliza o sistema de arquivos e metadados resultantes dentro do target do `Earthfile`. A partir daí, o desenvolvedor pode adicionar apenas `SAVE IMAGE minha-app:latest` ou criar novos targets de teste (`+test`) e lint (`+lint`) que herdam daquele `FROM DOCKERFILE`, migrando a lógica para targets nativos do `Earthfile` no seu próprio ritmo.

## Exemplo
```dockerfile
# Exemplo oficial do README reutilizando um Dockerfile existente no diretório atual dentro de um Earthfile
VERSION 0.8
docker:
    FROM DOCKERFILE .
    SAVE IMAGE some-image:latest
```

## Limites e trade-offs
Embora `FROM DOCKERFILE .` seja excelente para onboarding imediato, um `Dockerfile` monolítico tradicional não expõe artefatos intermediários via `SAVE ARTIFACT`; à medida que o projeto evolui, converter as etapas do `Dockerfile` em targets nativos do `Earthfile` (`+deps`, `+build`, `+test`, `+docker`) destrava o reuso fino de artefatos e o paralelismo máximo entre testes e imagem final.

## Como verificar
Em um repositório que já possua um `Dockerfile`, crie um `Earthfile` mínimo de 4 linhas usando `FROM DOCKERFILE .` e execute `earthly +docker` para validar a geração da imagem.

## Conexões
- [[earthly-imports-monorepos-multi-repositorios-remotos]] — Veja também: Earthly: composição de builds em monorepos e entre múltiplos repositórios Git remotos.
- [[earthly-builds-multiplataforma-linux-amd64-arm64]] — Veja também: Earthly: builds e imagens multiplataforma (linux/amd64 e linux/arm64) em um único comando BUILD --platform.
- [[earthly-automacao-build-containers-earthfile-reprodutivel]] — Referência cruzada direta com earthly-automacao-build-containers-earthfile-reprodutivel.
- [[earthly-artefatos-save-artifact-as-local-save-image]] — Referência cruzada direta com earthly-artefatos-save-artifact-as-local-save-image.

## Fontes
- [Earthly GitHub — README.md (Containerized Build Framework, Earthfile Examples, Cross-Directory Imports, Multi-Platform & Secrets)](https://raw.githubusercontent.com/earthly/earthly/main/README.md) — README oficial do Earthly (MPL-2.0) demonstrando sintaxe Earthfile VERSION 0.8, SAVE ARTIFACT AS LOCAL, SAVE IMAGE, FROM DOCKERFILE, imports entre diretórios/repositórios, builds multiplataforma e RUN --push --secret; consultado em 2026-10-03.
- [Earthly Official Documentation — Earthfile Reference](https://docs.earthly.dev/docs/earthfile) — Referência técnica oficial da gramática do Earthfile, base target, invocação de targets (+), WITH DOCKER, CACHE e FUNCTION; consultado em 2026-10-03.
- [Earthly — Official GitHub Repository](https://github.com/earthly/earthly) — Repositório oficial MPL-2.0 do Earthly; consultado em 2026-10-03.

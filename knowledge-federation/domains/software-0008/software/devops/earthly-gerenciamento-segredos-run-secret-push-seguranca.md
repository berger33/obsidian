---
id: software.devops.tranche08.000797
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

# Earthly: injeção segura de segredos em tempo de build (RUN --secret) e publicação condicional (RUN --push)

## Em uma frase
O comando `RUN --secret VAR=secret_id` injeta credenciais apenas na memória daquele comando específico sem jamais gravá-las nas camadas de cache ou na imagem final, enquanto `RUN --push` garante que efeitos colaterais externos só rodem quando `earthly --push` for autorizado.

## Por que importa
Um erro grave de segurança em Dockerfiles tradicionais é passar tokens privados (`GITHUB_TOKEN`, `NPM_TOKEN`, chaves SSH ou credenciais AWS) via `ARG` ou `ENV`: essas credenciais ficam gravadas permanentemente no histórico da imagem (`docker history`) e no cache de camadas. A seção `Cloud Secrets` do README oficial do Earthly mostra como `RUN --secret` e `RUN --push` protegem credenciais e efeitos colaterais.

## Como funciona
(1) **`RUN --secret ENV_VAR=secret_name`** (ou `--mount type=secret,id=secret_name,target=/caminho`): o Earthly solicita o valor do segredo (passado na CLI via `earthly --secret github_token="$GITHUB_TOKEN" +release` ou arquivo `.secret`) ao BuildKit e o expõe exclusivamente para aquele processo `RUN`; o valor nunca faz parte da chave de cache da camada nem é persistido no disco da imagem; e (2) **`RUN --push`** (e `SAVE IMAGE --push`): marca comandos que realizam ações irreversíveis no mundo externo (como `git push`, upload de release para S3/GitHub ou deploy). Por padrão (`earthly +release`), comandos `RUN --push` são pulados; eles só são executados se o operador invocar explicitamente `earthly --push +release` e somente após todos os demais targets do build passarem sem erros.

## Exemplo
```dockerfile
# Exemplo oficial do README usando RUN --push e --secret sem vazar o token em camadas da imagem
VERSION 0.8
release:
    FROM alpine:3.18
    COPY +build/prod-B .
    RUN --push --secret GITHUB_TOKEN=github_token github-release upload --File prod-B
```

## Limites e trade-offs
Como comandos `RUN --push` nunca são cacheados e só executam na fase final de exportação quando a flag `--push` é passada na linha de comando, nenhum comando `COPY`, `RUN` normal ou `SAVE ARTIFACT` pode ser declarado **depois** de um `RUN --push` dentro do mesmo target (pois a imagem/artefato já foi finalizada antes da fase de push).

## Como verificar
Execute `earthly +release` (sem `--push`) e confirme nos logs que a etapa `RUN --push` é exibida como ignorada (`--push` não habilitado), protegendo execuções locais acidentais.

## Conexões
- [[earthly-builds-multiplataforma-linux-amd64-arm64]] — Veja também: Earthly: builds e imagens multiplataforma (linux/amd64 e linux/arm64) em um único comando BUILD --platform.
- [[earthly-integracao-docker-in-docker-with-docker-testes]] — Veja também: Earthly: testes de integração com containers e Docker Compose dentro do build usando WITH DOCKER.
- [[earthly-automacao-build-containers-earthfile-reprodutivel]] — Referência cruzada direta com earthly-automacao-build-containers-earthfile-reprodutivel.
- [[earthly-artefatos-save-artifact-as-local-save-image]] — Referência cruzada direta com earthly-artefatos-save-artifact-as-local-save-image.

## Fontes
- [Earthly GitHub — README.md (Containerized Build Framework, Earthfile Examples, Cross-Directory Imports, Multi-Platform & Secrets)](https://raw.githubusercontent.com/earthly/earthly/main/README.md) — README oficial do Earthly (MPL-2.0) demonstrando sintaxe Earthfile VERSION 0.8, SAVE ARTIFACT AS LOCAL, SAVE IMAGE, FROM DOCKERFILE, imports entre diretórios/repositórios, builds multiplataforma e RUN --push --secret; consultado em 2026-10-03.
- [Earthly Official Documentation — Earthfile Reference](https://docs.earthly.dev/docs/earthfile) — Referência técnica oficial da gramática do Earthfile, base target, invocação de targets (+), WITH DOCKER, CACHE e FUNCTION; consultado em 2026-10-03.
- [Earthly — Official GitHub Repository](https://github.com/earthly/earthly) — Repositório oficial MPL-2.0 do Earthly; consultado em 2026-10-03.

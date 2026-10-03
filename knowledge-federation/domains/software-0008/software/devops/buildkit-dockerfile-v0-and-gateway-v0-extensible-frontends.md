---
id: software.devops.tranche04.000353
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-04.md"
fontes: ["https://raw.githubusercontent.com/moby/buildkit/master/README.md", "https://pkg.go.dev/github.com/moby/buildkit/client/llb", "https://github.com/moby/buildkit"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Frontends extensíveis no BuildKit: dockerfile.v0, gateway.v0 e linguagens alternativas para LLB

## Em uma frase
No BuildKit, **frontends** são componentes que rodam dentro do próprio BuildKit e convertem uma definição de build em alto nível para o grafo binário LLB. Além do frontend interno **`dockerfile.v0`** (`buildctl build --frontend=dockerfile.v0 --local context=. --local dockerfile=.`), existe o frontend especial **`gateway.v0`** (`--frontend gateway.v0 --opt source=docker/dockerfile`), que permite usar qualquer imagem OCI externa (como `docker/dockerfile-upstream:master`, Buildpacks, Earthfile, HLB, Nix, Blubber, DALEC ou envd) como compilador de linguagem de build para LLB.

## Por que importa
Separar a linguagem de escrita do build (frontend) do motor de execução e cache (LLB solver) permite adotar novas sintaxes do Dockerfile (`# syntax=docker/dockerfile:1`) ou linguagens declarativas inteiramente diferentes sem precisar atualizar o binário do daemon `buildkitd` nos servidores.

## Como funciona
Use `buildctl build --frontend=dockerfile.v0 --local context=. --local dockerfile=.` (passando `--opt target=foo`, `--opt build-arg:foo=bar` ou `--opt filename=./Dockerfile-alternative` quando necessário) ou invoque `gateway.v0` com `--opt source=docker/dockerfile` para usar versões externas atualizadas do frontend.

## Exemplo
Para testar recursos experimentais de Dockerfile sem atualizar o daemon de build do cluster, o engenheiro executa `buildctl build --frontend gateway.v0 --opt source=docker/dockerfile-upstream:master-labs --local context=. --local dockerfile=.`.

## Limites e trade-offs
Lembre-se de que os nomes `context` e `dockerfile` passados em `--local context=. --local dockerfile=.` são os identificadores exatos que o frontend Dockerfile procura para localizar o diretório de contexto e o Dockerfile no cliente.

## Como verificar
Execute `buildctl build --frontend=dockerfile.v0 --local context=. --local dockerfile=.` em um projeto de teste e confirme a resolução do frontend e a compilação do grafo LLB.

## Conexões
- [[buildkit-buildkitd-daemon-buildctl-client-and-worker-backends]] — Veja também: Arquitetura buildkitd e buildctl com workers OCI (runc/crun) e containerd.
- [[buildkit-dockerfile-run-mounts-bind-cache-tmpfs-secret-ssh]] — Veja também: Montagens avançadas RUN --mount=type=(bind, cache, tmpfs, secret, ssh) no BuildKit.

## Fontes
- [Moby BuildKit GitHub — README.md (Architecture, LLB, Frontends, Outputs & Caching)](https://raw.githubusercontent.com/moby/buildkit/master/README.md) — README oficial do Moby BuildKit detalhando arquitetura buildkitd e buildctl, formato intermediário binário LLB em Protobuf, gateway.v0 e dockerfile.v0, backends OCI (runc/crun) e containerd, opções de output (image, local, compression gzip/estargz/zstd, SOURCE_DATE_EPOCH) e export/import de cache.; consultado em 2026-10-03.
- [Go Package Documentation — github.com/moby/buildkit/client/llb](https://pkg.go.dev/github.com/moby/buildkit/client/llb) — Documentação oficial da biblioteca Go client/llb do BuildKit para construção programática de grafos de dependência LLB.; consultado em 2026-10-03.
- [Moby BuildKit — Official GitHub Repository](https://github.com/moby/buildkit) — Repositório oficial Apache-2.0 do Moby BuildKit.; consultado em 2026-10-03.

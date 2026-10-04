---
id: software.devops.tranche04.000354
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

# Montagens avançadas RUN --mount=type=(bind, cache, tmpfs, secret, ssh) no BuildKit

## Em uma frase
O README oficial destaca as instruções de Dockerfile exclusivas do BuildKit na forma **`RUN --mount=type=(bind|cache|tmpfs|secret|ssh)`**: `type=cache` mantém diretórios de cache de compiladores e gerenciadores de pacotes entre builds sem gravá-los nas camadas finais da imagem; `type=secret` e `type=ssh` injetam credenciais sensíveis ou agentes SSH apenas durante a execução daquele comando `RUN` sem jamais persistir segredos no histórico de camadas; `type=bind` monta arquivos de outros estágios ou do contexto sem `COPY`; e `type=tmpfs` fornece armazenamento efêmero em memória RAM.

## Por que importa
No modelo tradicional de Dockerfile sem BuildKit, passar um token privado via `ARG` ou `COPY` deixava o segredo gravado nos metadados ou nas camadas intermediárias da imagem, e caches de pacotes (`apt`, `pip`, `go mod`, `cargo`) precisavam ser baixados do zero ou poluíam o tamanho da imagem final.

## Como funciona
Substitua argumentos de segredos por `RUN --mount=type=secret,id=meu_token` e acelere a compilação de dependências com `RUN --mount=type=cache,target=/root/.cache/go-build` nos Dockerfiles executados pelo BuildKit.

## Exemplo
Em um build Go corporativo que baixa módulos de repositórios Git privados, o Dockerfile usa `RUN --mount=type=ssh --mount=type=cache,target=/go/pkg/mod go build`, concluindo em segundos sem deixar chaves SSH ou caches de módulos na imagem final.

## Limites e trade-offs
Nunca use `ARG` ou `ENV` para passar chaves privadas ou tokens de registro em Dockerfiles quando o BuildKit estiver disponível; utilize exclusivamente `--mount=type=secret` ou `--mount=type=ssh`.

## Como verificar
Inspecione a imagem final construída (por exemplo com `syft <image> --scope all-layers` ou `docker history`) e confirme que nem os arquivos de cache nem o segredo montado aparecem em nenhuma camada.

## Conexões
- [[buildkit-dockerfile-v0-and-gateway-v0-extensible-frontends]] — Veja também: Frontends extensíveis no BuildKit: dockerfile.v0, gateway.v0 e linguagens alternativas para LLB.
- [[buildkit-image-output-compression-estargz-zstd-and-reproducibility]] — Veja também: Exportação de imagens no BuildKit: compressão gzip/estargz/zstd, oci-mediatypes e SOURCE_DATE_EPOCH.

## Fontes
- [Moby BuildKit GitHub — README.md (Architecture, LLB, Frontends, Outputs & Caching)](https://raw.githubusercontent.com/moby/buildkit/master/README.md) — README oficial do Moby BuildKit detalhando arquitetura buildkitd e buildctl, formato intermediário binário LLB em Protobuf, gateway.v0 e dockerfile.v0, backends OCI (runc/crun) e containerd, opções de output (image, local, compression gzip/estargz/zstd, SOURCE_DATE_EPOCH) e export/import de cache.; consultado em 2026-10-03.
- [Go Package Documentation — github.com/moby/buildkit/client/llb](https://pkg.go.dev/github.com/moby/buildkit/client/llb) — Documentação oficial da biblioteca Go client/llb do BuildKit para construção programática de grafos de dependência LLB.; consultado em 2026-10-03.
- [Moby BuildKit — Official GitHub Repository](https://github.com/moby/buildkit) — Repositório oficial Apache-2.0 do Moby BuildKit.; consultado em 2026-10-03.

---
id: software.devops.tranche04.000356
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

# Exportação de artefatos para diretório local (type=local) e tarballs OCI ou Docker no BuildKit

## Em uma frase
O BuildKit não é restrito a produzir imagens de contêiner: usando `--output type=local,dest=path/to/output-dir`, o cliente copia diretamente os arquivos gerados para um diretório local da máquina cliente. Para exportar apenas artefatos específicos (como binários compilados ou relatórios `testresult.xml`), usa-se um estágio final `FROM scratch AS testresult` com `COPY --from=builder` combinado a `--opt target=testresult --output type=local,dest=path/to/output-dir`, ou a opção direta `src=<path>` sem estágio dedicado. O BuildKit também exporta tarballs Docker, tarballs OCI e diretamente para o image store do containerd.

## Por que importa
Usar o BuildKit com `type=local` permite compilar binários nativos, pacotes ou relatórios de testes em um ambiente hermético e cacheado por LLB sem precisar extrair arquivos manualmente de contêineres temporários com `docker create` + `docker cp`.

## Como funciona
Em pipelines de CI que compilam binários para release ou geram relatórios JUnit XML dentro de contêineres isolados, defina um estágio `FROM scratch` contendo apenas os arquivos de saída e extraia-os diretamente com `--output type=local,dest=./dist`.

## Exemplo
Um Dockerfile define `FROM scratch AS artifact` copiando apenas `/out/app-linux-amd64` do estágio compilador; o comando `buildctl build ... --opt target=artifact --output type=local,dest=./bin` entrega o binário pronto no host em uma única etapa.

## Limites e trade-offs
Evite usar `--output type=local` apontando para o estágio `builder` inteiro sem filtrar por um estágio `FROM scratch` ou `src=<path>`, pois isso copiaria todo o sistema de arquivos da distribuição Linux para o diretório local do cliente.

## Como verificar
Execute o build com `--opt target=<scratch-stage> --output type=local,dest=./out` e verifique que `./out` contém exclusivamente os artefatos copiados para o estágio `scratch`.

## Conexões
- [[buildkit-image-output-compression-estargz-zstd-and-reproducibility]] — Veja também: Exportação de imagens no BuildKit: compressão gzip/estargz/zstd, oci-mediatypes e SOURCE_DATE_EPOCH.
- [[buildkit-cache-import-export-inline-registry-local-and-cloud]] — Veja também: Exportação e importação de cache de build (inline, registry, local, GitHub Actions, S3 e Azure Blob).

## Fontes
- [Moby BuildKit GitHub — README.md (Architecture, LLB, Frontends, Outputs & Caching)](https://raw.githubusercontent.com/moby/buildkit/master/README.md) — README oficial do Moby BuildKit detalhando arquitetura buildkitd e buildctl, formato intermediário binário LLB em Protobuf, gateway.v0 e dockerfile.v0, backends OCI (runc/crun) e containerd, opções de output (image, local, compression gzip/estargz/zstd, SOURCE_DATE_EPOCH) e export/import de cache.; consultado em 2026-10-03.
- [Go Package Documentation — github.com/moby/buildkit/client/llb](https://pkg.go.dev/github.com/moby/buildkit/client/llb) — Documentação oficial da biblioteca Go client/llb do BuildKit para construção programática de grafos de dependência LLB.; consultado em 2026-10-03.
- [Moby BuildKit — Official GitHub Repository](https://github.com/moby/buildkit) — Repositório oficial Apache-2.0 do Moby BuildKit.; consultado em 2026-10-03.

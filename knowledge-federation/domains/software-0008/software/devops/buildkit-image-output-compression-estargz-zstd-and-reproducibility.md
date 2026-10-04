---
id: software.devops.tranche04.000355
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

# Exportação de imagens no BuildKit: compressão gzip/estargz/zstd, oci-mediatypes e SOURCE_DATE_EPOCH

## Em uma frase
Por padrão, o resultado de um build no BuildKit permanece apenas no cache interno até que `--output` seja especificado. Na saída `--output type=image,name=docker.io/user/image,push=true`, o BuildKit suporta chaves avançadas documentadas no README: `oci-mediatypes=true` (usa media types OCI padrão em vez dos tipos Docker), `oci-artifact=true` (formato de artefato OCI para atestações), `compression=<uncompressed|gzip|estargz|zstd>` com `compression-level` (0–9 para gzip/estargz e 0–22 para zstd; `estargz` exige `oci-mediatypes=true`), `force-compression=true`, `annotation.<key>=<value>` e `rewrite-timestamp=true` para reescrever timestamps de arquivos para o valor de `SOURCE_DATE_EPOCH` visando builds reproduzíveis (`docs/build-repro.md`).

## Por que importa
A escolha da compressão e dos metadados afeta diretamente o tempo de cold start no cluster (onde `zstd` descomprime muito mais rápido que `gzip` e `estargz` habilita lazy pulling) e a reprodutibilidade criptográfica do digest da imagem (`rewrite-timestamp=true` com `SOURCE_DATE_EPOCH`).

## Como funciona
Em pipelines de produção modernos, habilite `oci-mediatypes=true,compression=zstd` para reduzir tempo de pull nos nós Kubernetes e adote `rewrite-timestamp=true` aliado a `SOURCE_DATE_EPOCH` quando precisar de builds deterministicamente reproduzíveis.

## Exemplo
Para publicar a mesma imagem em dois registros simultaneamente com compressão zstd e media types OCI, o pipeline executa `buildctl build ... --output type=image,"name=ghcr.io/org/app,registry.interno/org/app",push=true,oci-mediatypes=true,compression=zstd`.

## Limites e trade-offs
Ao selecionar `compression=estargz`, lembre-se de passar obrigatoriamente `oci-mediatypes=true` conforme exigido pela documentação oficial, e use `force-compression=true` se precisar recompactar camadas já existentes herdadas da imagem base.

## Como verificar
Inspecione o manifesto da imagem publicada no registro e confirme os media types OCI, o algoritmo de compressão das camadas e as anotações anexadas.

## Conexões
- [[buildkit-dockerfile-run-mounts-bind-cache-tmpfs-secret-ssh]] — Veja também: Montagens avançadas RUN --mount=type=(bind, cache, tmpfs, secret, ssh) no BuildKit.
- [[buildkit-local-directory-and-tarball-outputs]] — Veja também: Exportação de artefatos para diretório local (type=local) e tarballs OCI ou Docker no BuildKit.

## Fontes
- [Moby BuildKit GitHub — README.md (Architecture, LLB, Frontends, Outputs & Caching)](https://raw.githubusercontent.com/moby/buildkit/master/README.md) — README oficial do Moby BuildKit detalhando arquitetura buildkitd e buildctl, formato intermediário binário LLB em Protobuf, gateway.v0 e dockerfile.v0, backends OCI (runc/crun) e containerd, opções de output (image, local, compression gzip/estargz/zstd, SOURCE_DATE_EPOCH) e export/import de cache.; consultado em 2026-10-03.
- [Go Package Documentation — github.com/moby/buildkit/client/llb](https://pkg.go.dev/github.com/moby/buildkit/client/llb) — Documentação oficial da biblioteca Go client/llb do BuildKit para construção programática de grafos de dependência LLB.; consultado em 2026-10-03.
- [Moby BuildKit — Official GitHub Repository](https://github.com/moby/buildkit) — Repositório oficial Apache-2.0 do Moby BuildKit.; consultado em 2026-10-03.

---
id: software.devops.tranche04.000358
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

# Coleta de lixo automática (automatic garbage collection) do cache interno no BuildKit

## Em uma frase
Uma das funcionalidades centrais listadas na abertura do README oficial do BuildKit é a **coleta de lixo automática (automatic garbage collection)** do armazenamento de cache local do daemon `buildkitd`. Ao contrário do builder legado do Docker que acumulava camadas órfãs e caches de build indefinidamente até esgotar o disco do host (exigindo cronjobs externos de `docker system prune`), o `buildkitd` monitora o uso de espaço e aplica políticas de retenção automáticas sobre os registros de cache LLB menos utilizados.

## Por que importa
Servidores de CI de alto volume executam centenas de builds por dia; sem garbage collection automático integrado ao grafo de objetos do builder, o esgotamento de disco (`no space left on device`) torna-se a principal causa de indisponibilidade de pipelines.

## Como funciona
Configure as regras de retenção e limites de espaço de garbage collection no arquivo `buildkitd.toml` dos workers de build de acordo com o tamanho do volume dedicado a `/var/lib/buildkit`, e utilize `buildctl du` / `buildctl prune` para inspeção ou limpeza sob demanda.

## Exemplo
Em um pool de workers `buildkitd` persistentes em Kubernetes com discos NVMe de 200 GB, a política automática de GC do `buildkitd` mantém o uso de disco controlado abaixo do limiar configurado enquanto preserva no cache as camadas base mais quentes.

## Limites e trade-offs
Não desabilite a coleta de lixo automática em workers `buildkitd` de longa duração e evite dimensionar o disco do worker menor do que o espaço necessário para manter simultaneamente as camadas dos builds concorrentes ativos.

## Como verificar
Execute `buildctl du` contra o daemon `buildkitd` para auditar o espaço consumido pelos registros de cache e confirmar que o GC mantém o consumo dentro dos limites configurados.

## Conexões
- [[buildkit-cache-import-export-inline-registry-local-and-cloud]] — Veja também: Exportação e importação de cache de build (inline, registry, local, GitHub Actions, S3 e Azure Blob).
- [[buildkit-rootless-execution-and-containerized-kubernetes-deployments]] — Veja também: Execução rootless do BuildKit sem privilégios de root e implantação em Kubernetes.

## Fontes
- [Moby BuildKit GitHub — README.md (Architecture, LLB, Frontends, Outputs & Caching)](https://raw.githubusercontent.com/moby/buildkit/master/README.md) — README oficial do Moby BuildKit detalhando arquitetura buildkitd e buildctl, formato intermediário binário LLB em Protobuf, gateway.v0 e dockerfile.v0, backends OCI (runc/crun) e containerd, opções de output (image, local, compression gzip/estargz/zstd, SOURCE_DATE_EPOCH) e export/import de cache.; consultado em 2026-10-03.
- [Go Package Documentation — github.com/moby/buildkit/client/llb](https://pkg.go.dev/github.com/moby/buildkit/client/llb) — Documentação oficial da biblioteca Go client/llb do BuildKit para construção programática de grafos de dependência LLB.; consultado em 2026-10-03.
- [Moby BuildKit — Official GitHub Repository](https://github.com/moby/buildkit) — Repositório oficial Apache-2.0 do Moby BuildKit.; consultado em 2026-10-03.

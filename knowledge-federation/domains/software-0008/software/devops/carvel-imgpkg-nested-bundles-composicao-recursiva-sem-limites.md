---
id: software.devops.tranche16.001534
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-16.md"
fontes: ["https://carvel.dev/imgpkg/docs/v0.43.x/resources/", "https://raw.githubusercontent.com/carvel-dev/imgpkg/develop/README.md", "https://github.com/carvel-dev/imgpkg"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Carvel imgpkg: composição recursiva de Nested Bundles e extração estruturada em disco

## Em uma frase
Um *Nested Bundle* no `imgpkg` é um bundle referenciado dentro do arquivo `.imgpkg/images.yml` (`ImagesLock`) de um bundle pai, permitindo compor plataformas complexas em árvore sem limite de profundidade ou largura.

## Por que importa
Um produto de plataforma (como um pacote de observabilidade) frequentemente agrupa múltiplos subpacotes independentes (Prometheus, Grafana, Loki), cada qual já publicado como seu próprio bundle `imgpkg` com suas próprias imagens de containers.

## Como funciona
Para os comandos `imgpkg copy` e `imgpkg push`, referenciar um bundle filho em `.imgpkg/images.yml` funciona exatamente como referenciar qualquer outra imagem OCI, com otimização automática de rede e deduplicação de blobs no repositório de destino. A diferença fundamental ocorre no `imgpkg pull -b <bundle-pai> --recursive -o /tmp/out`: o `imgpkg` detecta quais entradas do `ImagesLock` são bundles e extrai o conteúdo de cada bundle aninhado em seu subdiretório correspondente dentro de `.imgpkg/bundles/<sha256-...>/`.

## Exemplo
```bash
imgpkg pull -b registry.airgap.internal/platform/observability-bundle:2.0.0 \
  --recursive \
  -o /tmp/observability-extracted
ls -la /tmp/observability-extracted/.imgpkg/bundles/
```

## Limites e trade-offs
Sem a flag `--recursive` no `imgpkg pull`, apenas os arquivos do bundle de topo são extraídos para o diretório de saída, mantendo os bundles filhos apenas referenciados por digest em `.imgpkg/images.yml`.

## Como verificar
Execute `imgpkg pull --recursive` em um bundle composto e verifique que cada bundle filho em `.imgpkg/bundles/` teve seu próprio `.imgpkg/images.yml` atualizado para o endereço do registry de onde foi baixado.

## Conexões
- [[carvel-imgpkg-copy-relocacao-espessa-registries-air-gapped-tar]] — Veja também: Carvel imgpkg: cópia espessa (*thick copy*) de bundles e imagens dependentes entre registries e tarballs air-gapped.
- [[carvel-imgpkg-bundlelock-lock-output-promocao-gitops]] — Veja também: Carvel imgpkg: rastreamento determinístico de releases com `BundleLock` (`--lock-output`).

## Fontes
- [Carvel imgpkg GitHub — README.md (OCI Bundles, Thick Copy, Air-Gapped Relocation & Deterministic Layers)](https://carvel.dev/imgpkg/docs/v0.43.x/resources/) — README oficial do carvel-dev/imgpkg apresentando o conceito de OCI Bundle, comandos push/pull/copy e suporte a ambientes air-gapped; consultado em 2026-10-03.
- [Carvel imgpkg Official Documentation — Resources v0.43.x (Bundle, .imgpkg Directory, ImagesLock, BundleLock, Nested Bundles & ImageLocations)](https://raw.githubusercontent.com/carvel-dev/imgpkg/develop/README.md) — Referência oficial de recursos do Carvel imgpkg especificando ImagesLock, BundleLock, Nested Bundles recursivos e Locations OCI Image; consultado em 2026-10-03.
- [Carvel imgpkg — Official GitHub Repository](https://github.com/carvel-dev/imgpkg) — Repositório oficial Apache-2.0 do Carvel imgpkg; consultado em 2026-10-03.

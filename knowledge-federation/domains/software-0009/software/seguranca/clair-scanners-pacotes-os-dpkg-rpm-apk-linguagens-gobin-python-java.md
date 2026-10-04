---
id: software.seguranca.tranche07.000693
tipo: tecnica
dominio: software
subdominio: seguranca
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-07.md"
fontes: ["https://quay.github.io/clair/whatis.html", "https://raw.githubusercontent.com/quay/clair/main/README.md", "https://quay.github.io/claircore/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# ClairCore: Matriz de Scanners de Pacotes de Sistema Operacional (`dpkg`, `rpm`, `apk`) e Linguagens (`gobin`, `python`, `java`, `nodejs`, `ruby`, `rust`)

## Em uma frase
A biblioteca **`ClairCore`** (que equipa o Clair v4) executa duas famílias de scanners estáticos sobre cada camada de container: **Distribution / OS Package Scanners** e **Language / Application Package Scanners**.

## Por que importa
Muitas imagens de produção modernas (como imagens baseadas em `gcr.io/distroless/static` ou binários Go/Rust estáticos) não possuem gerenciador de pacotes `apt`/`rpm`/`apk`, mas embarcam dezenas de módulos Go (`go.mod` embutido na seção `.go.buildinfo` do binário ELF), pacotes Python `site-packages` (`METADATA`/`PKG-INFO`) ou arquivos `.jar`/`.war`/`pom.properties` Java.

## Como funciona
O `ClairCore` identifica automaticamente as distribuições suportadas (**Ubuntu**, **Debian**, **RHEL / UBI**, **SUSE**, **Oracle Linux**, **Alpine**, **Amazon Linux**, **VMware Photon**) e inspeciona bancos `/var/lib/dpkg/status`, `/var/lib/rpm/` (BerkeleyDB, NDB e SQLite do RPM 4.16+), `/lib/apk/db/installed`, além de abrir binários ELF Go com o scanner **`gobin`** para extrair a versão exata do compilador Go (`stdlib`) e de cada dependência compilada no binário!

## Exemplo
```bash
# Inspecionar no IndexReport gerado pelo Clair v4 todos os pacotes de SO e de linguagens detectados na imagem
curl -sS "http://127.0.0.1:6060/indexer/api/v1/index_report/sha256:6b5f5f2d4b8c9a1e3f4d5c6b7a8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e" \
  | jq '{packages_count: (.packages | length), distributions: .distributions, environments: .environments}'
```

## Limites e trade-offs
Ao compilar binários Go para containers, **não** remova os metadados de build Go com flags customizadas que apaguem a estrutura `buildinfo` se quiser que scanners estáticos como `ClairCore` (`gobin`), `OSV-Scanner` e `Trivy` detectem CVEs nas bibliotecas Go e na `stdlib` dentro da imagem distroless.

## Como verificar
Verifique no objeto `.packages` do `IndexReport` a presença tanto dos pacotes de sistema operacional quanto dos módulos de linguagem (`gobin`, `python`, `jar`).

## Conexões
- [[clair-fluxo-indexacao-content-addressable-manifest-layers-indexreport]] — Veja também: Clair v4 (`Indexer` & `ClairCore`): Indexação Endereçada por Conteúdo de Manifestos OCI, Deduplicação de Camadas e `IndexReport`.
- [[clair-motor-matching-updaters-fontes-ovals-osv-cvss-enrichment]] — Veja também: Clair v4 (`Matcher`): Atualizadores Contínuos de Feeds de Segurança (OVAL, **OSV**, Red Hat VEX/CSAF, Debian/Ubuntu/Alpine SecDB e NVD CVSS Enrichment).
- [[clair-arquitetura-analise-estatica-containers-claircore-indexer-matcher-notifier]] — Referência cruzada direta com clair-arquitetura-analise-estatica-containers-claircore-indexer-matcher-notifier.

## Fontes
- [Project Quay Clair v4 Official Documentation — What is ClairV4 & Architecture](https://quay.github.io/clair/whatis.html) — documentação oficial do Clair v4 cobrindo a separação ClairCore, Indexer (IndexReport), Matcher (VulnerabilityReport) e Notifier; consultado em 2026-10-03.
- [Project Quay Clair Official GitHub — Container Vulnerability Static Analysis](https://raw.githubusercontent.com/quay/clair/main/README.md) — repositório oficial do projeto Clair v4 e utilitário de linha de comando clairctl; consultado em 2026-10-03.
- [ClairCore Official Documentation — Layer Indexing & Vulnerability Matching Engine](https://quay.github.io/claircore/) — documentação oficial da biblioteca ClairCore para extração de pacotes de SO/linguagens e updaters de vulnerabilidades; consultado em 2026-10-03.

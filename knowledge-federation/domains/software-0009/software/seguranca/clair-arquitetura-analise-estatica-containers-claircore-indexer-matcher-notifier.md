---
id: software.seguranca.tranche07.000691
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

# Project Quay **Clair v4 & `ClairCore`**: Arquitetura de Análise Estática de Imagens OCI/Docker (`Indexer`, `Matcher` e `Notifier`)

## Em uma frase
**Clair v4** (`quay/clair`, Apache-2.0, desenvolvido pelo projeto Red Hat / Quay e motorizado pela biblioteca Go **`ClairCore`**) é o serviço open-source para análise estática e contínua de vulnerabilidades em imagens de containers **OCI** e **Docker**.

## Por que importa
Ao contrário de scanners de linha de comando que precisam baixar e re-extrair todas as camadas de uma imagem a cada execução de CI, o Clair v4 explora o fato de que **camadas OCI (`layers`) e manifestos são endereçados por conteúdo (*content-addressable* por digest SHA-256)** para indexar cada camada uma única vez e reavaliar vulnerabilidades instantaneamente.

## Como funciona
Conforme documentado na arquitetura oficial (`whatis.html`), o Clair v4 divide o trabalho em três serviços independentes (que podem rodar juntos em modo `combo` ou separados como microsserviços escaláveis): **(1) `Indexer`** (baixa as camadas da imagem, extrai pacotes de SO e linguagens e persiste o **`IndexReport`**), **(2) `Matcher`** (cruza um `IndexReport` existente contra os bancos de vulnerabilidades atualizados em background gerando o **`VulnerabilityReport`**) e **(3) `Notifier`** (emite webhooks/notificações assim que um novo CVE afeta qualquer manifesto já indexado no passado).

## Exemplo
```bash
# Consultar a saude e versao de uma instancia do Clair v4 e verificar o endpoint OpenAPI v1
curl -sS http://127.0.0.1:6060/openapi/v1 | jq '.info'
```

## Limites e trade-offs
Separar o `Indexer` (intensivo em I/O de disco e rede para baixar camadas tar.gz/zstd) do `Matcher` (intensivo em consultas SQL e atualização de feeds de segurança) permite escalar horizontalmente cada componente de acordo com a carga do registro de containers.

## Como verificar
Verifique a porta de introspecção/healthcheck (`:8089/healthz` por padrão) para monitorar a prontidão dos três componentes.

## Conexões
- [[clair-fluxo-indexacao-content-addressable-manifest-layers-indexreport]] — Veja também: Clair v4 (`Indexer` & `ClairCore`): Indexação Endereçada por Conteúdo de Manifestos OCI, Deduplicação de Camadas e `IndexReport`.
- [[clair-motor-matching-updaters-fontes-ovals-osv-cvss-enrichment]] — Referência cruzada direta com clair-motor-matching-updaters-fontes-ovals-osv-cvss-enrichment.

## Fontes
- [Project Quay Clair v4 Official Documentation — What is ClairV4 & Architecture](https://quay.github.io/clair/whatis.html) — documentação oficial do Clair v4 cobrindo a separação ClairCore, Indexer (IndexReport), Matcher (VulnerabilityReport) e Notifier; consultado em 2026-10-03.
- [Project Quay Clair Official GitHub — Container Vulnerability Static Analysis](https://raw.githubusercontent.com/quay/clair/main/README.md) — repositório oficial do projeto Clair v4 e utilitário de linha de comando clairctl; consultado em 2026-10-03.
- [ClairCore Official Documentation — Layer Indexing & Vulnerability Matching Engine](https://quay.github.io/claircore/) — documentação oficial da biblioteca ClairCore para extração de pacotes de SO/linguagens e updaters de vulnerabilidades; consultado em 2026-10-03.

---
id: software.seguranca.tranche07.000696
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

# Clair v4 (`clairctl`): Operação via Linha de Comando (`clairctl report`, `export-updaters` / `import-updaters`) para CI/CD e Ambientes *Air-Gapped*

## Em uma frase
O utilitário oficial de linha de comando **`clairctl`** (distribuído junto ao repositório `quay/clair`) permite interagir diretamente com uma instância do Clair v4 a partir de pipelines de CI/CD (GitLab CI, GitHub Actions, Tekton, Jenkins) e gerenciar bundles de vulnerabilidades para redes desconectadas (*Air-Gapped*).

## Por que importa
Ao executar `clairctl report <imagem>`, o `clairctl` consulta o Registry da imagem para montar a estrutura `Manifest` (com os digests e URLs das camadas), submete o manifesto ao `Indexer` do Clair v4 e recupera o `VulnerabilityReport` formatado em texto, JSON ou XML.

## Como funciona
Para datacenters classificados ou industriais sem saída para a internet, uma máquina conectada na DMZ executa **`clairctl export-updaters --config config.yaml /tmp/vuln-bundle.gz`** (baixando todos os feeds OVAL/OSV/CVSS em um único arquivo comprimido), que é transferido e importado no banco do Clair v4 isolado com **`clairctl import-updaters`**!

## Exemplo
```bash
# Gerar relatorio de vulnerabilidades em JSON via clairctl para uma imagem OCI e exportar bundle de feeds para ambiente air-gapped
clairctl --host http://clair.internal.corp:6060 report -o json \
  registry.internal.corp/payments/api-service:v2.4.1 > /cases/audit/clair_report.json

clairctl export-updaters -c /etc/clair/config.yaml /cases/audit/clair-feeds-20261003.gz
```

## Limites e trade-offs
No pipeline de CI/CD, inspecione o JSON retornado por `clairctl report -o json` com `jq` para bloquear o deploy se houver qualquer vulnerabilidade com `normalized_severity == "Critical"` ou `"High"` que já possua versão corrigida (`fixed_in_version != ""`).

## Como verificar
Teste `clairctl export-updaters` seguido de `clairctl import-updaters` em um banco PostgreSQL de homologação para validar o procedimento de atualização *air-gapped*.

## Conexões
- [[clair-servico-notificacao-notifier-webhooks-novos-cves-imagens-antigas]] — Veja também: Clair v4 (`Notifier`): Detecção Proativa de **Novos CVEs** em Imagens Já Implantadas e Entrega Confiável via **Webhooks / AMQP / STOMP**.
- [[clair-implantacao-combo-vs-microservicos-postgresql-escalabilidade]] — Veja também: Clair v4: Modos de Implantação (`combo` vs Microsserviços `indexer`/`matcher`/`notifier`), Dimensionamento de PostgreSQL e Coordenação via `clair-lock`.
- [[clair-arquitetura-analise-estatica-containers-claircore-indexer-matcher-notifier]] — Referência cruzada direta com clair-arquitetura-analise-estatica-containers-claircore-indexer-matcher-notifier.
- [[clair-motor-matching-updaters-fontes-ovals-osv-cvss-enrichment]] — Referência cruzada direta com clair-motor-matching-updaters-fontes-ovals-osv-cvss-enrichment.

## Fontes
- [Project Quay Clair v4 Official Documentation — What is ClairV4 & Architecture](https://quay.github.io/clair/whatis.html) — documentação oficial do Clair v4 cobrindo a separação ClairCore, Indexer (IndexReport), Matcher (VulnerabilityReport) e Notifier; consultado em 2026-10-03.
- [Project Quay Clair Official GitHub — Container Vulnerability Static Analysis](https://raw.githubusercontent.com/quay/clair/main/README.md) — repositório oficial do projeto Clair v4 e utilitário de linha de comando clairctl; consultado em 2026-10-03.
- [ClairCore Official Documentation — Layer Indexing & Vulnerability Matching Engine](https://quay.github.io/claircore/) — documentação oficial da biblioteca ClairCore para extração de pacotes de SO/linguagens e updaters de vulnerabilidades; consultado em 2026-10-03.

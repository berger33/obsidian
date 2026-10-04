---
id: software.seguranca.tranche07.000699
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

# Clair v4: Normalização de Severidade (`Unknown`, `Negligible`, `Low`, `Medium`, `High`, `Critical`), Enriquecimento CVSS e Priorização

## Em uma frase
Cada fonte de dados de segurança usa sua própria escala de severidade (por exemplo, a Red Hat classifica impacto como `Low`, `Moderate`, `Important`, `Critical`; o Debian usa `unimportant`, `low`, `medium`, `high`; e a NVD usa scores numéricos **CVSS v3.1** de `0.0` a `10.0`); o Clair v4 preserva a severidade original da distribuição em `severity` e fornece o campo padronizado **`normalized_severity`**!

## Por que importa
Ter tanto a classificação contextual do mantenedor da distribuição (`normalized_severity`) quanto o vetor **CVSS v3** (adicionado pelo *Enricher* `cvss` no objeto `.enrichments` do `VulnerabilityReport`) permite criar políticas de risco muito mais inteligentes do que apenas olhar o score bruto da NVD.

## Como funciona
Muitas vezes uma biblioteca possui um CVE com score NVD `9.8 Critical`, mas no pacote oficial do RHEL/Debian a funcionalidade vulnerável vem desabilitada em tempo de compilação, razão pela qual o time de segurança da distribuição classifica o pacote como `Low` ou `Negligible`: priorizar correções onde `normalized_severity` é `Critical`/`High` **e** `fixed_in_version` está disponível foca a engenharia no risco real.

## Exemplo
```bash
# Filtrar no VulnerabilityReport do Clair v4 apenas vulnerabilidades High/Critical que ja possuem correcao disponivel (fixed_in_version)
jq '[.vulnerabilities[] | select((.normalized_severity == "Critical" or .normalized_severity == "High") and (.fixed_in_version != "")) | {name, package: .package.name, installed: .package.version, fixed_in: .fixed_in_version, severity: .normalized_severity}]' \
  /cases/audit/clair_report.json
```

## Limites e trade-offs
Combine a saída filtrada do Clair v4 com a pontuação **EPSS (*Exploit Prediction Scoring System*)** e o catálogo **CISA KEV (*Known Exploited Vulnerabilities*)** no DefectDojo ou Dependency-Track para priorizar imediatamente CVEs explorados ativamente na natureza.

## Como verificar
Verifique no JSON do `VulnerabilityReport` a presença do bloco `.enrichments` contendo os vetores `CVSS:3.1/AV:N/...` associados às vulnerabilidades.

## Conexões
- [[clair-autenticacao-seguranca-api-psk-jwt-tls-introspeccao]] — Veja também: Clair v4: Hardening da API — Autenticação **JWT com Pre-Shared Key (`auth.psk`)**, TLS Mútuo e Isolamento da Porta de Introspecção.
- [[clair-integracao-project-quay-harbor-admission-controllers-vex]] — Veja também: Clair v4: Integração Nativa com **Project Quay**, Políticas de **Kubernetes Admission Control** e Redução de Superfície com Imagens Mínimas.
- [[clair-motor-matching-updaters-fontes-ovals-osv-cvss-enrichment]] — Referência cruzada direta com clair-motor-matching-updaters-fontes-ovals-osv-cvss-enrichment.

## Fontes
- [Project Quay Clair v4 Official Documentation — What is ClairV4 & Architecture](https://quay.github.io/clair/whatis.html) — documentação oficial do Clair v4 cobrindo a separação ClairCore, Indexer (IndexReport), Matcher (VulnerabilityReport) e Notifier; consultado em 2026-10-03.
- [Project Quay Clair Official GitHub — Container Vulnerability Static Analysis](https://raw.githubusercontent.com/quay/clair/main/README.md) — repositório oficial do projeto Clair v4 e utilitário de linha de comando clairctl; consultado em 2026-10-03.
- [ClairCore Official Documentation — Layer Indexing & Vulnerability Matching Engine](https://quay.github.io/claircore/) — documentação oficial da biblioteca ClairCore para extração de pacotes de SO/linguagens e updaters de vulnerabilidades; consultado em 2026-10-03.

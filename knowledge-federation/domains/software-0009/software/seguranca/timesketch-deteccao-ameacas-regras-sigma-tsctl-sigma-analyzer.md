---
id: software.seguranca.tranche06.000525
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-06.md"
fontes: ["https://raw.githubusercontent.com/google/timesketch/master/README.md", "https://timesketch.org/guides/user/sketch-overview/", "https://timesketch.org/guides/admin/install/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Timesketch: Caça a Ameaças (*Threat Hunting*) Retroativa em Timelines com Regras **Sigma** e `tsctl`

## Em uma frase
O Timesketch integra nativamente o padrão aberto **Sigma** (*Generic Signature Format for SIEM Systems*), permitindo traduzir regras Sigma de detecção de ameaças para queries OpenSearch compatíveis com os campos do Plaso e executá-las retroativamente sobre qualquer timeline forense.

## Por que importa
Quando uma nova técnica de ataque ou CVE zero-day é divulgada hoje com uma regra Sigma correspondente, a equipe DFIR pode rodar o **Sigma Analyzer** sobre timelines de incidentes passados para verificar se o atacante utilizou aquela técnica semanas atrás.

## Como funciona
As regras Sigma são gerenciadas pela CLI administrativa (`tsctl list-sigma-rules`, `tsctl import-sigma-rules`) ou na interface web, e o *Sigma Analyzer* varre a timeline marcando cada evento correspondente com a tag `sigma:<rule_id>` e anexando os metadados da regra (título, severidade, referências MITRE ATT&CK).

## Exemplo
```bash
# Listar regras Sigma instaladas e validar o mapeamento de uma regra no servidor Timesketch via tsctl
tsctl list-sigma-rules | head -n 20
```

## Limites e trade-offs
Regras Sigma escritas originalmente para campos proprietários do Sysmon no Splunk precisam que o arquivo de mapeamento Sigma do Timesketch (`/etc/timesketch/sigma_config.yaml`) traduza os nomes dos campos para o esquema gerado pelos parsers do Plaso/JSONL.

## Como verificar
Execute o *Sigma Analyzer* sobre uma timeline de teste contendo eventos Windows `.evtx` suspeitos e filtre por `tag:sigma*` na aba *Explore*.

## Conexões
- [[timesketch-analisadores-automaticos-analyzers-chain-tagger-similarity]] — Veja também: Timesketch: Execução de **Analyzers** Automatizados em Background (Taggers, Chain Analyzer, Account Finder, Domain/Hash Enrichment).
- [[timesketch-investigacao-guiada-dfiq-questions-facets-approaches]] — Veja também: Timesketch: Investigação Guiada com **DFIQ** (*Digital Forensics Investigative Questions* — Scenarios, Facets, Questions e Approaches).
- [[timesketch-linguagem-busca-opensearch-dsl-saved-views-context-query]] — Referência cruzada direta com timesketch-linguagem-busca-opensearch-dsl-saved-views-context-query.

## Fontes
- [Google Timesketch Official GitHub — Collaborative Forensic Timeline Analysis](https://raw.githubusercontent.com/google/timesketch/master/README.md) — documentação oficial do Google Timesketch para análise colaborativa de timelines forenses; consultado em 2026-10-03.
- [Timesketch Official User Guide — Sketch Overview & Lifecycle](https://timesketch.org/guides/user/sketch-overview/) — guia oficial de abas do Sketch (Explore, Stories, Intelligence), tsctl, arquivamento e labels de proteção; consultado em 2026-10-03.
- [Timesketch Official Admin Guide — Installation & Configuration](https://timesketch.org/guides/admin/install/) — guia oficial de administração, Analyzers, Sigma e DFIQ no Timesketch; consultado em 2026-10-03.

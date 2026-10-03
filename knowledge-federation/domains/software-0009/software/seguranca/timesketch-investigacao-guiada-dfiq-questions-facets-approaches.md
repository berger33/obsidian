---
id: software.seguranca.tranche06.000526
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

# Timesketch: Investigação Guiada com **DFIQ** (*Digital Forensics Investigative Questions* — Scenarios, Facets, Questions e Approaches)

## Em uma frase
O Timesketch implementa nativamente o framework open-source **DFIQ** (*Digital Forensics Investigative Questions*, `google/dfiq`), um catálogo estruturado em YAML que decompõe cenários forenses complexos em perguntas investigativas padronizadas e consultas prontas.

## Por que importa
Padroniza o raciocínio investigativo entre analistas juniores e seniores: em vez de encarar uma tela em branco, o analista seleciona o cenário DFIQ (ex.: *Compromised Windows Host* ou *Data Exfiltration*), e o Timesketch apresenta a árvore de perguntas que devem ser respondidas.

## Como funciona
A hierarquia do DFIQ organiza-se em quatro níveis: **Scenarios** (o tipo de incidente de alto nível), **Facets** (agrupamentos temáticos como *Initial Access*, *Persistence*, *Lateral Movement*), **Questions** (perguntas objetivas como *"Quais extensões de navegador foram instaladas no sistema?"* ou *"Houve execução de tarefas agendadas anômalas?"*) e **Approaches** (os passos exatos, artefatos necessários e queries Timesketch/Plaso que respondem àquela pergunta automaticamente).

## Exemplo
```yaml
# Estrutura resumida de uma Question e Approach no formato YAML do DFIQ integrado ao Timesketch
id: Q1024
display_name: "Were any new Windows Services installed on the system?"
type: question
description: "Attackers frequently install malicious services for persistence or privilege escalation."
approaches:
  - name: "Search Windows System Event Log for Event ID 7045 and Security Log for 4697"
    processors:
      - name: timesketch
        analysis:
          - type: query
            value: 'data_type:"windows:evtx:record" AND (event_identifier:7045 OR event_identifier:4697)'
```

## Limites e trade-offs
Para habilitar o catálogo DFIQ no Timesketch, configure `DFIQ_ENABLED = True` e aponte `DFIQ_PATH` em `/etc/timesketch/timesketch.conf` para o diretório contendo os templates YAML oficiais e internos do seu CSIRT.

## Como verificar
Verifique no painel lateral esquerdo do Sketch a renderização das árvores de perguntas DFIQ e clique em uma pergunta para executar a query associada.

## Conexões
- [[timesketch-deteccao-ameacas-regras-sigma-tsctl-sigma-analyzer]] — Veja também: Timesketch: Caça a Ameaças (*Threat Hunting*) Retroativa em Timelines com Regras **Sigma** e `tsctl`.
- [[timesketch-aba-intelligence-iocs-integracao-yeti-misp-opencti]] — Veja também: Timesketch: Aba **Intelligence**, Marcação de IOCs na Timeline e Integração com Plataformas de CTI (Yeti, MISP e OpenCTI).
- [[timesketch-arquitetura-analise-colaborativa-timelines-forenses-opensearch]] — Referência cruzada direta com timesketch-arquitetura-analise-colaborativa-timelines-forenses-opensearch.
- [[timesketch-linguagem-busca-opensearch-dsl-saved-views-context-query]] — Referência cruzada direta com timesketch-linguagem-busca-opensearch-dsl-saved-views-context-query.
- [[timesketch-narrativa-forense-stories-grafos-relatorios-markdown]] — Referência cruzada direta com timesketch-narrativa-forense-stories-grafos-relatorios-markdown.

## Fontes
- [Google Timesketch Official GitHub — Collaborative Forensic Timeline Analysis](https://raw.githubusercontent.com/google/timesketch/master/README.md) — documentação oficial do Google Timesketch para análise colaborativa de timelines forenses; consultado em 2026-10-03.
- [Timesketch Official User Guide — Sketch Overview & Lifecycle](https://timesketch.org/guides/user/sketch-overview/) — guia oficial de abas do Sketch (Explore, Stories, Intelligence), tsctl, arquivamento e labels de proteção; consultado em 2026-10-03.
- [Timesketch Official Admin Guide — Installation & Configuration](https://timesketch.org/guides/admin/install/) — guia oficial de administração, Analyzers, Sigma e DFIQ no Timesketch; consultado em 2026-10-03.

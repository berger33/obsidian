---
id: software.seguranca.tranche06.000530
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

# Timesketch: Governança de Acesso (ACLs de Sketch), Rótulos de Preservação Legal (`protected` / `preserved`), Arquivamento e `tsctl`

## Em uma frase
Como linhas do tempo forenses contêm evidências críticas que podem ser submetidas a processos judiciais ou auditorias regulatórias, o Timesketch implementa controles granulares de ACL por Sketch, rótulos de bloqueio contra exclusão (**`protected`** e **`preserved`**) e arquivamento reversível.

## Por que importa
Um erro operacional ou tentativa maliciosa de apagar um Sketch (`Soft Delete` ou `Hard Delete`) destruiria anotações de semanas de trabalho investigativo; aplicar a label `protected` ou `preserved` impede que **qualquer usuário (inclusive administradores)** delete ou arquive o Sketch enquanto a label estiver ativa.

## Como funciona
Quando um caso é encerrado mas precisa ser retido a baixo custo, a operação **Archive** marca o Sketch e suas timelines como `archived` e **fecha os índices correspondentes no OpenSearch** (desde que o índice não seja compartilhado com outro sketch ativo), liberando memória RAM do cluster OpenSearch até que um analista clique em **Unarchive** para reabrir o índice instantaneamente.

## Exemplo
```bash
# Inspecionar o status de uma timeline especifica e listar usuarios/ACLs via tsctl no servidor Timesketch
tsctl timeline-status 7
tsctl list-users
```

## Limites e trade-offs
Conforme documentado no guia oficial do Timesketch, o sistema verifica em todo o cluster se um índice OpenSearch é compartilhado por mais de um Sketch ativo antes de fechá-lo no *Soft Delete* ou *Archive* ou apagá-lo no *Hard Delete*, garantindo integridade de dados entre investigações.

## Como verificar
Aplique a label `protected` a um Sketch de teste e tente deletá-lo, confirmando que a plataforma bloqueia a operação até que a label de proteção seja explicitamente removida.

## Conexões
- [[timesketch-automacao-python-timesketch-api-client-notebooks-jupyter]] — Veja também: Timesketch: Ciência de Dados Forense com **`timesketch-api-client`**, DataFrames `pandas` e Container Jupyter Notebook (`picatrix`).
- [[timesketch-arquitetura-analise-colaborativa-timelines-forenses-opensearch]] — Referência cruzada direta com timesketch-arquitetura-analise-colaborativa-timelines-forenses-opensearch.
- [[timesketch-narrativa-forense-stories-grafos-relatorios-markdown]] — Referência cruzada direta com timesketch-narrativa-forense-stories-grafos-relatorios-markdown.
- [[thehive-multi-tenancy-organizacoes-rbac-auditoria-webhooks]] — Referência cruzada direta com thehive-multi-tenancy-organizacoes-rbac-auditoria-webhooks.

## Fontes
- [Google Timesketch Official GitHub — Collaborative Forensic Timeline Analysis](https://raw.githubusercontent.com/google/timesketch/master/README.md) — documentação oficial do Google Timesketch para análise colaborativa de timelines forenses; consultado em 2026-10-03.
- [Timesketch Official User Guide — Sketch Overview & Lifecycle](https://timesketch.org/guides/user/sketch-overview/) — guia oficial de abas do Sketch (Explore, Stories, Intelligence), tsctl, arquivamento e labels de proteção; consultado em 2026-10-03.
- [Timesketch Official Admin Guide — Installation & Configuration](https://timesketch.org/guides/admin/install/) — guia oficial de administração, Analyzers, Sigma e DFIQ no Timesketch; consultado em 2026-10-03.

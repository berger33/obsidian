---
id: software.seguranca.tranche17.001657
tipo: tecnica
dominio: software
subdominio: seguranca
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-17.md"
fontes: ["https://kyverno.io/docs/introduction/quick-start/", "https://kyverno.io/docs/guides/migration-to-cel/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Kyverno: Escopo por recurso e namespace

## Em uma frase
**Kyverno — Escopo por recurso e namespace:** Match e exclude definem quais recursos e operações são avaliados pela policy.

## Por que importa
O recorte de **escopo por recurso e namespace** ajuda a enforçar configuração segura na admissão e reportar desvios sem substituir revisão de cluster. A equipe registra risco, evidência e responsável.

## Como funciona
Para **escopo por recurso e namespace**, políticas como recursos Kubernetes são avaliadas em requisições de admissão e podem validar, mutar ou gerar recursos conforme a regra. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Restringa regra de Pod a namespaces de aplicação e verifique que namespaces de sistema têm tratamento explícito. Teste em staging autorizado.

## Limites e trade-offs
Filtro muito amplo pode afetar controllers e serviços de cluster; filtro estreito deixa lacunas. Exceções exigem responsável e prazo.

## Como verificar
Teste nomes, labels, namespaces e operações CREATE/UPDATE nos limites do escopo. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[kyverno-relatorios-de-violacoes-e-politica]] — Complementa o tópico com kyverno: relatórios de violações e política.

## Fontes
- [Kyverno — Quick Start](https://kyverno.io/docs/introduction/quick-start/) — guia oficial sobre validação, mutação e geração de políticas; consultado em 2026-10-04.
- [Kyverno — Migration to CEL Policies](https://kyverno.io/docs/guides/migration-to-cel/) — guia atual de migração de ClusterPolicy para tipos de política baseados em CEL; consultado em 2026-10-04.

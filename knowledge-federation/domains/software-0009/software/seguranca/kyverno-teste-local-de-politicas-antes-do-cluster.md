---
id: software.seguranca.tranche17.001660
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

# Kyverno: Teste local de políticas antes do cluster

## Em uma frase
**Kyverno — Teste local de políticas antes do cluster:** Testes de policy permitem validar fixtures de recurso antes de expor regras ao webhook de produção.

## Por que importa
O recorte de **teste local de políticas antes do cluster** ajuda a enforçar configuração segura na admissão e reportar desvios sem substituir revisão de cluster. A equipe registra risco, evidência e responsável.

## Como funciona
Para **teste local de políticas antes do cluster**, políticas como recursos Kubernetes são avaliadas em requisições de admissão e podem validar, mutar ou gerar recursos conforme a regra. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Execute `kyverno test` com recurso que deve passar e recurso que deve falhar antes do merge. Teste em staging autorizado.

## Limites e trade-offs
Teste local não substitui validação no cluster com CRDs, admission e versão real do Kubernetes. Exceções exigem responsável e prazo.

## Como verificar
Rode suíte offline e um teste de integração em cluster efêmero antes de promover enforcement. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[falco-fonte-de-eventos-syscall]] — Complementa o tópico com falco: fonte de eventos syscall.

## Fontes
- [Kyverno — Quick Start](https://kyverno.io/docs/introduction/quick-start/) — guia oficial sobre validação, mutação e geração de políticas; consultado em 2026-10-04.
- [Kyverno — Migration to CEL Policies](https://kyverno.io/docs/guides/migration-to-cel/) — guia atual de migração de ClusterPolicy para tipos de política baseados em CEL; consultado em 2026-10-04.

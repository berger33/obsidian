---
id: software.seguranca.tranche17.001653
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

# Kyverno: Geração de recursos auxiliares

## Em uma frase
**Kyverno — Geração de recursos auxiliares:** Políticas geradoras podem criar recursos relacionados como parte da aplicação de uma regra de governança.

## Por que importa
O recorte de **geração de recursos auxiliares** ajuda a enforçar configuração segura na admissão e reportar desvios sem substituir revisão de cluster. A equipe registra risco, evidência e responsável.

## Como funciona
Para **geração de recursos auxiliares**, políticas como recursos Kubernetes são avaliadas em requisições de admissão e podem validar, mutar ou gerar recursos conforme a regra. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Crie ConfigMap de teste em namespace novo a partir de política aprovada e verifique ownership e sincronização. Teste em staging autorizado.

## Limites e trade-offs
Geração pode ampliar privilégios ou divergir se origem e destino não forem explicitamente limitados. Exceções exigem responsável e prazo.

## Como verificar
Teste remoção e atualização do recurso fonte e confirme ciclo de vida esperado do recurso gerado. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[kyverno-verificacao-de-imagens-assinadas]] — Complementa o tópico com kyverno: verificação de imagens assinadas.

## Fontes
- [Kyverno — Quick Start](https://kyverno.io/docs/introduction/quick-start/) — guia oficial sobre validação, mutação e geração de políticas; consultado em 2026-10-04.
- [Kyverno — Migration to CEL Policies](https://kyverno.io/docs/guides/migration-to-cel/) — guia atual de migração de ClusterPolicy para tipos de política baseados em CEL; consultado em 2026-10-04.

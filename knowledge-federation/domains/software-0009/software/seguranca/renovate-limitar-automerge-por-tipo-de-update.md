---
id: software.seguranca.tranche18.001765
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-18.md"
fontes: ["https://docs.renovatebot.com/configuration-options/", "https://docs.renovatebot.com/key-concepts/dashboard/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Renovate: Limitar automerge por tipo de update

## Em uma frase
**Renovate — Limitar automerge por tipo de update:** Automerge pode mesclar updates sem intervenção quando habilitado, mas é opcional e depende de checks adequados.

## Por que importa
O recorte de **limitar automerge por tipo de update** ajuda a manter dependências e ferramentas atualizadas com revisão, agrupamento e testes automatizados. A equipe registra risco, evidência e responsável.

## Como funciona
Para **limitar automerge por tipo de update**, managers reconhecem arquivos, regras escolhem como agrupar ou agendar updates e a plataforma recebe branches ou pull requests. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Permita automerge apenas para classes de update cobertas por testes e status checks obrigatórios. Teste em staging autorizado.

## Limites e trade-offs
Sem branch protection e checks selecionados, uma atualização com testes falhos pode entrar. Exceções exigem responsável e prazo.

## Como verificar
Simule PR com falha de teste e confirme que a plataforma bloqueia automerge. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[renovate-exigir-aprovacao-para-major-updates]] — Complementa o tópico com renovate: exigir aprovação para major updates.

## Fontes
- [Renovate — Configuration options](https://docs.renovatebot.com/configuration-options/) — referência oficial de managers, packageRules, schedule e automerge; consultado em 2026-10-04.
- [Renovate — Dependency Dashboard](https://docs.renovatebot.com/key-concepts/dashboard/) — guia oficial de aprovação, visibilidade de updates e workflow do dashboard; consultado em 2026-10-04.

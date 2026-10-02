---
id: software.testes.regression-prioritization.000001
tipo: tecnica
dominio: software
subdominio: testes
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-01
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-01
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001.md"
fontes: ["https://dl.acm.org/doi/10.1109/32.988497", "https://www.gasq.org/files/content/ISTQB2/ISTQB-CTAL-TA-Syllabus-v4.0-EN.pdf"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: [Regression test prioritization, Test prioritization, Priorização de testes de regressão]
lote: software-testes-2000-0001
---

# Priorização de testes de regressão por risco e impacto

## Em uma frase
Priorização de regressão ordena testes existentes para executar primeiro os que melhor atendem um objetivo explícito após mudanças, sem confundir ordem com descarte permanente.

## Por que importa
Suítes grandes podem levar mais tempo do que a janela disponível antes de integrar ou liberar uma mudança. Se os testes mais informativos executam cedo, a equipe pode encontrar falhas mais rapidamente e interromper o fluxo para investigação. Análise de risco e impacto da mudança ajuda a escolher o foco, mas não prova que testes fora da seleção não são necessários.

## Como funciona
O ISTQB CTAL-TA aponta diferentes métodos de seleção para regressão e observa que não há técnica manual universalmente superior: resultados dependem da situação. Em estudos empíricos de Elbaum, Malishevsky e Rothermel, várias técnicas de priorização melhoraram a taxa de detecção de falhas ao longo da execução, mas a eficácia variou entre programas e custos de processo. Priorizar decide ordem; selecionar ou reduzir decide que subconjunto será executado. São decisões distintas e devem ficar registradas.

## Exemplo
Após alterar autorização numa API, ordene cedo testes de papéis, acesso cruzado e fluxos dependentes do módulo, usando rastreabilidade e risco. Se houver tempo, execute o restante da suíte; se não houver, registre quais casos ficaram para depois, qual evidência faltou e quem aceitou o risco residual.

## Limites e trade-offs
Prioridade baseada apenas em histórico de defeitos pode ignorar componentes novos, mudanças pequenas porém críticas ou interações entre módulos. Dados de cobertura e mudança têm custo e podem ser imprecisos. Melhorar detecção precoce não garante redução do tempo total nem que todos os defeitos sejam encontrados; os resultados empíricos dos métodos são dependentes do programa e do processo.

## Como verificar
Declare a meta de ordenação, por exemplo detectar defeitos cedo, cobrir código alterado ou proteger riscos críticos. Registre versão e conjunto de testes candidatos, relação com a mudança e motivos de seleção. Compare falhas descobertas e tempo ao longo do tempo; reveja seleções quando surgirem defeitos escapados ou requisitos novos.

## Conexões
- [[risk-based-testing-priorizacao-risco]] — oferece critérios de risco para orientar a ordem.
- [[mutation-testing-eficacia-testes]] — pode ajudar a avaliar defeitos artificiais detectáveis pela suíte.
- [[piramide-testes-estrategia-contexto]] — diferentes níveis da suíte têm custos e feedback distintos.

## Fontes
- [Elbaum, Malishevsky e Rothermel — Test Case Prioritization: A Family of Empirical Studies](https://dl.acm.org/doi/10.1109/32.988497) — evidências empíricas, variação entre programas e custos; acesso em 2026-10-01.
- [ISTQB CTAL-TA Syllabus v4.0, seção 2.2.1](https://www.gasq.org/files/content/ISTQB2/ISTQB-CTAL-TA-Syllabus-v4.0-EN.pdf) — escopo de regressão e seleção de testes após mudanças; acesso em 2026-10-01.

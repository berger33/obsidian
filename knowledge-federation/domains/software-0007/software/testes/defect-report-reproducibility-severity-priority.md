---
id: software.testes.defect-report.000001
tipo: pratica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-01
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-01
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-04.md"
fontes: ["https://astqb.org/5-5-defect-management/", "https://astqb.org/assets/documents/CTFL-4.0-Sample-Exam3-2-Answers.pdf", "https://www.atlassian.com/software/jira/templates/bug-report"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: [Defect report, Bug report, Relatório de defeito, Relatório de bug]
lote: software-testes-2000-0001
---

# Relatório de defeito: reprodução, evidência e triagem

## Em uma frase
Um relatório de defeito comunica uma anomalia com contexto e evidência suficientes para que a equipe investigue, classifique e acompanhe sua resolução.

## Por que importa
“Não funciona” não informa como reproduzir o problema nem qual resultado era esperado. Um relato claro reduz idas e voltas, preserva o contexto da falha e permite acompanhar decisões até o fechamento. Nem toda anomalia reportada será defeito: triagem pode identificar falso positivo, mudança solicitada ou comportamento correto.

## Como funciona
O CTFL descreve um processo com fluxo desde a descoberta até o fechamento: registrar, analisar e classificar anomalias, decidir resposta e fechar o relatório. Um registro útil inclui título conciso, passos de reprodução, esperado e observado, ambiente, versões, frequência e evidência relevante. Severidade descreve impacto; prioridade trata urgência de resposta e deve ser atribuída conforme regras de triagem da organização. O registro deve permitir reproduzir antes de especular sobre causa raiz.

## Exemplo
“Checkout retorna HTTP 500 após confirmar endereço, build 42, Chrome 130/macOS 15” é mais acionável do que “checkout quebrado”. Acrescente os passos numerados, pré-condições, resultado esperado (pedido criado uma vez) e observado (500 e pedido sem estado conhecido), frequência, logs redigidos e identificador do caso de teste. Não inclua senha, token ou dado pessoal desnecessário.

## Limites e trade-offs
Coletar mais informação não é sempre melhor: inclua apenas detalhes úteis e evite segredos ou dados pessoais. Um relato não prova que a causa está no componente indicado pelo autor. Escalas de severidade e prioridade variam; documente os critérios locais em vez de assumir nomes universais. Se não for reproduzível, registre tentativas e diferenças observadas.

## Como verificar
Peça que outra pessoa siga os passos em ambiente correspondente. Confira que esperado e observado são distinguíveis, que versão e pré-condições estão anotadas e que evidência não contém credenciais. Atualize o estado do defeito conforme triagem, correção, teste de confirmação e fechamento.

## Conexões
- [[test-oracles-resultados-esperados]] — esperado precisa estar definido para avaliar a diferença.
- [[test-environment-configuration-management]] — versão e configuração são parte do contexto reproduzível.
- [[regression-test-prioritization-risco-impacto]] — defeitos corrigidos podem gerar regressões a priorizar.

## Fontes
- [ASTQB — ISTQB CTFL §5.5: Defect Management](https://astqb.org/5-5-defect-management/) — fluxo de anomalia, análise, classificação, resposta e fechamento; acesso em 2026-10-01.
- [ASTQB — CTFL v4.0 Sample Exam #3 Answers](https://astqb.org/assets/documents/CTFL-4.0-Sample-Exam3-2-Answers.pdf) — exercício que diferencia severidade pelo impacto e prioridade pela urgência; acesso em 2026-10-01.
- [Atlassian — Bug report template](https://www.atlassian.com/software/jira/templates/bug-report) — campos e passos para descrever reprodução, resultados e ambiente; acesso em 2026-10-01.

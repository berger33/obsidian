---
id: software.testes.state-transition.000001
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
fontes: ["https://astqb.org/assets/documents/ISTQB_CTFL_Syllabus_v4.0.1.pdf", "https://www.gasq.org/files/content/ISTQB2/ISTQB-CTAL-TA-Syllabus-v4.0-EN.pdf"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: [State transition testing, Teste de transição de estados, N-switch coverage]
lote: software-testes-2000-0001
---

# Teste de transição de estados e critérios de cobertura

## Em uma frase
Teste de transição de estados deriva casos a partir de estados, eventos, guardas, ações e transições válidas ou inválidas definidos por um modelo de comportamento.

## Por que importa
Quando a resposta de um sistema depende do estado corrente, testar cada operação uma vez pode não exercitar ciclos, bloqueios ou sequências inválidas. Um modelo de estados torna visível o comportamento esperado após eventos e permite medir aspectos diferentes do caminho percorrido. Ele é aplicável, por exemplo, a fluxos de autenticação, pedidos, dispositivos e protocolos.

## Como funciona
O syllabus ISTQB descreve diagramas de estado e tabelas de estado; uma sequência de eventos gera uma sequência de mudanças de estado. Os critérios não são equivalentes: cobertura de todos os estados exige visitar cada estado; cobertura de transições válidas exige executar cada transição válida; cobertura de todas as transições de uma tabela também tenta transições inválidas. No nível avançado, o ISTQB descreve ainda cobertura N-switch para sequências de transições válidas com comprimento definido.

## Exemplo
Em um sistema de PIN, modele os estados “aguardando PIN”, “tentativas restantes” e “bloqueado”, com eventos de PIN correto/incorreto. Cobrir o estado bloqueado não garante que a transição de uma tentativa para a seguinte funcione. Um teste de sequência pode exercitar erros repetidos até o bloqueio; testes separados podem tentar eventos não permitidos no estado bloqueado.

## Limites e trade-offs
Um modelo incompleto omite estados ou guardas e pode criar confiança artificial. O espaço de sequências cresce com número de estados, transições e comprimento; cobrir um critério não prova todos os caminhos possíveis. Estados concorrentes ou dados contínuos podem exigir abstrações, modelos hierárquicos ou outras técnicas. Defina explicitamente o comportamento de evento inválido em vez de presumir que toda transição ausente é tratada corretamente.

## Como verificar
Confronte cada estado, evento, guarda e ação com a especificação. Declare o critério de cobertura escolhido e calcule os itens cobertos contra o total do modelo. Teste transições inválidas de forma isolada quando um defeito em uma pode mascarar outro; preserve as sequências que reproduzem regressões.

## Conexões
- [[testes-stateful-model-based-hypothesis]] — gera sequências de regras sobre uma máquina de estados de teste.
- [[decision-table-testing-regras-condicionais]] — tabelas de decisão cobrem combinações de condições; uma tabela de estado representa estados/eventos/transições.
- [[combinatorial-testing-pairwise-t-way]] — cobertura de sequência e t-way tratam combinações diferentes.

## Fontes
- [ISTQB/ASTQB — CTFL Syllabus v4.0.1, seção 4.2.4](https://astqb.org/assets/documents/ISTQB_CTFL_Syllabus_v4.0.1.pdf) — diagramas, tabelas e critérios de transição de estados; acesso em 2026-10-01.
- [ISTQB — CTAL Test Analyst Syllabus v4.0, seção 3.2.2](https://www.gasq.org/files/content/ISTQB2/ISTQB-CTAL-TA-Syllabus-v4.0-EN.pdf) — cobertura N-switch e modelagem comportamental avançada; acesso em 2026-10-01.

---
id: software.testes.tranche23.001726
tipo: tecnica
dominio: software
subdominio: testes
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-23.md"
fontes: ["https://boofuzz.readthedocs.io/en/stable/user/quickstart.html", "https://github.com/jtpereyda/boofuzz/blob/master/README.rst"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# post_test_case_callbacks e ProtocolSessionReference: resposta que alimenta a próxima requisição

## Em uma frase
Para "cool stuff like checking responses" — a frase da doc — a Quickstart manda usar post_test_case_callbacks na Session, e para usar dados de uma resposta numa requisição subsequente, aponta a classe ProtocolSessionReference; o README, por sua vez, anuncia "Extensible instrumentation/failure detection" como feature central, da qual esses hooks são a face pública.

## Por que importa
Validar a resposta transforma o fuzzer de gerador em oráculo: um servidor que crasha é óbvio, mas um que responde 200 a um campo malformado que deveria dar erro é um bug que só callback pega — e o ProtocolSessionReference fecha o loop de protocolos com tokens de sessão reais.

## Como funciona
O callback recebe o contexto do test case após cada iteração (posicionamento conforme o parâmetro nomeado da Session), e o ProtocolSessionReference é usado dentro das Requests para importar valores capturados de resposta — os dois nomes aparecem linkados na mesma página de quickstart.

## Exemplo
Adicione um pós-callback que falha o test case quando a resposta contém stack trace, e aponte um ProtocolSessionReference para o token de login do seu protocolo; rode e confirme que a UI marca os test cases rejeitados pelo seu oráculo.

## Limites e trade-offs
A Quickstart dá os nomes e a intenção, não a assinatura completa dos callbacks — os contratos detalhados vivem na referência de API (links source/Session e other-modules da própria página), e comportamentos como ordem de execução não são especificados ali.

## Como verificar
Abra os dois parágrafos finais do Quickstart e siga os âncoras post_test_case_callbacks (Session) e ProtocolSessionReference (other modules) referenciadas por ele.

## Conexões
- [[boofuzz-results-sqlite]] — Veja também: Cada run é um banco SQLite aberto no boofuzz com boo open.
- [[boofuzz-monitors]] — Veja também: Monitores fora do processo: os scripts de processo e rede no root.

## Fontes
- [boofuzz — Quickstart (Read the Docs)](https://boofuzz.readthedocs.io/en/stable/user/quickstart.html) — Session, Target, conexões, Requests, grafo, resultados e exemplos; consultado em 2026-10-03.
- [boofuzz — README.rst oficial](https://github.com/jtpereyda/boofuzz/blob/master/README.rst) — sucessão ao Sulley, features, instalação e comunidade; consultado em 2026-10-03.

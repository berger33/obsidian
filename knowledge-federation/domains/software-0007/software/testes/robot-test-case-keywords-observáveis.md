---
id: software.testes.tranche11.000470
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-11.md"
fontes: ["https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html", "https://robotframework.org/robotframework/latest/libraries/BuiltIn.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Robot Framework: manter caso centrado em comportamento observável

## Em uma frase
Um caso Robot Framework contém chamadas a keywords descritas nas seções de teste e executadas pelas bibliotecas importadas.

## Por que importa
Sequências que apenas reproduzem cliques ou chamadas internas são frágeis e podem não explicar o resultado que a pessoa usuária espera.

## Como funciona
Dê nomes de negócio às user keywords e organize Given/When/Then quando isso melhorar a leitura sem criar camadas vazias.

## Exemplo
Um caso “Pedido confirmado” prepara cliente, envia pedido e verifica status visível e evento esperado, em vez de chamar helper interno de controller.

## Limites e trade-offs
Robot não impõe BDD nem uma quantidade fixa de steps; bom vocabulário depende do domínio.

## Como verificar
Peça a alguém fora da implementação que descreva o objetivo do caso usando apenas nomes e resultado das keywords.

## Conexões
- [[robot-setup-teardown-escopo]] — Veja também: Robot Framework: escolher setup e teardown pelo escopo do recurso.

## Fontes
- [Robot Framework 7.5 — User Guide](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html) — formato de testes, setups, teardowns, tags, templates, variáveis, libraries e arquivos de saída; consultado em 2026-10-02.
- [Robot Framework 7.5 — BuiltIn library](https://robotframework.org/robotframework/latest/libraries/BuiltIn.html) — keywords incorporadas de fluxo, logging, execução, variáveis e assertions; consultado em 2026-10-02.

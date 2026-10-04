---
id: software.testes.tranche11.000477
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
fontes: ["https://robotframework.org/robotframework/latest/libraries/BuiltIn.html", "https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Robot Framework: limitar Run Keyword And Ignore Error a erro esperado

## Em uma frase
Run Keyword And Ignore Error captura falha de keyword e devolve status e mensagem, permitindo tratamento deliberado no fluxo.

## Por que importa
Usar a keyword como wrapper genérico pode fazer a suíte terminar verde apesar de a operação crítica ter falhado.

## Como funciona
Desestruture o status retornado, aceite somente a falha esperada e propague ou marque como falha qualquer resultado inesperado.

## Exemplo
Um teste tenta uma consulta opcional e valida status FAIL apenas para recurso ausente; falha de autenticação continua sendo erro do caso.

## Limites e trade-offs
Capturar a exceção altera a forma de fluxo; o resultado ignorado não deve ser confundido com sucesso da operação.

## Como verificar
Force tanto o erro esperado quanto um erro diferente e confirme que somente o primeiro segue pelo ramo permitido.

## Conexões
- [[robot-keyword-argumentos-e-conversao]] — Veja também: Robot Framework: declarar argumentos de keyword como interface de teste.
- [[robot-wait-until-keyword-succeeds-idempotência]] — Veja também: Robot Framework: repetir condição observável sem repetir efeito irreversível.

## Fontes
- [Robot Framework 7.5 — BuiltIn library](https://robotframework.org/robotframework/latest/libraries/BuiltIn.html) — keywords incorporadas de fluxo, logging, execução, variáveis e assertions; consultado em 2026-10-02.
- [Robot Framework 7.5 — User Guide](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html) — formato de testes, setups, teardowns, tags, templates, variáveis, libraries e arquivos de saída; consultado em 2026-10-02.

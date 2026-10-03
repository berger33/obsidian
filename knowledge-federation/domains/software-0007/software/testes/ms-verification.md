---
id: software.testes.tranche20.001381
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-20.md"
fontes: ["https://www.mock-server.com/mock_server/verification.html", "https://github.com/mock-server/mockserver"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# MockServer: verificar o que foi recebido

## Em uma frase
A verificação consulta os pedidos registrados e confirma a quantidade de ocorrências, podendo exigir um número exato, mínimo ou máximo.

## Por que importa
Verificar o envio complementa a simulação da resposta e detecta integrações que deixam de chamar um serviço ou passam a chamá-lo duas vezes.

## Como funciona
Verifique os pedidos obrigatórios do cenário com quantidade explícita e consulte também os pedidos que não deveriam ocorrer.

## Exemplo
Após o fluxo de confirmação, a verificação pode exigir que o aviso tenha sido enviado exatamente uma vez.

## Limites e trade-offs
Verificação por caminho amplo conta chamadas de origens distintas, e verificar apenas presença deixa passar envio duplicado.

## Como verificar
Remova uma chamada do fluxo em teste e confirme que a verificação passa a falhar indicando a contagem encontrada.

## Conexões
- [[ms-request-matchers]] — Veja também: MockServer: corresponder pedidos com precisão.
- [[ms-response-verification]] — Veja também: MockServer: verificar respostas registradas.

## Fontes
- [MockServer — Verificar pedidos](https://www.mock-server.com/mock_server/verification.html) — verificação por quantidade e por sequência; consultado em 2026-10-03.
- [MockServer — repositório oficial](https://github.com/mock-server/mockserver) — código-fonte, versões e documentação do projeto; consultado em 2026-10-03.

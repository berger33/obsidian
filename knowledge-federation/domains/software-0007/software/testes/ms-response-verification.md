---
id: software.testes.tranche20.001382
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
fontes: ["https://www.mock-server.com/proxy/verification.html", "https://www.mock-server.com/mock_server/verification.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# MockServer: verificar respostas registradas

## Em uma frase
Quando a verificação inclui correspondência de resposta, a contagem passa a considerar os pares de pedido e resposta registrados no proxy.

## Por que importa
Contar pares verifica o que o sistema sob teste respondeu, não apenas o que enviou, cobrindo falhas de resposta incorreta sob condição específica.

## Como funciona
Use a verificação de resposta quando o sistema estiver atrás do proxy e combine correspondência de pedido e de resposta quando a ordem importar.

## Exemplo
A verificação pode exigir que a resposta de erro tenha sido devolvida ao menos uma vez para o pedido de pagamento recusado.

## Limites e trade-offs
Sem combinar pedido e resposta, a contagem pode atribuir resposta de um caminho a pedido de outro, e a ordem dos pares exige verificação de sequência.

## Como verificar
Aponte o proxy para um serviço que responde de forma diferente e confirme que a verificação detecta a resposta observada.

## Conexões
- [[ms-verification]] — Veja também: MockServer: verificar o que foi recebido.
- [[ms-proxy-and-record-replay]] — Veja também: MockServer: gravar tráfego com proxy.

## Fontes
- [MockServer — Verificar respostas](https://www.mock-server.com/proxy/verification.html) — verificação de respostas gravadas e pares pedido-resposta; consultado em 2026-10-03.
- [MockServer — Verificar pedidos](https://www.mock-server.com/mock_server/verification.html) — verificação por quantidade e por sequência; consultado em 2026-10-03.

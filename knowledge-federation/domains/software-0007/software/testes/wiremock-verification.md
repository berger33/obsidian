---
id: software.testes.tranche17.001122
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-17.md"
fontes: ["https://wiremock.org/docs/verifying/", "https://wiremock.org/docs/stubbing/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# WireMock: verificar chamadas recebidas

## Em uma frase
O servidor registra as requisições e permite verificar ocorrências por critérios, contando chamadas a uma rota específica.

## Por que importa
Verificar o efeito das chamadas confirma que o cliente comunicou o que deveria, cobrindo falhas de integração que a resposta simulada não revela.

## Como funciona
Verifique contagem exata ou mínima por critério relevante, evitando condições amplas que sempre encontram alguma chamada.

## Exemplo
Um fluxo de notificação pode exigir exatamente uma chamada ao endpoint de envio após a confirmação do pedido.

## Limites e trade-offs
Contagens baseadas em qualquer requisição passam mesmo quando o cliente chama a rota errada, e verificações esquecidas deixam a suíte silenciosa.

## Como verificar
Execute o fluxo e verifique a contagem da rota esperada, depois remova a chamada do cliente e confirme que a verificação falha.

## Conexões
- [[wiremock-fault-simulation]] — Veja também: WireMock: injetar falhas e atrasos.
- [[wiremock-record-playback]] — Veja também: WireMock: gravar tráfego e reproduzir.

## Fontes
- [WireMock — Verifying](https://wiremock.org/docs/verifying/) — verificação de chamadas recebidas e contagem por critério; consultado em 2026-10-03.
- [WireMock — Stubbing](https://wiremock.org/docs/stubbing/) — mapeamentos de stub, respostas predefinidas e prioridades; consultado em 2026-10-03.

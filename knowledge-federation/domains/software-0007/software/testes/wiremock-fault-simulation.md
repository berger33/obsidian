---
id: software.testes.tranche17.001121
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
fontes: ["https://wiremock.org/docs/simulating-faults/", "https://wiremock.org/docs/stubbing/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# WireMock: injetar falhas e atrasos

## Em uma frase
O servidor pode responder com atraso fixo ou variável, encerrar conexões e devolver respostas malformadas para testar o tratamento de falhas do cliente.

## Por que importa
Caminhos de erro raramente ocorrem em ambiente controlado, e a injeção deliberada verifica se o cliente trata tempo esgotado e resposta inválida.

## Como funciona
Isole os stubs de falha por rota ou etiqueta, use atrasos que excedam o limite do cliente e verifique a mensagem exibida.

## Exemplo
Um stub pode atrasar a resposta além do tempo limite do cliente para confirmar que a interface mostra mensagem de indisponibilidade.

## Limites e trade-offs
Falhas injetadas em stubs compartilhados afetam outros testes, e atrasos muito longos alongam a suíte sem necessidade.

## Como verificar
Injete atraso acima do limite configurado e confirme que o cliente desiste no prazo e registra o caminho de erro previsto.

## Conexões
- [[wiremock-priorities]] — Veja também: WireMock: resolver sobreposição com prioridades.
- [[wiremock-verification]] — Veja também: WireMock: verificar chamadas recebidas.

## Fontes
- [WireMock — Simulating faults](https://wiremock.org/docs/simulating-faults/) — injeção de atrasos, falhas de conexão e respostas malformadas; consultado em 2026-10-03.
- [WireMock — Stubbing](https://wiremock.org/docs/stubbing/) — mapeamentos de stub, respostas predefinidas e prioridades; consultado em 2026-10-03.

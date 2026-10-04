---
id: software.testes.tranche17.001125
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
fontes: ["https://wiremock.org/docs/stubbing/", "https://wiremock.org/docs/record-playback/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# WireMock: reconhecer limites da simulação

## Em uma frase
O simulador reproduz respostas definidas, sem lógica de negócio, persistência real nem garantia de que o serviço verdadeiro se comporta assim.

## Por que importa
Confundir simulação com integração verificada produz falsa segurança, e divergências de contrato só aparecem quando o serviço real é exercitado.

## Como funciona
Use o simulador para isolar o cliente, complemente com testes de contrato contra o serviço real e revise os stubs quando o contrato mudar.

## Exemplo
Um cliente pode passar em todos os testes com stubs desatualizados e falhar em produção porque o serviço mudou o formato de um campo.

## Limites e trade-offs
Stubs versionados sem dono envelhecem silenciosamente, e a gravação antiga pode descrever comportamento já corrigido.

## Como verificar
Compare um stub com a resposta do serviço real para a mesma requisição e trate cada diferença como pendência de atualização.

## Conexões
- [[wiremock-standalone-and-ci]] — Veja também: WireMock: executar de forma autônoma no pipeline.

## Fontes
- [WireMock — Stubbing](https://wiremock.org/docs/stubbing/) — mapeamentos de stub, respostas predefinidas e prioridades; consultado em 2026-10-03.
- [WireMock — Record and playback](https://wiremock.org/docs/record-playback/) — gravação de tráfego real e geração automática de stubs; consultado em 2026-10-03.

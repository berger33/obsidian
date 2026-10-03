---
id: software.testes.tranche17.001123
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
fontes: ["https://wiremock.org/docs/record-playback/", "https://wiremock.org/docs/stubbing/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# WireMock: gravar tráfego e reproduzir

## Em uma frase
O servidor pode atuar como intermediário, capturar respostas de um serviço real e gerar stubs automaticamente a partir do tráfego observado.

## Por que importa
Gravar um serviço existente acelera a criação de um ambiente simulado sem inventar respostas que talvez não correspondam ao real.

## Como funciona
Aponte o cliente para o intermediário, limite a captura às rotas de interesse e revise os stubs gerados antes de versioná-los.

## Exemplo
Uma integração de terceiros pode ser gravada uma vez e reproduzida nas execuções seguintes, evitando dependência de rede.

## Limites e trade-offs
Cabeçalhos sensíveis capturados precisam ser removidos, e respostas com identificadores voláteis exigem ajuste das condições de correspondência.

## Como verificar
Grave uma sessão curta, reproduza sem o serviço real e confirme que o cliente recebe as mesmas respostas observadas.

## Conexões
- [[wiremock-verification]] — Veja também: WireMock: verificar chamadas recebidas.
- [[wiremock-standalone-and-ci]] — Veja também: WireMock: executar de forma autônoma no pipeline.

## Fontes
- [WireMock — Record and playback](https://wiremock.org/docs/record-playback/) — gravação de tráfego real e geração automática de stubs; consultado em 2026-10-03.
- [WireMock — Stubbing](https://wiremock.org/docs/stubbing/) — mapeamentos de stub, respostas predefinidas e prioridades; consultado em 2026-10-03.

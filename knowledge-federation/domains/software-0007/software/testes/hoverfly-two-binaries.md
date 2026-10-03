---
id: software.testes.tranche22.001641
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-22.md"
fontes: ["https://docs.hoverfly.io/en/latest/pages/introduction/gettingstarted.html", "https://github.com/SpectoLabs/hoverfly/blob/master/README.md"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Hoverfly: o par hoverfly + hoverctl

## Em uma frase
A ferramenta são dois binários: hoverfly, o aplicativo que faz o trabalho pesado como proxy server, webserver e endpoints de API, e hoverctl, a CLI que configura e controla o hoverfly — inclusive rodando-o como daemon.

## Por que importa
Separar engine de controle deixa o ciclo de desenvolvimento barato: o proxy permanece de pé entre execuções de teste, e a CLI religa modos e injeta simulações sem reiniciar nada.

## Como funciona
O mínimo do getting started oficial: hoverctl version e hoverfly -version para validar a instalação, hoverctl start para subir o daemon e hoverctl stop para derrubar.

## Exemplo
hoverctl logs serve como prova de vida — a doc ensina a checar a string "serving proxy" no log para confirmar que o hoverfly está de pé.

## Limites e trade-offs
Os dois binários precisam estar num diretório do PATH (a instrução é explícita sobre extrair ambos para lá); versões desalinhadas entre par geram erros confusos de protocolo.

## Como verificar
Extraia os dois binários para o mesmo PATH, rode hoverctl start e grep "serving proxy" na saída de hoverctl logs.

## Conexões
- [[hoverfly-what-it-is]] — Veja também: Hoverfly: simulações de API num binário.
- [[hoverfly-capture-mode]] — Veja também: Hoverfly: capture grava o tráfego real.

## Fontes
- [Hoverfly — Getting Started](https://docs.hoverfly.io/en/latest/pages/introduction/gettingstarted.html) — binários hoverfly/hoverctl, start, logs e stop; consultado em 2026-10-03.
- [Hoverfly — README oficial](https://github.com/SpectoLabs/hoverfly/blob/master/README.md) — proposta, quickstart, build em Go e contribuição; consultado em 2026-10-03.

---
id: software.testes.tranche22.001644
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
fontes: ["https://docs.hoverfly.io/en/stable/pages/tutorials/basic/capturingsequences/capturingsequences.html", "https://docs.hoverfly.io/en/latest/index.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Hoverfly: sequências para APIs com estado

## Em uma frase
Por default o hoverfly guarda um par request/resposta por vez; para APIs stateful — mesma chamada, respostas que mudam — liga-se a gravação com hoverctl mode capture --stateful, que captura a sequência inteira.

## Por que importa
Uma API de checkout com session tokens é intratável como mapa estático url→resposta; a sequência gravada preserva a ordem que o protocolo exige e o teste replay repassa a narrativa.

## Como funciona
O tutorial mostra dois curls seguidos contra time.jsontest.com capturados como dois pares request/resposta da mesma requisição, distinguíveis pelo estado associado.

## Exemplo
Na simulação gravada, cada par carrega requiresState {"sequence:1": "1"} e transições com transitionsState {"sequence:1": "2"} — o replay anda na sequência e para no fim dela.

## Limites e trade-offs
Chaves "sequence:" são inicializadas automaticamente com 1 na importação; nomes de estado mais expressivos precisam ser criados antes, por exemplo hoverctl state set shopping-basket empty.

## Como verificar
Rode a simulação de duas etapas três vezes seguidas em simulate e observe o que acontece depois da última transição de estado.

## Conexões
- [[hoverfly-export-simulation]] — Veja também: Hoverfly: exportar filtrando por URL.
- [[hoverfly-simulate-mode]] — Veja também: Hoverfly: simulate é o replay sem rede.

## Fontes
- [Hoverfly — Capturing a stateful sequence](https://docs.hoverfly.io/en/stable/pages/tutorials/basic/capturingsequences/capturingsequences.html) — capture --stateful, requiresState/transitionsState e hoverctl state; consultado em 2026-10-03.
- [Hoverfly — documentação inicial](https://docs.hoverfly.io/en/latest/index.html) — conceitos-chave, reference e troubleshooting do v1.12.15; consultado em 2026-10-03.

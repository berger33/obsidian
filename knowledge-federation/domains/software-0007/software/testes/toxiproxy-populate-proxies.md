---
id: software.testes.tranche21.001542
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-21.md"
fontes: ["https://github.com/Shopify/toxiproxy", "https://github.com/Shopify/toxiproxy/tree/main/client"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Toxiproxy: popular os proxies no boot

## Em uma frase
O mapeamento de endpoints — nome, listen e upstream — é registrado cedo no boot via populate, arquivo config/toxiproxy.json lido com -config ou comandos do toxiproxy-cli create.

## Por que importa
Antes de qualquer conexão de teste passar pelo Toxiproxy, ele precisa saber para onde encaminhar cada porta, e o populate idempotente foi desenhado para rodar a cada start.

## Como funciona
Defina a lista de proxies no formato nome_escuta_destino com habilitação, use portas fora da faixa efêmera e deixe a aplicação conectar-se só pelos listen.

## Exemplo
shopify_test_redis_master escutando 22220 e encaminhando para 6379 é o exemplo canônico da documentação.

## Limites e trade-offs
Nomes colidindo entre aplicações no mesmo Toxiproxy exigem o padrão <app>_<env>_<data store>_<shard> sugerido; a porta 0 do listen gera escolha efêmera devolvida na resposta.

## Como verificar
Chame populate duas vezes com o mesmo conteúdo e confirme que o servidor aceita sem duplicar os proxies.

## Conexões
- [[toxiproxy-install-server]] — Veja também: Toxiproxy: obter e subir o servidor.
- [[toxiproxy-latency-bandwidth]] — Veja também: Toxiproxy: latência e banda pelos toxic latency e bandwidth.

## Fontes
- [Toxiproxy — README oficial](https://github.com/Shopify/toxiproxy) — proposta, instalação, populate, toxics e HTTP API; consultado em 2026-10-03.
- [Toxiproxy — cliente Go](https://github.com/Shopify/toxiproxy/tree/main/client) — cliente oficial embutido no repositório; consultado em 2026-10-03.

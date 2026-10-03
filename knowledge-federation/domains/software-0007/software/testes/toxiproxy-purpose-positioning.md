---
id: software.testes.tranche21.001540
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
fontes: ["https://github.com/Shopify/toxiproxy", "https://github.com/Shopify/toxiproxy-ruby"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Toxiproxy: provar a resiliência em teste

## Em uma frase
O Toxiproxy é uma estrutura para simular condições de rede em testes, desenvolvimento e CI, com adulteração determinística das conexões e espaço para caos aleatório.

## Por que importa
Provar que a aplicação não tem ponto único de falha exige provocar a falha sob controle repetível, algo que ferramentas de shell como nc não entregam de forma portável nem sem root.

## Como funciona
Aponte as conexões de teste do seu app pelo proxy e manipule a saúde do link por API enquanto o caso roda.

## Exemplo
A mesma suíte que valida o caminho feliz ganha um caso "Redis lento em um segundo" sem tocar no cliente de código de produção.

## Limites e trade-offs
É um proxy TCP: protocolos que exigem terminação TLS inspecionada ou UDP exigem atenção redobrada ao modelo mental do que está sendo perturbado.

## Como verificar
Execute o exemplo de latência de 1000 ms e confirme que a chamada levou ao menos um segundo.

## Conexões
- [[toxiproxy-install-server]] — Veja também: Toxiproxy: obter e subir o servidor.

## Fontes
- [Toxiproxy — README oficial](https://github.com/Shopify/toxiproxy) — proposta, instalação, populate, toxics e HTTP API; consultado em 2026-10-03.
- [Toxiproxy — cliente Ruby](https://github.com/Shopify/toxiproxy-ruby) — exemplos de populate, down e apply; consultado em 2026-10-03.

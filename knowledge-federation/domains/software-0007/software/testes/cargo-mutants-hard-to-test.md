---
id: software.testes.tranche21.001539
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
fontes: ["https://github.com/sourcefrog/cargo-mutants", "https://crates.io/crates/cargo-mutants"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# cargo-mutants: funções de efeito difícil de testar

## Em uma frase
Funções que gerenciam caches ou efeitos de performance podem sobreviver à mutação sem poderem ser simplesmente removidas; o README orienta torná-las observáveis ou pular com aviso.

## Por que importa
O valor do achado aqui é a conversa: a ferramenta aponta que aquele trecho crítico não está coberto e exige uma decisão registrada.

## Como funciona
Quando a asserção direta for inviável, exponha um contador de alocações ou de misses de cache e teste por esse observável.

## Exemplo
Um cache intencionalmente best-effort pode ganhar um teste de duas chamadas seguidas medindo a segunda vinda do mapa interno.

## Limites e trade-offs
O skip é a saída barata demais: o README o lista como forma de silenciar o aviso e explicar a decisão, não de resolver o problema.

## Como verificar
Converta um sobrevivente de cache em teste por contador e confirme que o mutante passa a ser pego.

## Conexões
- [[cargo-mutants-speed-advice]] — Veja também: cargo-mutants: acelerar builds para acelerar mutantes.

## Fontes
- [cargo-mutants — README oficial](https://github.com/sourcefrog/cargo-mutants) — proposta, resultados, skip e saída; consultado em 2026-10-03.
- [cargo-mutants — pacote no crates.io](https://crates.io/crates/cargo-mutants) — versões publicadas e metadados do pacote; consultado em 2026-10-03.

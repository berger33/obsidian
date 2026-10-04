---
id: software.testes.tranche16.000978
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-16.md"
fontes: ["https://github.com/tsenart/vegeta", "https://pkg.go.dev/github.com/tsenart/vegeta/v12/lib"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Vegeta: configurar tempo limite e transporte HTTP

## Em uma frase
O ataque aceita tempo limite por requisição, conexões persistentes, negociação de versão do protocolo e opções de certificado para ambientes de teste.

## Por que importa
Sem limite, uma resposta que nunca chega prende o trabalhador e distorce a medição; com limite curto demais, a carga mede a paciência do cliente.

## Como funciona
Declare tempo limite compatível com a expectativa do serviço, mantenha conexões persistentes e restrinja a validação de certificado apenas a ambientes controlados.

## Exemplo
Um tempo limite próximo do percentil alto observado evita que requisições presas consumam trabalhadores indefinidamente.

## Limites e trade-offs
Ignorar certificados ou redirecionamentos em ambiente permanente esconde falhas de configuração que apareceriam para pessoas usuárias reais.

## Como verificar
Compare uma execução com e sem conexões persistentes e observe o efeito no custo de estabelecimento antes de fixar a configuração.

## Conexões
- [[vegeta-rate-workers-connections]] — Veja também: Vegeta: distinguir taxa, trabalhadores e conexões.
- [[vegeta-thresholds-in-ci]] — Veja também: Vegeta: transformar o resumo em verificação automática.

## Fontes
- [Vegeta — repositório oficial](https://github.com/tsenart/vegeta) — manual de uso: attack, report, plot, encode, dump e opções de conexão; consultado em 2026-10-03.
- [Vegeta — biblioteca Go](https://pkg.go.dev/github.com/tsenart/vegeta/v12/lib) — API de taxa, atacante, alvos e métricas para uso programático; consultado em 2026-10-03.

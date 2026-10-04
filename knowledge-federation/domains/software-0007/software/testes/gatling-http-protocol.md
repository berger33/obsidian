---
id: software.testes.tranche17.001064
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
fontes: ["https://docs.gatling.io/reference/script/http/protocol/", "https://docs.gatling.io/concepts/simulation/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Gatling: configurar o protocolo HTTP compartilhado

## Em uma frase
O construtor de protocolo reúne endereço base, cabeçalhos, versão do protocolo e política de conexões aplicados a todos os cenários da simulação.

## Por que importa
Centralizar a configuração evita repetir cabeçalhos em cada requisição e mantém coerência quando o alvo muda entre ambientes.

## Como funciona
Declare o endereço base e os cabeçalhos comuns no protocolo, parametrize o que varia por ambiente e evite duplicar valores nas requisições.

## Exemplo
Um protocolo pode fixar o tipo de conteúdo esperado e a identificação do cliente, deixando cada requisição apenas com seu caminho e corpo.

## Limites e trade-offs
Políticas de conexão e de compartilhamento de conexões alteram o custo medido, e a escolha precisa ser coerente com o cliente real.

## Como verificar
Compare uma execução com e sem reaproveitamento de conexões e observe a diferença antes de fixar a política do protocolo.

## Conexões
- [[gatling-assertions]] — Veja também: Gatling: reprovar a execução com asserções.
- [[gatling-reports-and-ci]] — Veja também: Gatling: consumir relatórios e integrar ao pipeline.

## Fontes
- [Gatling — HTTP protocol](https://docs.gatling.io/reference/script/http/protocol/) — endereço base, cabeçalhos comuns e políticas de conexão; consultado em 2026-10-03.
- [Gatling — Simulation](https://docs.gatling.io/concepts/simulation/) — estrutura da simulação, protocolo, cenários e relatório de execução; consultado em 2026-10-03.

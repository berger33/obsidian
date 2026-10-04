---
id: software.testes.tranche08.000197
tipo: tecnica
dominio: software
subdominio: testes
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-08.md"
fontes: ["https://developer.hashicorp.com/terraform/language/tests/mocking", "https://developer.hashicorp.com/terraform/cli/test"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Terraform: testar data sources e outputs calculados

## Em uma frase
Teste separadamente a lógica de composição dos outputs e a resolução real de data sources externos.

## Por que importa
Um mock pode validar transformação de atributos, mas não confirma filtros, permissões ou disponibilidade dos objetos consultados no cloud.

## Como funciona
No teste isolado, forneça valores controlados e verifique expressão/derivação; em integração, use fixture identificável para validar consulta real quando necessária.

## Exemplo
Mock fornece subnet id previsível para testar composição de rede; um sandbox verifica que filtro por tags encontra exatamente os recursos esperados.

## Limites e trade-offs
Data source pode depender de estado fora do repositório e mudar entre execuções; o teste real deve declarar pré-condições e cleanup.

## Como verificar
Compare output de mock e sandbox e confirme que cenário de nenhum resultado e de múltiplos resultados não passa silenciosamente.

## Conexões
- [[terraform-tests-mock-provider-escopo]] — Veja também: Terraform: delimitar mocks de provider.
- [[terraform-plan-assertions-estado-esperado]] — Veja também: Terraform: verificar plano contra mudança de infraestrutura esperada.

## Fontes
- [Terraform — Mocking](https://developer.hashicorp.com/terraform/language/tests/mocking) — mock_provider, valores computados e overrides; consultado em 2026-10-02.
- [Terraform — Testing features](https://developer.hashicorp.com/terraform/cli/test) — validações e terraform test para comportamento de configuração; consultado em 2026-10-02.

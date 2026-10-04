---
id: software.testes.tranche08.000193
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
fontes: ["https://developer.hashicorp.com/terraform/language/validate", "https://developer.hashicorp.com/terraform/language/tests"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Terraform: testar validação de variáveis como contrato

## Em uma frase
Codifique limites e combinações inválidas no módulo e cubra cada validação com entradas que cruzem a fronteira.

## Por que importa
Validações claras recusam configuração incorreta cedo e tornam o contrato do módulo verificável antes de qualquer recurso ser aplicado.

## Como funciona
Para cada condição, crie caso aceito no limite e caso rejeitado imediatamente fora dele. Mantenha mensagem de erro útil e não replique regra de forma divergente.

## Exemplo
Um parâmetro de retenção permite mínimo documentado e falha com valor inferior; outro teste cobre combinação incompatível de flags.

## Limites e trade-offs
Validação de variável não comprova que API remota aceita todo valor nem que recursos são criados corretamente.

## Como verificar
Execute `terraform validate` e testes de linguagem para ambos os lados da condição; confirme que erro é atribuível à variável esperada.

## Conexões
- [[terraform-check-block-nao-blocking]] — Veja também: Terraform: interpretar check blocks sem tratá-los como preconditions.
- [[terraform-plan-assertions-estado-esperado]] — Veja também: Terraform: verificar plano contra mudança de infraestrutura esperada.

## Fontes
- [Terraform — Validate configuration](https://developer.hashicorp.com/terraform/language/validate) — validação estrutural e condições de variáveis; consultado em 2026-10-02.
- [Terraform — Tests](https://developer.hashicorp.com/terraform/language/tests) — run blocks, asserts, plan/apply e provider configuration; consultado em 2026-10-02.

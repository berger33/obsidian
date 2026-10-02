---
id: software.testes.tranche08.000190
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
fontes: ["https://developer.hashicorp.com/terraform/cli/test", "https://developer.hashicorp.com/terraform/language/tests"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Terraform: distinguir validate de terraform test

## Em uma frase
Use validate para verificar configuração e terraform test para exercitar assertions e comportamento em módulos ou infraestrutura de teste.

## Por que importa
Validação estrutural não prova que provider real cria o recurso esperado; testes podem planejar ou aplicar recursos conforme o run configurado.

## Como funciona
Separe checagem de sintaxe/referências de cenários declarativos com inputs, runs e assertions. Documente quais testes usam mocks e quais contatam cloud.

## Exemplo
CI executa validate em toda mudança e um teste isolado verifica que combinação de variáveis produz a configuração esperada sem acesso à conta de produção.

## Limites e trade-offs
Comandos e efeitos dependem da versão, provider e configuração; `terraform test` pode provisionar recursos e deve ter escopo e credenciais controlados.

## Como verificar
Inspecione os run blocks e plano, execute no diretório temporário e confirme que nenhuma credencial de produção é exigida em teste unitário.

## Conexões
- [[terraform-tests-mock-provider-escopo]] — Veja também: Terraform: delimitar mocks de provider.
- [[terraform-variable-validation-contract]] — Veja também: Terraform: testar validação de variáveis como contrato.

## Fontes
- [Terraform — Testing features](https://developer.hashicorp.com/terraform/cli/test) — validações e terraform test para comportamento de configuração; consultado em 2026-10-02.
- [Terraform — Tests](https://developer.hashicorp.com/terraform/language/tests) — run blocks, asserts, plan/apply e provider configuration; consultado em 2026-10-02.

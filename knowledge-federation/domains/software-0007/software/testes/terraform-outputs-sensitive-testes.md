---
id: software.testes.tranche08.000195
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

# Terraform: testar outputs sem expor valores sensíveis

## Em uma frase
Valide presença e derivação de outputs sem imprimir segredos em logs ou snapshots de CI.

## Por que importa
Outputs podem propagar atributos sensíveis para relatórios; assertions e diagnóstico devem preservar confidencialidade tanto quanto o estado Terraform.

## Como funciona
Marque e trate valores sensíveis conforme o uso, teste saídas não secretas diretamente e evite interpolar segredo em mensagens ou artefatos de CI.

## Exemplo
O teste verifica que identificador de recurso aparece no output, mas compara apenas metadado não secreto de credencial e nunca imprime valor completo.

## Limites e trade-offs
Sensibilidade no Terraform não impede todo vazamento em ferramentas externas ou configuração incorreta; controle de state e logs continua necessário.

## Como verificar
Execute com logs examináveis, procure valores canário e valide permissões de state/artifacts; confirme assertions sem ecoar o conteúdo sensível.

## Conexões
- [[docker-build-secrets-nao-arg-env]] — Veja também: Docker: não inserir secrets em ARG, ENV ou layers.
- [[gha-artifact-retention-provenance]] — Veja também: GitHub Actions: reter artifacts sem perder proveniência.

## Fontes
- [Terraform — Testing features](https://developer.hashicorp.com/terraform/cli/test) — validações e terraform test para comportamento de configuração; consultado em 2026-10-02.
- [Terraform — Tests](https://developer.hashicorp.com/terraform/language/tests) — run blocks, asserts, plan/apply e provider configuration; consultado em 2026-10-02.

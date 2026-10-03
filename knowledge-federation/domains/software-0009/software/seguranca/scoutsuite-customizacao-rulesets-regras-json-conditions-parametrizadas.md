---
id: software.seguranca.tranche11.001015
tipo: tecnica
dominio: software
subdominio: seguranca
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-11.md"
fontes: ["https://raw.githubusercontent.com/nccgroup/ScoutSuite/master/README.md", "https://raw.githubusercontent.com/nccgroup/ScoutSuite/master/ScoutSuite/__main__.py"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Anatomia do Motor de Regras do Scout Suite (**`Ruleset` & `ProcessingEngine`**): Como Escrever **Regras e Rulesets JSON Customizados (`--ruleset`)**

## Em uma frase
Como o Scout Suite decide se uma configuração coletada da nuvem é um risco **`danger` (Vermelho)** ou **`warning` (Amarelo)**? Através do seu motor declarativo de regras JSON (**`ScoutSuite/core/ruleset.py`** e **`processingengine.py`**)!

## Por que importa
No Scout Suite, existem dois tipos de arquivos JSON de regras: **(1) Definições de Regras (*Rule Definitions*, ex.: `iam-password-policy-minimum-length.json`)** — que contêm a lógica booleana no array `conditions` (usando operadores como `equal`, `notEqual`, `lessThan`, `moreThan`, `null`, `notNull`, `true`, `false`, `containAtLeastOneOf`, `withKey`, etc. sobre os caminhos do JSON de recursos coletados!) e aceitam parâmetros variáveis (`_ARG_0_`, `_ARG_1_`); e **(2) Rulesets (`default.json`, `cis-1.2.0.json` ou um `corporate-ruleset.json` customizado)** — que listam quais regras estão habilitadas (`"enabled": true`), qual o nível de severidade (`"level": "danger"` ou `"warning"`) e quais valores passar em `"args"`!

## Como funciona
Isso significa que você pode aumentar o rigor da política de senhas ou de retenção de logs da sua empresa apenas editando `"args": [16]` no seu arquivo `--ruleset corporate.json`, sem tocar em uma única linha de código Python!

## Exemplo
```json
{
  "about": "Ruleset Corporativo Customizado para Auditoria AWS (SecOps)",
  "rules": {
    "iam-password-policy-minimum-length.json": [
      {
        "enabled": true,
        "level": "danger",
        "args": [16]
      }
    ],
    "s3-bucket-no-mfa-delete.json": [
      {
        "enabled": true,
        "level": "warning"
      }
    ]
  }
}
```

## Limites e trade-offs
Olhe que arquitetura elegante: como a definição genérica da regra (`iam-password-policy-minimum-length.json`) é separada da sua instanciação parametrizada no Ruleset (`"args": [16]`), uma mesma regra base serve tanto para o benchmark CIS padrão (que pode exigir 14 caracteres) quanto para a política interna de um banco (que exige 16 caracteres) via **`scout aws --ruleset corporate-ruleset.json`**!

## Como verificar
Combine `--ruleset` com `--fetch-local` para testar instantaneamente suas novas regras JSON sobre um snapshot de conta já baixado.

## Conexões
- [[scoutsuite-auditoria-gcp-projects-folders-organizations-service-account]] — Veja também: Scout Suite no **Google Cloud Platform (`scout gcp`)**: Auditoria em Escala por **Organization (`--organization-id`), Folder (`--folder-id`) e `--all-projects`**.
- [[scoutsuite-reexecucao-offline-fetch-local-update-comparacao-diffs]] — Veja também: Workflow Avançado do Scout Suite: Reavaliação Instantânea com **`--fetch-local`**, Atualização Parcial (**`--update`**) e Exportação JSON/SQLite (`--result-format`).
- [[scoutsuite-arquitetura-auditoria-multi-cloud-offline-nccgroup]] — Referência cruzada direta com scoutsuite-arquitetura-auditoria-multi-cloud-offline-nccgroup.
- [[scoutsuite-gestao-excecoes-exceptions-json-mapeamento-ip-ranges]] — Referência cruzada direta com scoutsuite-gestao-excecoes-exceptions-json-mapeamento-ip-ranges.

## Fontes
- [NCC Group Scout Suite Official GitHub — Multi-Cloud Security Auditing Tool](https://raw.githubusercontent.com/nccgroup/ScoutSuite/master/README.md) — repositório oficial do Scout Suite cobrindo auditoria point-in-time offline para AWS, Azure, GCP, Alibaba Cloud, OCI, DigitalOcean e Kubernetes; consultado em 2026-10-03.
- [Scout Suite Official CLI & Engine Implementation (`ScoutSuite/__main__.py`)](https://raw.githubusercontent.com/nccgroup/ScoutSuite/master/ScoutSuite/__main__.py) — implementação oficial dos provedores, parâmetros de autenticação, `--fetch-local`, `--update`, `--ruleset`, `--exceptions` e `--ip-ranges`; consultado em 2026-10-03.
